from django.http.response import JsonResponse
from Helpers.Utils import handle_exception, SuccessResp, handle_params, gen_id
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import auth as authentication 
from .models import UserLogin, UserLoginHistory
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
            'profile' : user.get_deferred_fields()
        } 

        print(record)

        



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
        
        authentication.login(req, user)
        his_args = {
            'user_login_id' : userObj.user_login_id,
            'visit_id' : gen_id(),
            'password_used':password,
            'successful_login' :'Y',
            'party':userObj.party_id,
        }
        UserLoginHistory.objects.filter(user_login_id = userObj.user_login_id ).update(thru_date = now(), updated_stamp=now() )
        usl_h = UserLoginHistory.objects.create(**his_args)
        # logger.debug ("User history created with id:'%s'",  usl_h.user_login_history_id)
        
        res = SuccessResp


    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res)

