from .models import Party, UserLogin, ContactMech, PartyContactMech, TelecomNumber, PostalAddress, PartyContent, Content,DataResource,ElectronicText, Enumeration
from django.utils.timezone import now 
from Helpers.Utils import gen_id, parse_mobile,handle_exception, get_initials, checkEmail, checkMobile
from json import loads 



def get_user_info(user_login_id):
    try:
        user = UserLogin.objects.select_related('party').get(user_login_id=user_login_id)
        party = user.party
        user_attachs = {}
        prc_args = {
            "party_id":party.party_id, 
            "thru_date__isnull":True,
            # "content__content_type_id":"IMAGE_FRAME", 
        }
        for prc_obj in PartyContent.objects.filter(**prc_args).select_related("content","party_content_type").all():
            user_attachs[prc_obj.party_content_type.party_content_type_id] = {
                "content_id"        : prc_obj.content.content_id,
                "content_name"      : prc_obj.content.content_name,
                "mime_type_id"      : prc_obj.content.mime_type_id,
                "mime_type_id"      : prc_obj.content.mime_type_id,
                "object_info"       : loads(prc_obj.content.data_resource.object_info)
            }

        # if (PartyRelatiionship.objects.filter(relationship_type_id='OWNER',party_role_to__party_id=party.party_id,party_role_from__role_type_id='INTERNAL_ORGANIZATIO').exists()):
        #     party_reln  = PartyRelatiionship.objects.get(relationship_type_id='OWNER',party_role_to__party_id=party.party_id,party_role_from__role_type_id='INTERNAL_ORGANIZATIO')
        #     prc_args["party_id"] = party_reln.party_role_from.party.party_id
        #     for prc_obj in PartyContent.objects.filter(**prc_args).select_related("content","party_content_type").all():
        #         user_attachs[prc_obj.party_content_type.party_content_type_id] = {
        #             "content_id"        : prc_obj.content.content_id,
        #             "content_name"      : prc_obj.content.content_name,
        #             "mime_type_id"      : prc_obj.content.mime_type_id,
        #             "mime_type_id"      : prc_obj.content.mime_type_id,
        #             "object_info"       : loads(prc_obj.content.data_resource.object_info)
        #         }
            
        user_attachs = {}
        prc_args = {
            "party_id":party.party_id, 
            "thru_date__isnull":True,
            "content__content_type_id":"IMAGE_FRAME", 
        }
        for prc_obj in PartyContent.objects.filter(**prc_args).select_related("content","party_content_type").all():
            user_attachs[prc_obj.party_content_type.party_content_type_id] = {
                "content_id"        : prc_obj.content.content_id,
                "content_name"      : prc_obj.content.content_name,
                "mime_type_id"      : prc_obj.content.mime_type_id,
                "mime_type_id"      : prc_obj.content.mime_type_id,
                "object_info"       : loads(prc_obj.content.data_resource.object_info)
            }

        pcm_email       = PartyContactMech.objects.filter( party_id=user.party_id, verified='Y', thru_date=None, contact_mech__contact_mech_type_id='EMAIL_ADDRESS'  ).select_related('contact_mech').all()
        pcm_telecom     = PartyContactMech.objects.filter( party_id=user.party_id, verified='Y', thru_date=None, contact_mech__contact_mech_type_id='TELECOM_NUMBER' ).select_related('contact_mech').all()
        telecoms        = []
        for pcm_obj in pcm_telecom:
            data = {
                'pcm_id'                :   pcm_obj.pcm_id,
                'contact_mech_id'       :   pcm_obj.contact_mech.contact_mech_id,
                'contact_mech_type_id'  :   pcm_obj.contact_mech.contact_mech_type_id,
                'cm_purpose_type_id'    :   pcm_obj.cm_purpose_type_id,
            }
            contact_id              = pcm_obj.contact_mech_id
            telecom_obj             = TelecomNumber.objects.get(contact_mech_id=contact_id)
            data['value']           = telecom_obj.contact_number
            data['country_code']    = telecom_obj.country_code
            telecoms.append(data)


        res = {
            "apiresponse": {
                "type": "OK",
                "severity": "INFO",
                "message": "Operation completed successfully.",
                "code": "0000"
            },
            'record' : {
                # "businesses" : [ obj for obj in PartyRelatiionship.objects.filter(relationship_type_id='OWNER',party_role_to__party_id=party.party_id,party_role_from__role_type_id='INTERNAL_ORGANIZATIO').values() ],
                'user_info'             :   {
                    'fullname'          : user.get_full_name(),
                    'firstname'         : user.first_name,
                    'last_name'         : user.last_name,
                    'middle_name'       : user.middle_name,
                    'biography'         : user.bio,
                    'username'          : user.username,
                    'user_login_id'     : user.user_login_id,
                    'marital_status'    : user.marital_status_id,
                    'salutation'        : user.salutation_id,
                    'gender'            : user.gender_id,
                    'dob'               : user.birth_date.strftime('%d-%m-%Y'),
                    'is_private'        : user.is_private,
                    'is_active'         : user.is_active,
                    'is_staff'          : user.is_staff,
                    'is_superuser'      : user.is_superuser,
                    "groups"            : [ group.name for group in user.groups.all() ],
                    'created_stamp'     : user.created_stamp.timestamp(),
                },
                'party_obj' : {
                    'party_id'          : user.party_id,
                    'party_type'        : user.party.party_type_id,
                    'created_stamp'     : user.party.created_stamp.timestamp(),
                },
                'party_assets'          : user_attachs,
                'contact_meches'        : {
                    'TELECOM_NUMBER'    : telecoms , 
                    'EMAIL_ADDRESS'     : [
                        {
                            'pcm_id'                :   email_obj.pcm_id,
                            'value'                 :   email_obj.contact_mech.info_string,
                            'contact_mech_id'       :   email_obj.contact_mech.contact_mech_id,
                            'contact_mech_type_id'  :   email_obj.contact_mech.contact_mech_type_id,
                            'cm_purpose_type_id'    :   email_obj.cm_purpose_type_id,
                        }   for email_obj in pcm_email
                    ],
                
                },
            },
        }

    except Exception as e:
        res = handle_exception(e)

    return res



def modify_user(user_login_id, update_profile=False, **params):
    user_obj            = UserLogin.objects.select_related('party').get(user_login_id=user_login_id)
    party_id            = gen_id('PR_',15)
    email_id            = params.get('email',None)
    phone               = params.get('phone',None)
    whastapp_number     = params.get('whastapp',None)
    gender              = str(params.get("gender","")).upper()
    marital_status      = str(params.get('marital_status')).upper()

    user_args = {
        # "is_superuser"      : params.get('is_superuser'     , user_obj.is_superuser),
        # "is_staff"          : params.get('is_staff'         ,   user_obj.is_staff),
        # "is_active"         : params.get('is_active'        ,   user_obj.is_active),
        "salutation"        : params.get('salutation'       ,   user_obj.salutation),
        "first_name"        : params.get('first_name'       ,   user_obj.first_name),
        "last_name"         : params.get('last_name'        ,   user_obj.last_name),
        "middle_name"       : params.get('middle_name'      ,   user_obj.middle_name),
        "is_private"        : params.get('is_private'       ,   user_obj.is_private),
        "birth_date"        : params.get('dob'              ,   user_obj.birth_date),
        "marrige_date"      : params.get('marrige_date'     ,   user_obj.marrige_date),
        "deceased_date"     : params.get('deceased_date'    ,   user_obj.deceased_date),
        "bio"               : params.get('bio'              ,   user_obj.bio),
    }

    user_args['initials']   = get_initials(str(user_args["first_name"] + " " + user_args["last_name"]))

    if Enumeration.objects.filter( enum_id=marital_status, enum_type='MARITAL_STATUS' ).exists():
        user_args['marital_status_id']  = marital_status
        
    if Enumeration.objects.filter( enum_id=gender, enum_type='GENDER' ).exists():
        user_args['gender_id']  = gender

    if ( update_profile == True ):
        party       = user_obj.party
        party_id    = party.party_id


    else:
        party_args   = {
            'party_id'          : party_id ,
            'party_type_id'     : 'PERSON',
            'description'       : f"Party created for PERSON with PartyID: {party_id}",
            'status_id'         : 'PARTY_ENABLED',
            'created_date'      : now(),
        }

        user_args['party_id']       = party_id
        user_args['is_active']      = False
        party = Party.objects.create(**party_args)


    user_args['updated_stamp']   = now()
    UserLogin.objects.filter(user_login_id=user_login_id).update(**user_args)
    # logger.debug ("party created with party_id:'%s'", party.party_id)


    if (email_id != None) and (email_id != "") and (checkEmail(email_id)):
        contact_args = { 'contact_type' : 'EMAIL_ADDRESS', 'value' : email_id , "party_id": party.party_id, 'purpose':"PRIMARY_EMAIL" , 'address' : None}
        res_contact  = create_contact_mech(update_available=update_profile,**contact_args)


    if (phone != None) and (phone != "") and checkMobile(phone):
        contact_args = { 'contact_type' : 'TELECOM_NUMBER', 'value' : phone , "party_id": party.party_id, 'purpose':"PRIMARY_PHONE" , 'address' : None}
        res_contact  = create_contact_mech(update_available=update_profile,**contact_args)

    if (whastapp_number != None) and (whastapp_number != "") and checkMobile(whastapp_number):
        contact_args = { 'contact_type' : 'TELECOM_NUMBER', 'value' : whastapp_number , "party_id": party.party_id, 'purpose':"WHATSAPP_NUMBER" , 'address' : None}
        res_contact  = create_contact_mech(update_available=update_profile,**contact_args)


    res = {
        "apiresponse": {
            "type": "OK",
            "severity": "INFO",
            "message": "Operation completed successfully.",
            "code": "0000"
        },
        "record": {
            "user_login_id":user_login_id,
            "party_id" : party.party_id,
        }
    }
    return res 



def create_contact_mech(update_available=False,**params):
    contact_mech_id     = params.get('contact_mech_id',None)
    contact_type        = params.get('contact_type',None)
    address             = params.get('address',None)
    value               = params.get('value',None)
    purpose             = params.get('purpose',None)
    party_id            = params.get('party_id',None)
    record              = {}

    if party_id == None:
        raise Exception('HANDLED: party_id is required.')

    if (value == None) and (address == None):
        raise Exception('HANDLED: value/address is required.')

    if contact_type == None:
        raise Exception('HANDLED: contact_type is required.')

    if purpose == None:
        raise Exception('HANDLED: purpose is required.')

    if (update_available == True):        
        pc_payload = {
            'party_id'                              : party_id,
            'thru_date__isnull'                     : True,
            'contact_mech__contact_mech_type_id'    : contact_type,
            'cm_purpose_type_id'                    : purpose,
        }

        if contact_mech_id != None:  pc_payload['contact_mech_id'] = contact_mech_id
        PartyContactMech.objects.filter(**pc_payload).select_related('contact_mech').update(thru_date=now(), updated_stamp = now())



    if (contact_type == 'EMAIL_ADDRESS'):
        cm_id = gen_id("CMEM_")    
        cm_obj      = ContactMech.objects.create(contact_mech_id=cm_id, contact_mech_type_id=contact_type, info_string=value )
        pcm_obj     = PartyContactMech.objects.create(party_id=party_id, contact_mech_id=cm_id, cm_purpose_type_id=purpose , verified='Y')
    
    elif contact_type == 'TELECOM_NUMBER':
        cm_id       = gen_id("CMMOB_")
        data        = parse_mobile(value)
        cm_obj      = ContactMech.objects.create(contact_mech_id=cm_id, contact_mech_type_id=contact_type)
        pcm_obj     = PartyContactMech.objects.create(party_id=party_id, contact_mech_id=cm_id, cm_purpose_type_id=purpose, verified='Y')
        TelecomNumber.objects.create( contact_mech_id = cm_id, country_code = data['country_code'] , contact_number = data['mobile'] )

    else:
        address = dict(address)
        cm_id       = gen_id("CMPA_")
        cm_obj      = ContactMech.objects.create(contact_mech_id=cm_id, contact_mech_type_id=contact_type)
        pcm_obj     = PartyContactMech.objects.create(party_id=party_id, cm_purpose_type_id=purpose, contact_mech_id=cm_id, verified='Y')
        pa_paload   = {
            'contact_mech_id'       :   cm_id, 
            'to_name'               :   address.get('to_name',              None), 
            'attn_name'             :   address.get('attn_name',            None), 
            'address1'              :   address.get('address1',             None), 
            'address2'              :   address.get('address2',             None),
            'house_number'          :   address.get('house_number',         None),
            'house_number_ext'      :   address.get('house_number_ext',     None),
            'directions'            :   address.get('directions',           None),
            'city'                  :   address.get('city',                 None),
            'postal_code'           :   address.get('postal_code',          None),
            'postal_code_ext'       :   address.get('postal_code_ext',      None),
            'city_geo'              :   address.get('city_geo',             None),
            'country_geo'           :   address.get('country_geo',          None),
            'state_province_geo'    :   address.get('state_province_geo',   None),
            'municipality_geo'      :   address.get('municipality_geo',     None),            
        }
        PostalAddress.objects.create(**pa_paload)

    record['contact_mech_id']                   = cm_id
    record['pcm_id']                            = pcm_obj.pcm_id
    return record



def create_content(content_type, party_id, content_name,description,mime_type_id, created_by_user_login, updated_by_user_login, object_info, party_content_type_id=None ,electronic_text=None, is_public='Y', locale_string=None,data_resource_name=None, service_name= None, content_prefix='CON_', dr_type='IMAGE_OBJECT' ,owner_content_id=None, decorator_content_id=None,status_id='CTNT_AVAILABLE'):
    content_id          = gen_id(initials=content_prefix)
    obj = { 'content_id': content_id }
    dr_payload          =  {
        'data_resource_type_id'     :   dr_type,
        'status_id'                 :   status_id,
        'data_resource_name'        :   data_resource_name ,
        'locale_string'             :   locale_string,
        'mime_type_id'              :   mime_type_id,
        'object_info'               :   object_info, 
        'is_public'                 :   is_public,
        'created_by_user_login_id'  :   created_by_user_login,
        'updated_by_user_login_id'  :   updated_by_user_login,
    }

    dr_obj = DataResource.objects.create(**dr_payload) 
    obj['data_resource_id'] = dr_obj.data_resource_id
    if (electronic_text != None):
        ElectronicText.objects.create(data_resource_id=dr_obj.data_resource_id, text_data=electronic_text)

    content_payload     = {
        'content_id'                :   content_id,
        'content_type_id'           :   content_type,     
        'owner_content_id'          :   owner_content_id,     
        'decorator_content_id'      :   decorator_content_id,   
        'data_resource_id'          :   dr_obj.data_resource_id,
        'status_id'                 :   status_id,
        'mime_type_id'              :   mime_type_id,
        'service_name'              :   service_name,
        'content_name'              :   content_name,
        'description'               :   description,
        'created_by_user_login_id'  :   created_by_user_login,
        'updated_by_user_login_id'  :   updated_by_user_login,
    }

    content_obj         = Content.objects.create(**content_payload)
    if (party_content_type_id != None):
        PartyContent.objects.filter( party_id=party_id, party_content_type_id=party_content_type_id ).update(updated_stamp=now(),thru_date=now())
        pc_obj  = PartyContent.objects.create( party_id=party_id, content_id=content_id, party_content_type_id=party_content_type_id )
        obj['party_content_id'] = pc_obj.party_content_id

    return obj 




'''
# from DJAccounts.models import UserLogin, UserLoginHistory, PartyContact, Content,Enumeration,Party, PartyRole, PartyRelatiionship,ContactMech, DataResource, ElectronicText, PartyContent
# from Modules.Utils import handle_exception,gen_id,save_file_to_filesystem, get_thumbnails_from_img, get_initials, logger, get_client_ip
# from json import dumps,loads
# from django.utils.timezone import now as current_timestamp


def modify_user(req,user_login_id, update_profile=False, **params):
    user_obj    = UserLogin.objects.get(user_login_id=user_login_id)
    email_id    = params.get('email',None)
    phone       = params.get('phone',None)
    party       = None

    enum_type       = "MARITAL_STATUS"
    gender          = str(params.get("gender","")).upper()
    marital_status  = str(params.get('marital_status')).upper()

    user_args = {
        # "is_superuser"      : params.get('is_superuser', False),
        "is_staff"          : params.get('is_staff', True),
        "is_active"         : params.get('is_active', True),
        "suffix"            : params.get('suffix', user_obj.suffix),
        "first_name"        : params.get('first_name', user_obj.first_name),
        "last_name"         : params.get('last_name', user_obj.last_name),
        "middle_name"       : params.get('middle_name', user_obj.middle_name),
        "is_private"        : params.get('is_private',user_obj.is_private),
        "birth_date"        : params.get('dob', user_obj.birth_date),
        "deceased_date"     : params.get('deceased_date',None),
        "marrige_date"      : params.get('marrige_date',user_obj.marrige_date),
        "bio"               : params.get('bio',user_obj.bio),
    }

    if Enumeration.objects.filter(enum_id=marital_status, enum_type=enum_type).exists():
        user_args['marital_status_id']  = marital_status

    if (gender != "")  :
        if ( gender == "F" ) : user_args['gender'] = "F" 
        if ( gender == "M" ) : user_args['gender'] = "M" 
        if ( gender == "O" ) : user_args['gender'] = "O" 


    user_args['initials']   = get_initials(str(user_args["first_name"] + " " + user_args["last_name"]))
    
    enum_id = "USER_REGISTER"
    
    
    if (update_profile == True): 
        party   = Party.objects.get(user_login=user_obj, party_type_id='PERSON')
        party.last_modified_date = current_timestamp()
        party.updated_stamp      = current_timestamp()
        if req.user.is_authenticated:
            party.last_modified_by_user_login = req.user
        
        party.save()
        enum_id = "USER_UPDATED"
        user_args['updated_stamp']   = current_timestamp()



    UserLogin.objects.filter(user_login_id=user_login_id).update(**user_args)
    logger.debug ("User created or updated with username:'%s'", user_obj.user_login_id)

    his_args = {
        "user_login_history_id" : gen_id("ULH_",length=20),
        "user_login_id" : user_obj,
        "history_type_id"  : enum_id,  
        "ip_addr"       : get_client_ip(req),
        "user_agent"    : req.META['HTTP_USER_AGENT'] ,       
    }
    usl_h = UserLoginHistory.objects.create(**his_args)
    logger.debug ("User history created with id:'%s'",  usl_h.user_login_history_id)

    if party == None:
        party_args = {
            "user_login"    : user_obj, 
            "party_id"      : str(gen_id("PR_")), 
            "party_type_id" : 'PERSON', 
            "description"   : "Party created for Person",
            "status_id"     : "PARTY_ENABLED"
        }
        if req.user.is_authenticated: party_args['created_by_user_login_id'] = req.user.user_login_id 
        party = Party.objects.create(**party_args)
        logger.debug ("party created with party_id:'%s'", party.party_id)



    if (email_id != None) and (email_id != ""):
        contact_args = { 'EMAIL_ADDRESS':email_id, "party_id": party.party_id, 'cm_purpose':"PRIMARY_EMAIL" }
        res_contact  = modify_contact(req,update_profile,**contact_args)

    if (phone != None) and (phone != ""):
        contact_args = { 'TELECOM_NUMBER': phone , "party_id": party.party_id, 'cm_purpose':"PRIMARY_PHONE" }
        res_contact  = modify_contact(req,update_profile,**contact_args)


    res = {
        "apiresponse": {
            "type": "OK",
            "severity": "INFO",
            "message": "Operation completed successfully.",
            "code": "0000"
        },
        "record": {
            "user_login_id":user_login_id,
            "party_id" : party.party_id,
        }
    }
    return res 



def add_reln_ship(party_from, party_to, role_from , role_to, reln_type,status=None):
    party_id_from = PartyRole.objects.create(
        party_role_id       = gen_id("PRL_"),
        party_id            = party_from ,
        role_type_id        = role_from
    )
    party_id_to = PartyRole.objects.create(
        party_role_id       = gen_id("PRL_"),
        party_id            = party_to ,
        role_type_id        = role_to
    )
    relnship_args = {
        "unique_id"               : gen_id('PRELN_' ),
        "party_role_to"           : party_id_to,
        "party_role_from"         : party_id_from,
        "relationship_type_id"    : reln_type,
        "relationship_name"       : f"{party_from}|{role_from}|{party_to}|{role_to}|{reln_type}"
    }
    if status != None:
        relnship_args['status_id'] = status
    party_reln = PartyRelatiionship.objects.create( **relnship_args )

    res = {
            "apiresponse": {
                "type": "OK",
                "severity": "INFO",
                "message": "Operation completed successfully.",
                "code": "0000"
            },
            "party_role_from"   :  party_id_from.party_role_id ,
            "party_role_to"     :  party_id_to.party_role_id ,
            "party_relnship"    :  party_reln.unique_id,
            "party_from"        : party_from,
            "party_to"          : party_to,
        }
    return res




def createTextContent(req,text,mime_type="text/plain",title="Text Title",status="CTNT_PUBLISHED",is_public='Y'):
    data_resource_id    = gen_id("DRS_",20)
    content_id          = gen_id("CNT_",20)
    drs_args = {
        "data_resource_id"      : data_resource_id,
        "data_resource_type_id" : "ELECTRONIC_TEXT",
        "status_id"             : status,
        "data_resource_name"    : title,
        "mime_type_id"          : mime_type,
        "is_public"             : is_public,
    }
    drs_obj     = DataResource.objects.create(**drs_args)

    ele_args            = {
        "data_resource_id" :  drs_obj.data_resource_id,
        "text_data" : text
    }
    elec_obj    = ElectronicText.objects.create(**ele_args)

    ctnt_args   = {
        "content_id"                : content_id,
        "content_type_id"           : "",
        "content_name"              : title,
        "mime_type_id"              : mime_type,
        "data_resource_id"          : drs_obj.data_resource_id,
        "status_id"                 : status,
        "created_by_user_login_id"  : req.user.user_login_id,
        "created_date"              : current_timestamp(),
    }

    ctnt_obj     = Content.objects.create(**ctnt_args)

    return {"content_id" : content_id, "data_resource_id":data_resource_id}
    


def createFileContent(req,file, status="CTNT_PUBLISHED",is_public='Y'):
    mime_type_id    = "text/richtext"
    dr_type_id      = "OTHER_OBJECT"
    obj_info        = {}
    content_type    = "DOCUMENT"
    dr_type_id      = "OTHER_OBJECT"
    
    obj_info['file_info'] = save_file_to_filesystem(file)
    mime_type_id    = obj_info['file_info']['mime_type']

    if (str(mime_type_id).lower().startswith('image/')): 
        content_type    = "IMAGE_FRAME"
        dr_type_id      = "IMAGE_OBJECT" 
        obj_info['image_info'] = get_thumbnails_from_img(obj_info['file_info']['filepath'],extn=obj_info['file_info']['file_ext'])

    if (str(mime_type_id).lower().startswith('video/')): 
        content_type    = "MEDIA_CONTENT"
        dr_type_id      = "VIDEO_OBJECT" 

     
    data_resource_id    = gen_id("DRS_",20)
    content_id          = gen_id("CNT_",20)
    
    drs_args = {
        "data_resource_id"      : data_resource_id,
        "data_resource_type_id" : dr_type_id,
        "status_id"             : status,
        "data_resource_name"    : file.name,
        "mime_type_id"          : file.content_type,
        "object_info"           : dumps(obj_info),
        "is_public"             : is_public,
    }
    
    drs_obj     = DataResource.objects.create(**drs_args)
    
    ctnt_args   = {
        "content_id"                : content_id,
        "content_type_id"           : content_type,
        "content_name"              : file.name,
        "mime_type_id"              : mime_type_id,
        "data_resource_id"          : drs_obj.data_resource_id,
        "status_id"                 : status,
        "description"               : "Content created with status: '{}' and filename:'{}'".format(status,file.name),
        "created_by_user_login_id"  : req.user.user_login_id,
        "created_date"              : current_timestamp(),
    }

    ctnt_obj     = Content.objects.create(**ctnt_args)

    return {"content_id" : content_id, "data_resource_id":data_resource_id}
    
    
"""
def uploadTo_content(file, party_id ,party_content_type,status='CTNT_PUBLISHED'):
    args = {}

    rs = search("\w*/(\w*)",file.content_type)
    if (rs == None):
        raise Exception("HANDLED: Invalid content type!")

    extn  = rs.groups()[0]
    if extn not in whitelist_extn.keys():
        raise Exception("HANDLED: Please upload a valid file. ({})".format(",".join(whitelist_extn)))


    dr_type_id      = "OTHER_OBJECT"
    info            = save_file_to_filesystem(file.read(), extn)
    info['size']    = file.size
    obj_info        = ""

    if str(file.content_type).startswith("video"): 
        dr_type_id = "VIDEO_OBJECT" 

    if str(file.content_type).startswith("audio"):
        dr_type_id = "AUDIO_OBJECT" 

    if str(file.content_type).startswith("image"):  
        dr_type_id = "IMAGE_OBJECT" 
        obj_info = dumps(
            {
                "file_info" : info,
                "thum_info" : get_thumbnails_from_img(info['filepath'],extn=extn),
            }
        )


    logger.debug("Content type found: %s",extn)
    data_resource_id    = gen_id("DRS_",20)
    content_id          = gen_id("CNT_",20)
    # info = save_file_to_filesystem(file.read(), extn)
    # info['size'] = file.size
    # args['content_id']      = gen_id("CNT",18)
    # args['content_name']    = file.name
    # args['mime_type']       = file.content_type
    # args['content_type']    = Enumeration.objects.get(enum_id=dr_type_id)
    # args['text_info']       = dumps(
    #     {
    #         "file_info" : info,
    #         "thum_info" : get_thumbnails_from_img(info['filepath'],extn=extn),
    #     }
    # )

    drs_args = {
        "data_resource_id"      : data_resource_id,
        "data_resource_type_id" : dr_type_id,
        "status_id"             : status,
        "data_resource_name"    : file.name,
        "mime_type_id"          : file.content_type,
        "object_info"           :  obj_info,
        "is_public"             : "Y"
    }
    
        
    drs_obj = DataResource.objects.create(**drs_args)

    # content = Content.objects.create(**args)
    # party_content = PartyContent.objects.create(
    #     party_content_id    = gen_id("PCNT_",16),
    #     party_id            = party_id,
    #     content             = content,
    #     party_content_type_id  = party_content_type,
    # )

    # return {"content_id": content.content_id, "party_content": party_content.party_content_id }

"""

def modify_contact(req,update_available=False,**params):
    record  = []
    cm_purpose  = params.get("cm_purpose")
    params.pop('cm_purpose')
    
    if 'party_id' in params.keys(): 
        party  = Party.objects.get(party_id=params.get('party_id'))
        params.pop('party_id')
    
    else:
        party = req.user.party

    for key in params.keys():
        contact_type_id = ""
        if str(key).upper() == "TELECOM_NUMBER": contact_type_id = "TELECOM_NUMBER"
        if str(key).upper() == "POSTAL_ADDRESS": contact_type_id = "POSTAL_ADDRESS"  
        if str(key).upper() == "EMAIL_ADDRESS": contact_type_id = "EMAIL_ADDRESS"  
        # if str(key).upper() == "MOBILE": contact_type_id = "EMAIL_ADDRESS"
        # if str(key).upper() == "ALTERNATE MOBILE": contact_type_id = "EMAIL_ADDRESS"  

        if (contact_type_id != ""):
            contact_mech_id = gen_id("CM_",length=20)
            con_args = {
                "contact_mech_id"     : contact_mech_id,
                "contact_mech_type_id"   : contact_type_id ,
                "info_string"    : params.get(key)    
            }
            
            if update_available == True:
                update_args = { 
                    'party_id' : party.party_id, 
                    'thruDate__isnull' : True, 
                    'contact__contact_mech_type_id': contact_type_id, 
                    "cm_purpose_id": cm_purpose
                }

                if ("contact_id" in params.keys()) : 
                    update_args['contact_id'] =  contact_mech_id                
                    
                PartyContact.objects.filter(**update_args).select_related('contact').update(thruDate=current_timestamp())

            contact_obj = ContactMech.objects.create(**con_args)
            party_con = PartyContact.objects.create(
                **{
                    "cm_purpose_id": cm_purpose,
                    "party_contact_id" : gen_id("PCM_",20),
                    "party_id" : party.party_id,
                    "contact_id" : contact_obj.contact_mech_id,
                } 
            )

            record.append({
                "contact_id": contact_mech_id,
                "party_contact": party_con.party_contact_id,
                "type":str(key).upper()
            })


    res = {
        "apiresponse": {
            "type": "OK",
            "severity": "INFO",
            "message": "Operation completed successfully.",
            "code": "0000"
        },
        "record" : record,
    }
    return res

'''
