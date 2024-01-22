from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import auth as authentication 
from .models import UserLogin, UserLoginHistory, Party, PartyContactMech, TelecomNumber, PartyContent
from django.utils.timezone import now 
from django.db.models import Q 
from django.conf import settings
from .views_helpers import create_contact_mech, create_content
from Helpers.Utils import handle_exception, SuccessResp, handle_params, gen_id, get_initials, generate_password, generate_url_hash
from Helpers.Utils import checkEmail, checkMobile , get_thumbnails_from_img, save_file_to_filesystem
from json import loads,dumps


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
        user    =   req.user
        if user.is_anonymous:
            raise Exception("HANDLED:User is not logged-in.")

        pcs             = PartyContent.objects.filter( party_content_type_id='PROFILE_PIC', thru_date=None ).select_related('content').all()
        pcm_email       = PartyContactMech.objects.filter( party_id=user.party_id, verified='Y', thru_date=None, contact_mech__contact_mech_type_id='EMAIL_ADDRESS'  ).select_related('contact_mech').all()
        pcm_telecom     = PartyContactMech.objects.filter( party_id=user.party_id, verified='Y', thru_date=None, contact_mech__contact_mech_type_id='TELECOM_NUMBER' ).select_related('contact_mech').all()
        telecoms        = []
        for pcm_obj in pcm_telecom:
            data = {
                'pcm_id'                :   pcm_obj.pcm_id,
                'contact_mech_id'       :   pcm_obj.contact_mech.contact_mech_id,
                'contact_mech_type_id'  :   pcm_obj.contact_mech.contact_mech_type_id,
            }
            contact_id              = pcm_obj.contact_mech_id
            telecom_obj             = TelecomNumber.objects.get(contact_mech_id=contact_id)
            data['value']           = telecom_obj.contact_number
            data['country_code']    = telecom_obj.country_code
            telecoms.append(data)


        res = {
            'profile' : {
                'fullname'          : user.get_full_name(),
                'username'          : user.username,
                'user_login_id'     : user.user_login_id,
                'marital_status'    : user.marital_status_id,
                'salutation'        : user.salutation_id,
                'gender'            : user.gender_id,
                'dob'               : user.birth_date,
                'party_id'          : user.party_id,
                'party_type'        : user.party.party_type_id,
                'party_assets'      : {
                        pc.party_content_type_id : {
                            'party_content_id'  :   pc.party_content_id ,
                            'content_id'        :   pc.content_id ,
                            'data_resource_id'  :   pc.content.data_resource_id,
                            'object_info'       :   loads(pc.content.data_resource.object_info),
                        }
                        for pc in pcs
                },
                'contact_meches'        : {
                    'TELECOM_NUMBER'    : telecoms , 
                    'EMAIL_ADDRESS'     : [
                        {
                            'pcm_id'                :   email_obj.pcm_id,
                            'value'                 :   email_obj.contact_mech.info_string,
                            'contact_mech_id'       :   email_obj.contact_mech.contact_mech_id,
                            'contact_mech_type_id'  :   email_obj.contact_mech.contact_mech_type_id,
                        }   for email_obj in pcm_email
                    ],
                
                },
            },
            "apiresponse": {
                "type": "OK",
                "severity": "INFO",
                "message": "Operation completed successfully.",
                "code": "0000"
            }
        }


    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)



@require_http_methods(['GET',])
def activate_acc(req,user_login_id,uaid):
    try:
        hash = generate_url_hash(user_login_id)
        if (hash != uaid):
            raise Exception("HANDLED:User not identified.")
        
        ul_obj = UserLogin.objects.get(user_login_id=user_login_id)
        if (ul_obj.is_active == True):
            raise Exception('HANDLED:User is already activated')

        ul_obj.is_active = True
        ul_obj.save()
        res = SuccessResp


    except Exception as e:
        res = handle_exception(str(e))
    return JsonResponse(res)



@require_http_methods(['GET',])
def remove_account(req):
    try:
        user = req.user
        if (user.is_anonymous):
            raise Exception('HANDLED:User must be logged-in to use this API.')

        user.is_active = False
        user.save()
        authentication.logout(req)
        res = SuccessResp

    except Exception as e:
        res = handle_exception(e)

        
    return JsonResponse(res,safe=False)



@require_http_methods(['GET',])
def forgot_password(req):
    try:
        params      = handle_params(req)
        username    = params.get('username',None)
        if (username == None) or (username == ''):
            raise Exception("HANDLED:username is required.")

        if not UserLogin.objects.filter(Q(username=username) | Q(user_login_id=username)).exists():
            raise Exception("HANDLED:User not exists.")
        
        user_obj = UserLogin.objects.get(Q(username=username) | Q(user_login_id=username))
        password = generate_password()
        user_obj.set_password(password)
        user_obj.save()

        """ Communication will be sent. """ 

        res = {
            "apiresponse": {
                "type": "OK",
                "severity": "INFO",
                "message": "Your generated password has been sent to your mobile/email.",
                "code": "0000"
            }
        }
        print("Password: ", password)

    except Exception as e:
        res = handle_exception(e)

        
    return JsonResponse(res,safe=False)



@require_http_methods(['GET',])
def change_password(req):
    try:
        params      = handle_params(req)
        password    = params.get('password',None)

        if req.user.is_anonymous:
            raise Exception("HANDLED:User must be logged-in.")

        if (password == None) or (password == ''):
            raise Exception("HANDLED:new password is required.")

        
        user_obj = req.user
        user_obj.set_password(password)
        user_obj.save()

        """ Communication will be sent. """ 

        res = SuccessResp
        print("Password: ", password)

    except Exception as e:
        res = handle_exception(e)

        
    return JsonResponse(res,safe=False)



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
        if user is  None: raise Exception("HANDLED: Invalid Credentials")
        
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
        mobile          = params.get("mobile", None )
        initials        = get_initials(' '.join([firstname, lastname]))

        if (firstname == '' or email == None):
            raise Exception('HANDLED:email/name is required to create account.')

        if UserLogin.objects.filter(username=username).exists():
            raise Exception('HANDLED:Username is not available.')


        if gender == 'male':
            gender_id = 'MALE'
            salutation = 'MR'

        elif gender == 'female':
            gender_id = 'FEMALE'
            salutation = 'MR'

        else:
            gender_id = None
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
            'is_active'         : False,
        }

        if bio   != None:   ul_payload['bio'] = bio
        if email != None:   ul_payload['email'] = email

        ul_obj = UserLogin.objects.create(**ul_payload)
        ul_obj.set_password(password)
        ul_obj.save()

        if (email != None) and (email != ''):
            if not (checkEmail(email)):
                raise Exception("HANDLED:{} is not a valid mail.".format(email))
            
            create_contact_mech(contact_type="EMAIL_ADDRESS", party_id=party_id, purpose='PRIMARY_EMAIL', value=email)

        if (mobile != None) and (mobile != ''):
            if not (checkMobile(mobile)):
                raise Exception("HANDLED:{} is not a valid mobile number.".format(mobile))
            
            create_contact_mech(contact_type="TELECOM_NUMBER", party_id=party_id, purpose='PRIMARY_PHONE', value=mobile)


        activate_url = f"{settings.BASE_URL}/users/activate/{ul_obj.user_login_id}/{generate_url_hash(ul_obj.user_login_id)}"
        res = SuccessResp
        res['record'] = {
            'user_id'       : user_login_id,
            'party_id'      : party_id,
            'username'      : username,
            'activate_url'  : activate_url,
        }


    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)



@csrf_exempt
@require_http_methods(['POST',])
def update_user(req):
    try:
        params          = handle_params(req)

        if (req.user.is_anonymous):
            raise Exception('HANDLED:user must be logged-in to use this API.')
        
        user = req.user
        user.username               = params.get("username", user.username )
        user.first_name             = params.get("firstname", user.first_name )
        user.last_name              = params.get("lastname", user.last_name )
        user.middle_name            = params.get("middlename", user.middle_name )
        user.birth_date             = params.get("dob", user.birth_date )
        user.salutation             = params.get("salutation", user.salutation )
        user.marrige_date           = params.get("marrige_date", user.marrige_date )
        user.bio                    = params.get("bio", user.bio )
        user.gender_id              = params.get("gender", user.gender_id )
        user.marital_status_id      = str(params.get("marital_status", user.marital_status_id )).upper()
        user.updated_stamp          = now() 

        email                       = params.get("email",None)
        mobile                      = params.get("mobile",None)

        if (email != None) and (email != ''):
            create_contact_mech(contact_type='EMAIL_ADDRESS', party_id=user.party_id, purpose='PRIMARY_EMAIL', value=email)

        if (mobile != None) and (mobile != ''):
            create_contact_mech(contact_type='TELECOM_NUMBER', party_id=user.party_id, purpose='PRIMARY_PHONE', value=mobile)

        user.save()        
        res = SuccessResp

    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)



@csrf_exempt
@require_http_methods(['POST',])
def update_profile_pic(req):
    try:
        user            = req.user
        files           = dict(req.FILES)
        profile_pics    = files['profile_pic']
        
        if (user.is_anonymous):
            raise Exception('HANDLED:user must be logged-in to use this API.')
        
        for pp in profile_pics:
            save_obj    = save_file_to_filesystem(file=pp,initals='PP_',base_path=settings.BASE_DIR)
            thumbs      = get_thumbnails_from_img(filepath=save_obj['filepath'],extn=save_obj['file_ext'])
            object_info = {
                'original_img'  : save_obj,
                'thumbs_img'    : thumbs,
            }
            
            create_content(
                content_type='IMAGE_FRAME',
                party_id=user.party_id,
                content_name=save_obj['filename'],
                description='Profile pic uploaded to storage system',
                mime_type_id=save_obj['mime_type'],
                created_by_user_login=user.user_login_id,
                updated_by_user_login=user.user_login_id,
                object_info=dumps(object_info),
                party_content_type_id='PROFILE_PIC',
                service_name=save_obj['original_filename'],
                data_resource_name="Recieved file: {}".format(save_obj['original_filename']) ,
            )
            
        res = SuccessResp

    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)
