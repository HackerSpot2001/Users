from django.http.response import JsonResponse
from Helpers.Utils import handle_exception, SuccessResp, handle_params, gen_id, get_initials, generate_password
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import auth as authentication 
from .models import UserLogin, UserLoginHistory, Party
from django.utils.timezone import now 
from django.db.models import Q 

# ALL Get Requests
@require_http_methods(['GET',])
def logoff(req):
    try:
        if req.user.is_authenticated:
            authentication.logout(req)

        res = SuccessResp

    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)


@require_http_methods(['GET',])
def get_profile(req):
    try:
        res     = SuccessResp
        user    = req.user

        if user.is_anonymous:
            raise Exception("HANDLED:User is not logged-in.")

        user = UserLogin.objects.get(user_login_id = user.user_login_id)

        record = {
            'profile' : {
                'fullname'          : user.get_full_name(),
                'username'          : user.username,
                'marital_status'    : user.marital_status_id,
                'salutation'        : user.salutation_id,
                'gender'            : user.gender_id,
                'dob'               : user.birth_date,
                'party_id'          : user.party_id,
                'party_type'        : user.party.party_type_id,
            }
        } 


        res['record'] = record



    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)



@csrf_exempt
@require_http_methods(['POST',])
def login_user(req):
    try:
        params      = handle_params(req)
        username    = params.get("username", None )
        password    = params.get("password" , None)

        if username == None or password == None:
            raise Exception("HANDLED: Username and Password is required to login.")

        if req.user.is_authenticated : 
            raise Exception("HANDLED: User is already logged-in.")

        if not UserLogin.objects.filter(Q(username=username) | Q(user_login_id=username)).exists():
            raise Exception("HANDLED: User not found.")

        userObj = UserLogin.objects.get(Q(username=username) | Q(user_login_id=username))
        if (userObj.is_active == False): raise Exception("HANDLED: Account is deactivated.")

        user    = authentication.authenticate(req,user_login_id=userObj.user_login_id, password=password)
        if user is  None: raise Exception("HANDLED: Wrong Credentials")
        
        his_args = {
            'user_login_id' : userObj.user_login_id,
            'visit_id' : gen_id(),
            'password_used':password,
            'successful_login' :'Y',
            'party_id' : userObj.party_id,
        }
        UserLoginHistory.objects.filter(user_login_id = userObj.user_login_id, thru_date=None ).update(thru_date = now(), updated_stamp=now() )
        usl_h = UserLoginHistory.objects.create(**his_args)
        # logger.debug ("User history created with id:'%s'",  usl_h.user_login_history_id)
        
        res = SuccessResp
        authentication.login(req, user)


    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)


@csrf_exempt
@require_http_methods(['POST',])
def create_user(req):
    try:
        params          = handle_params(req)
        user_login_id   = gen_id('UL_',16)
        username        = params.get("username", user_login_id )
        password        = params.get("password" , generate_password(10))
        firstname       = str(params.get("firstname" , ''))
        lastname        = str(params.get("lastname" , ''))
        middlename      = str(params.get("middlename" , ''))
        marital_status  = str(params.get("marital_status" ,'SINGLE')).upper()
        gender          = str(params.get("gender", '' )).lower()
        bio             = params.get("bio", None )
        birth_date      = params.get("dob", None )
        marrige_date    = params.get("marrige_date" ,None)
        email           = params.get("email", None )
        initials        = get_initials(' '.join([firstname, lastname]))

        if (firstname == '' or email == None):
            raise Exception('HANDLED:email/name is required to create account.')


        if gender == 'male':
            gender_id = 'MALE'
            salutation = 'MR'

        elif gender == 'female':
            gender_id = 'FEMALE'
            salutation = 'MR'

        else:
            gender_id = 'OTHERS'
            salutation = None

        if (marital_status == 'MARRIED') and marrige_date == None:
            raise Exception("HANDLED:marrige_date parameter is required when you choose marital_status as MARRIED.")

        party_id = gen_id('PR_',15)
        party_payload = {
            'party_id'          : party_id ,
            'party_type_id'     : 'PERSON',
            'description'       : f"Party created for PERSON with PartyID: {party_id}",
            'status_id'         : 'PARTY_ENABLED',
            'created_date'      : now(),
        }
        Party.objects.create(**party_payload)
        ul_payload = {
            'user_login_id'     : user_login_id,
            'username'          : username,
            'first_name'        : firstname,
            'last_name'         : lastname,
            'middle_name'       : middlename,
            'initials'          : initials,
            'birth_date'        : birth_date,
            'salutation'        : salutation,
            'gender_id'         : gender_id,
            'marital_status_id' : marital_status,
            'marrige_date'      : marrige_date,    
            'party_id'          : party_id,
        }

        if bio   != None:   ul_payload['bio'] = bio
        if email != None:   ul_payload['email'] = email

        ul_obj = UserLogin.objects.create(**ul_payload)
        ul_obj.set_password(password)
        ul_obj.save()

        res = SuccessResp
        res['record'] = {
            'user_id'   : user_login_id,
            'party_id'  : party_id,
            'username'  : username,
        }


    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)



