from .models import Party, UserLogin, ContactMech, PartyContactMech, TelecomNumber, PostalAddress 
from .models import PartyContent, Content,DataResource,ElectronicText, Enumeration, PartyRelationship, PartyRole, PartyGroup, PartyClassification
from django.core.paginator import Paginator
from django.utils.timezone import now 
from Helpers.Utils import gen_id, parse_mobile,handle_exception, get_initials, checkEmail, checkMobile
from json import loads 

def get_users (**filters):
    res = {}
    try:
        search = {}
        classification          = filters.get("classification", None)
        rows                    = filters.get("rows", 10)
        page                    = int(filters.get("page", 1))
        select_rel              = ['party',]

        if (classification != None ):
            search['party__partyclassification__party_classification_group_id'] = str(classification).upper()
        
        users_objs              = UserLogin.objects.select_related(*select_rel).filter(**search).all()
        paginator               = Paginator(users_objs, rows)
        paginator.validate_number(page)
        users                   = paginator.get_page(page)
        res["users"] =  [
            {
                'birth_date' : user.birth_date.strftime('%Y-%m-%d'),
                'first_name' : user.first_name,
                'middle_name' : user.middle_name,
                'last_name' : user.last_name,
                'fullname' : user.getFullName(),
                'party_id' : user.party_id,
                'profilePic' : user.party.getProfilePic(),
                'created_stamp': int(user.created_stamp.timestamp()),
                'user_login_id': user.user_login_id,
            } for user in users
        ]
        res['metadata'] = {
            'total_count' : paginator.count,
            'total_pages' : paginator.num_pages,
            'current_page': page
        }
        
    except Exception as e:
        res = handle_exception(e)
        print(e)

    return res


def get_user_info(user_login_id):
    try:
        user = UserLogin.objects.select_related('party').get(user_login_id=user_login_id)
        party = user.party
        user_attachs        = {}
        business_attachs    = {}
        business_info       = {}
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

        preln_filter = {
            'party_relationship_type_id'    :   'OWNER' , 
            'party_role_from__party_id'     :   party.party_id , 
            'party_role_from__role_type_id' :   'ACCOUNT' , 
            'party_role_to__role_type_id'   :   'INTERNAL_ORGANIZATIO' ,
        }
        if (PartyRelationship.objects.filter(**preln_filter).select_related('party_role_from', 'party_role_to').exists()):
            prlen_obj   = PartyRelationship.objects.select_related('party_role_from', 'party_role_to').get(**preln_filter)
            party_group = prlen_obj.party_role_to.party
            prc_args["party_id"] = party_group.party_id
            for prc_obj in PartyContent.objects.filter(**prc_args).select_related("content","party_content_type").all():
                business_attachs[prc_obj.party_content_type.party_content_type_id] = {
                    "content_id"        : prc_obj.content.content_id,
                    "content_name"      : prc_obj.content.content_name,
                    "mime_type_id"      : prc_obj.content.mime_type_id,
                    "mime_type_id"      : prc_obj.content.mime_type_id,
                    "object_info"       : loads(prc_obj.content.data_resource.object_info)
                }

            business_info['party_group_id']         = party_group.party_id
            business_info['group_name']             = party_group.partygroup.group_name
            business_info['group_name_local']       = party_group.partygroup.group_name_local
            business_info['created_stamp']          = party_group.created_stamp.timestamp()
            business_info['business_attachs']       = business_attachs
            business_info['contact_mechs']          = {
                'TELECOM_NUMBER'    : party_group.getAllTelecomNumbers(),
                'EMAIL_ADDRESS'     : party_group.allEmails(),
            }
        
            
        user_attachs = {}
        prc_args["party_id"] = party.party_id
        for prc_obj in PartyContent.objects.filter(**prc_args).select_related("content","party_content_type").all():
            user_attachs[prc_obj.party_content_type.party_content_type_id] = {
                "content_id"        : prc_obj.content.content_id,
                "content_name"      : prc_obj.content.content_name,
                "mime_type_id"      : prc_obj.content.mime_type_id,
                "mime_type_id"      : prc_obj.content.mime_type_id,
                "object_info"       : loads(prc_obj.content.data_resource.object_info)
            }


        res = {
            "apiresponse": {
                "type": "OK",
                "severity": "INFO",
                "message": "Operation completed successfully.",
                "code": "0000"
            },
            'record' : {
                'business_info': business_info,
                'user_info'             :   {
                    'fullname'          : user.getFullName(),
                    'firstname'         : user.first_name,
                    'last_name'         : user.last_name,
                    'middle_name'       : user.middle_name,
                    'biography'         : user.bio,
                    'username'          : user.username,
                    'user_login_id'     : user.user_login_id,
                    'marital_status'    : user.marital_status_id,
                    'salutation'        : user.salutation_id,
                    'gender'            : user.gender_id,
                    # 'dob'               : user.birth_date.strftime('%d-%m-%Y'),
                    'dob'               : user.birth_date.strftime('%Y-%m-%d'),
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
                    'TELECOM_NUMBER'    : party.getAllTelecomNumbers() , 
                    'EMAIL_ADDRESS'     : party.allEmails(),
                },
            },
        }

    except Exception as e:
        res = handle_exception(e)

    return res




def modify_user(user_login_id, update_profile=False, **params):
    user_obj            = UserLogin.objects.select_related('party').get(user_login_id=user_login_id)
    party_id            = gen_id('PR_',15)
    email_id            = params.get('email',       None)
    phone               = params.get('phone',       None)
    whastapp_number     = params.get('whastapp',    None)
    party_group         = params.get('party_group', None)
    classification      = params.get('classification', None)
    utype               = params.get('utype', None)

    salutation          = str(params.get('salutation',  ''))
    gender              = str(params.get("gender","")).upper()
    marital_status      = str(params.get('marital_status','')).upper()

    user_args = {
        # "is_superuser"      : params.get('is_superuser'     , user_obj.is_superuser),
        # "is_staff"          : params.get('is_staff'         ,   user_obj.is_staff),
        # "is_active"         : params.get('is_active'        ,   user_obj.is_active),
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

    
    if Enumeration.objects.filter( enum_id=salutation, enum_type='SALUTATION' ).exists():
        user_args['salutation_id']  = salutation
        
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

    if (str(utype).upper() == 'EMP'):
        add_reln_ship(party_from=party_id, party_to='Company',reln_type='EMPLOYMENT', role_to='INTERNAL_ORGANIZATIO',role_from='EMPLOYEE', status='PARTYREL_CREATED')
        
    # if (str(classification).upper() != None):
    if (classification != None):
        classification = str(classification).upper()
        payload = {
            'party_classification_group_id'     : classification,
            'party_id'                          : party_id 
        }
        create_classification(**payload)
        # add_reln_ship(party_from=party_id, party_to='Company',reln_type='EMPLOYMENT', role_to='INTERNAL_ORGANIZATIO',role_from='EMPLOYEE', status='PARTYREL_CREATED')
        

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




def create_content(**params):
    content_type            = params.get('content_type'                     , None              )
    party_id                = params.get('party_id'                         , None              )
    content_name            = params.get('content_name'                     , None              )
    description             = params.get('description'                      , None              )
    mime_type_id            = params.get('mime_type_id'                     , None              )
    created_by_user_login   = params.get('created_by_user_login'            , None              )
    updated_by_user_login   = params.get('updated_by_user_login'            , None              )
    object_info             = params.get('object_info'                      , None              )
    party_content_type_id   = params.get('party_content_type_id'            , None              )
    electronic_text         = params.get('electronic_text'                  , None              )
    locale_string           = params.get('locale_string'                    , None              )
    data_resource_name      = params.get('data_resource_name'               , None              )
    service_name            = params.get('service_name'                     , None              )
    owner_content_id        = params.get('owner_content_id'                 , None              )
    decorator_content_id    = params.get('decorator_content_id'             , None              )
    content_prefix          = params.get('content_prefix'                   , 'CON_'            )
    dr_type                 = params.get('dr_type'                          , 'IMAGE_OBJECT'    )
    status_id               = params.get('status_id'                        , 'CTNT_AVAILABLE'  )
    is_public               = params.get('is_public'                        , 'Y'               )
    
    
    if ( updated_by_user_login    == None )     : raise Exception("HANDLED:updated_by_user_login is required.")
    if ( created_by_user_login    == None )     : raise Exception("HANDLED:created_by_user_login is required.")
    if ( content_type == None )                 : raise Exception("HANDLED:content_type is required.")
    if ( party_id    == None )                  : raise Exception("HANDLED:party_id is required.")
    if ( content_name    == None )              : raise Exception("HANDLED:content_name is required.")
    if ( description    == None )               : raise Exception("HANDLED:description is required.")
    if ( mime_type_id    == None )              : raise Exception("HANDLED:mime_type_id is required.")
    if ( object_info    == None )               : raise Exception("HANDLED:object_info is required.")


    content_id              = gen_id(initials=content_prefix)
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




def add_reln_ship(party_from, party_to, role_from , role_to, reln_type,status=None):
    (party_role_from, _ )   = PartyRole.objects.get_or_create( party_id = party_from, role_type_id = role_from )
    (party_role_to, _ )     = PartyRole.objects.get_or_create( party_id = party_to, role_type_id = role_to )
    relnship_args   = {
        "party_relationship_id"         : gen_id('PREL_' )  ,
        "party_role_from"               : party_role_from   ,
        "party_role_to"                 : party_role_to     ,
        "party_relationship_type_id"    : reln_type         ,
        "relationship_name"             : f"party_from:{party_from}, role_from:{role_from}, party_to:{party_to}, role_to:{role_to}, reln_type:{reln_type}"
    }

    if status != None: relnship_args['status_id'] = status

    party_reln = PartyRelationship.objects.create( **relnship_args )

    res = {
            "apiresponse": {
                "type": "OK",
                "severity": "INFO",
                "message": "Operation completed successfully.",
                "code": "0000"
            },
            "party_role_from"   :  party_role_from.party_role_id ,
            "party_role_to"     :  party_role_to.party_role_id ,
            "party_relnship"    :  party_reln.party_relationship_id,
            "party_from"        : party_from,
            "party_to"          : party_to,
        }
    return res




def create_party_group(**params):
    person_party_id     = params.get('person_party_id',None)
    company_email       = params.get('company_email', None)
    company_phone       = params.get('company_phone', None)
    person_role_id      = params.get('person_role_id','ACCOUNT')
    pg_role_id          = params.get('pg_role_id','INTERNAL_ORGANIZATIO')
    reln_type_id        = params.get('reln_type_id', 'OWNER')
    status              = params.get('status', 'PARTYREL_CREATED')
    
    if person_party_id == None:
        raise Exception ('HANDLED:person_party_id is required.')

    res = {'person_party_id' :  person_party_id, 'person_role_id' : person_role_id, 'party_group_role_id' : pg_role_id, 'reln_type_id' : reln_type_id }
    (pr_role_from, _ ) = PartyRole.objects.get_or_create(party_id=person_party_id, role_type_id=person_role_id )
    payload = {
        'party_role_from'               : pr_role_from ,
        'party_relationship_type_id'    : reln_type_id ,
        'thru_date__isnull'             : True,
    }

    if (PartyRelationship.objects.filter(**payload).exists()):
        preln_obj       = PartyRelationship.objects.get(**payload)
        party_role_to   = preln_obj.party_role_to
        party_group     = PartyGroup.objects.get( party=party_role_to.party )

        
    else:
        party_group_id = gen_id("PG_",20)
        party_args   = {
            'party_id'          : party_group_id ,
            'party_type_id'     : 'PARTY_GROUP',
            'description'       : f"Party created for PARTY_GROUP with PartyID: {party_group_id}",
            'status_id'         : 'PARTY_ENABLED',
            'created_date'      : now(),
        }

        Party.objects.create(**party_args)
        party_group = PartyGroup.objects.create(party_id=party_group_id )
        add_reln_ship(party_from=person_party_id, party_to=party_group_id,reln_type=reln_type_id, role_to=pg_role_id,role_from=person_role_id, status=status)

    if ((company_email != None) and (company_email != '')  and (checkEmail(company_email))):
        cm_payload = { 'contact_type' : 'EMAIL_ADDRESS', 'value' : company_email , "party_id": party_group.party_id, 'purpose':"PRIMARY_EMAIL" , 'address' : None }
        create_contact_mech(False,**cm_payload)

    if ((company_phone != None) and (company_phone != '')  and (checkMobile(company_phone))):
        cm_payload = { 'contact_type' : 'TELECOM_NUMBER', 'value' : company_phone , "party_id": party_group.party_id, 'purpose':"PRIMARY_PHONE" , 'address' : None }
        create_contact_mech(False,**cm_payload)


    party_group.group_name          = params.get('group_name'       , party_group.group_name)
    party_group.group_name_local    = params.get('group_name_local' , party_group.group_name_local)
    party_group.office_site_name    = params.get('office_site_name' , party_group.office_site_name)
    party_group.annual_revenue      = params.get('annual_revenue'   , party_group.annual_revenue)
    party_group.num_employees       = params.get('num_employees'    , party_group.num_employees)
    party_group.ticker_symbol       = params.get('ticker_symbol'    , party_group.ticker_symbol)
    party_group.comments            = params.get('comments'         , party_group.comments)
    party_group.save()
    res['party_group_id']           = party_group.party_id

    return res 



def create_classification(**params):
    party_classification_group_id   = params.get('party_classification_group_id',None)
    party_id                        = params.get('party_id',None)         
    if (party_classification_group_id== None ): raise Exception("HANDLED: party_classification_group_id is required to create classification")
    if (party_id== None ): raise Exception("HANDLED: party_id is required to create classification")
    payload = {
        'party_id': party_id,
        'party_classification_group_id':party_classification_group_id
    }
    pcf = PartyClassification.objects.create(**payload)
    print(pcf.party_classification_id)
    return pcf