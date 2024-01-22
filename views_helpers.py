from .models import ContactMech, PartyContactMech, PartyContactMechPurpose, TelecomNumber, PostalAddress, PartyContent, Content,DataResource,ElectronicText
from django.utils.timezone import now 
from Helpers.Utils import gen_id, parse_mobile



def create_contact_mech(contact_type,party_id,purpose,value=None, address=None):
    PartyContactMech.objects.filter(party_id=party_id, thru_date = None, contact_mech__contact_mech_type_id=contact_type ).select_related('contact_mech').update(thru_date=now(), updated_stamp = now())
    PartyContactMechPurpose.objects.filter(party_id=party_id, thru_date = None, contact_mech_purpose_type_id=purpose ).update(thru_date=now(), updated_stamp = now())

    if (contact_type == 'EMAIL_ADDRESS'):
        cm_id = gen_id("CMEM_")    
        cm_obj      = ContactMech.objects.create(contact_mech_id=cm_id, contact_mech_type_id='EMAIL_ADDRESS', info_string=value )
        pcm_obj     = PartyContactMech.objects.create(party_id=party_id, contact_mech_id=cm_id, verified='Y')
    
    elif contact_type == 'TELECOM_NUMBER':
        cm_id       = gen_id("CMMOB_")
        data        = parse_mobile(value)
        cm_obj      = ContactMech.objects.create(contact_mech_id=cm_id, contact_mech_type_id='TELECOM_NUMBER')
        pcm_obj     = PartyContactMech.objects.create(party_id=party_id, contact_mech_id=cm_id, verified='Y')
        TelecomNumber.objects.create( contact_mech_id = cm_id, country_code = data['country_code'] , contact_number = data['mobile'] )

    else:
        address = dict(address)
        cm_id       = gen_id("CMPA_")
        cm_obj      = ContactMech.objects.create(contact_mech_id=cm_id, contact_mech_type_id='POSTAL_ADDRESS')
        pcm_obj     = PartyContactMech.objects.create(party_id=party_id, contact_mech_id=cm_id, verified='Y')
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

    pcmp_obj    = PartyContactMechPurpose.objects.create(party_id=party_id, contact_mech_id=cm_id, contact_mech_purpose_type_id=purpose)  
 



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