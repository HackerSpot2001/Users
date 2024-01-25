from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import auth as authentication 
from .models import UserLogin, UserLoginHistory
from django.utils.timezone import now 
from django.db.models import Q 
from django.conf import settings
from .views_helpers import create_content, get_user_info, modify_user
from Helpers.Utils import handle_exception, SuccessResp, handle_params, gen_id, generate_password, generate_url_hash
from Helpers.Utils import get_thumbnails_from_img, save_file_to_filesystem
from json import dumps


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
        
        # print(dir(user.party))
        res = get_user_info(user_login_id=user.user_login_id)

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

        user.is_deleted = True
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

        if not UserLogin.objects.filter(Q(username=username) | Q(user_login_id=username) , is_deleted=False).exists():
            raise Exception("HANDLED:User not exists.")
        
        user_obj = UserLogin.objects.get(Q(username=username) | Q(user_login_id=username) , Q(is_deleted=False))
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

        if not UserLogin.objects.filter(Q(username=username) | Q(user_login_id=username), is_deleted = False).exists():
            raise Exception("HANDLED: User not found.")

        userObj = UserLogin.objects.get(Q(username=username) | Q(user_login_id=username), is_deleted = False)
        if (userObj.is_active == False): raise Exception("HANDLED: Account is deactivated.")

        # if (userObj.is_deleted == True): raise Exception("HANDLED: Account is Deleted.")

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
        params              = handle_params(req)
        passwd              = params.get('password', str(generate_password(20)))
        login_id            = gen_id(initials='UL_',length=20)
        params['username']  = params.get('username', str(params.get('mobile',gen_id(length=20))))

        if (UserLogin.objects.filter(username = params.get('username'), is_deleted = False).exists()):
            raise Exception ("HANDLED: Username is not available.")

        user = UserLogin(user_login_id = login_id)
        if ('username' in params.keys()):
            user.username = params.get('username')

        user.set_password(passwd)
        user.save()

        res = modify_user(user_login_id=login_id, update_profile=False, **params)

        activate_url = f"{settings.BASE_URL}/users/activate/{login_id}/{generate_url_hash(login_id)}"
        res['record']['activation_url'] = activate_url
        # logger.debug ("User created or updated with username:'%s' and password: '%s'", login_id, passwd)

    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res, safe=False, status=200)


@csrf_exempt
@require_http_methods(['POST',])
# @group_required(('HR_Group'),login_url='login/')
def update_user(req):
    try:
        params   = handle_params(req)
        
        if req.user.is_anonymous:
            raise Exception("HANDLED: login is required to update account. ")
            
        param_login_id = params.get('user_login_id', req.user.user_login_id)
        if 'user_login_id' in params.keys():
            params.pop('user_login_id')

        if (not req.user.is_superuser) and (not req.user.groups.filter(name="HR_Group").exists() ) and (param_login_id != req.user.user_login_id):
            raise Exception("HANDLED: You are not authorized to update someone's profile")

        else:
            res = modify_user(user_login_id=param_login_id, update_profile=True,  **params)

    except Exception as e:
        res = handle_exception(e)

    return JsonResponse(res,status=200)



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
