from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserLoginManager
from Helpers.Utils import *


class Enumeration(models.Model):
    enum_id             = models.CharField(primary_key=True, max_length=20)
    enum_type           = models.ForeignKey('EnumerationType', models.CASCADE, blank=True, null=True)
    enum_code           = models.CharField(max_length=60, blank=True, null=True)
    sequence_id         = models.CharField(max_length=20, blank=True, null=True)
    description         = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.enum_id    

    class Meta:
        managed     = True
        db_table    = 'enumeration'
        ordering    = ["-created_stamp"]
        verbose_name_plural    = 'Enumeration'
        


class EnumerationType(models.Model):
    enum_type_id    = models.CharField(primary_key=True, max_length=20)
    parent_type     = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    has_table       = models.CharField(max_length=1, blank=True, null=True)
    description     = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.enum_type_id    
    
    class Meta:
        managed     = True
        db_table    = 'enumeration_type'
        ordering    = ["-created_stamp"]
        verbose_name_plural    = 'EnumerationType'



class UserLogin(AbstractUser):
    user_login_id       = models.CharField(primary_key=True,unique=True,max_length=20,editable=False)
    username            = models.CharField(max_length=50, unique=True, null=False, blank=False )
    password            = models.CharField(max_length=255, null=False,blank=False)
    first_name          = models.CharField(max_length=50, null=True)
    middle_name         = models.CharField(max_length=50, null=True)
    last_name           = models.CharField(null=True,max_length=50)
    bio                 = models.TextField(null=True)
    initials            = models.CharField(max_length=10)
    birth_date          = models.DateField(null=True)
    deceased_date       = models.DateField(null=True)
    is_private          = models.BooleanField(default=False)
    salutation          = models.ForeignKey(Enumeration, null=True, on_delete=models.CASCADE,related_name='salutation')
    gender              = models.ForeignKey(Enumeration, null=True, on_delete=models.CASCADE, related_name='gender')
    marital_status      = models.ForeignKey(Enumeration, null=True, on_delete=models.CASCADE, related_name='marital_status')
    party               = models.OneToOneField('Party', models.CASCADE, blank=True, null=True)
    marrige_date        = models.DateField(null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD      = 'user_login_id'
    REQUIRED_FIELDS     = [ 'password']

    objects = UserLoginManager()

    def __str__(self):
        return self.user_login_id    
    
    def get_full_name(self):
        return ' '.join([self.first_name, self.middle_name,self.last_name])

    class Meta:
        managed = True
        db_table = 'user_login'
        ordering = ["-created_stamp"]
        verbose_name_plural    = 'UserLogin'



class Party(models.Model):
    party_id        = models.CharField(primary_key=True, max_length=20)
    party_type      = models.ForeignKey('PartyType', models.CASCADE, blank=True, null=True)
    external_id     = models.CharField(max_length=20, blank=True, null=True)
    description     = models.TextField(blank=True, null=True)
    status          = models.ForeignKey('StatusItem', models.CASCADE, blank=True, null=True)
    created_date    = models.DateTimeField(blank=True, null=True)
    is_unread       = models.CharField(max_length=1, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)
    # data_source     = models.ForeignKey(DataSource, models.CASCADE, blank=True, null=True)
    # preferred_currency_uom = models.ForeignKey('Uom', models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.party_id    
    

    class Meta:
        managed = True
        db_table = 'party'
        verbose_name_plural = 'Party'



class PartyType(models.Model):
    party_type_id   = models.CharField(primary_key=True, max_length=20)
    parent_type     = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    has_table       = models.CharField(max_length=1, blank=True, null=True)
    description     = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.party_type_id    
    

    class Meta:
        managed = True
        db_table = 'party_type'
        verbose_name_plural = 'PartyType'



class StatusItem(models.Model):
    status_id       = models.CharField(primary_key=True, max_length=20)
    status_type     = models.ForeignKey('StatusType', models.CASCADE, blank=True, null=True)
    status_code     = models.CharField(max_length=60, blank=True, null=True)
    sequence_id     = models.CharField(max_length=20, blank=True, null=True)
    description     = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.status_id    
    

    class Meta:
        managed = True
        db_table = 'status_item'
        verbose_name_plural = 'StatusItem'



class StatusType(models.Model):
    status_type_id  = models.CharField(primary_key=True, max_length=20)
    parent_type     = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    has_table       = models.CharField(max_length=1, blank=True, null=True)
    description     = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.status_type_id    
    

    class Meta:
        managed = True
        db_table = 'status_type'
        verbose_name_plural = 'StatusType'



class UserLoginHistory(models.Model):
    ulh_id              = models.CharField(max_length=30, primary_key=True, unique=True, default=gen_user_login_history)
    user_login          = models.ForeignKey(UserLogin, models.CASCADE)  # The composite primary key (user_login_id, from_date) found, that is not supported. The first column is selected.
    visit_id            = models.CharField(max_length=20, blank=True, null=True)
    from_date           = models.DateTimeField(auto_now_add=True)
    thru_date           = models.DateTimeField(blank=True, null=True)
    password_used       = models.CharField(max_length=255, blank=True, null=True)
    successful_login    = models.CharField(max_length=1, blank=True, null=True)
    party               = models.ForeignKey(Party, models.CASCADE, blank=True, null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_login.user_login_id    


    class Meta:
        managed = True
        db_table = 'user_login_history'
        unique_together = (('user_login', 'from_date'),)
        verbose_name_plural = 'UserLoginHistory'



class ContactMechType(models.Model):
    contact_mech_type_id    = models.CharField(primary_key=True, max_length=20)
    parent_type             = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    has_table               = models.CharField(max_length=1, blank=True, null=True)
    description             = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'contact_mech_type'
        verbose_name_plural = 'ContactMechType'



class ContactMechPurposeType(models.Model):
    contact_mech_purpose_type_id    = models.CharField(primary_key=True, max_length=20)
    description                     = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp                   = models.DateTimeField(auto_now_add=True)
    created_stamp                   = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed     = True
        db_table    = 'contact_mech_purpose_type'
        verbose_name_plural = 'ContactMechPurposeType'



class ContactMech(models.Model):
    contact_mech_id     = models.CharField(primary_key=True, max_length=20)
    contact_mech_type   = models.ForeignKey('ContactMechType', models.CASCADE, blank=True, null=True)
    info_string         = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)


    class Meta:
        managed     = True
        db_table    = 'contact_mech'
        verbose_name_plural = 'ContactMech'



class PartyContactMech(models.Model):
    pcm_id          = models.CharField(max_length=30, primary_key=True, unique=True, default=generate_pcm)
    party           = models.ForeignKey('Party', models.CASCADE)  # The composite primary key (party_id, contact_mech_id, from_date) found, that is not supported. The first column is selected.
    contact_mech    = models.ForeignKey(ContactMech, models.CASCADE)
    from_date       = models.DateTimeField(auto_now_add=True)
    thru_date       = models.DateTimeField(blank=True, null=True)
    extension       = models.CharField(max_length=255, blank=True, null=True)
    verified        = models.CharField(max_length=1, blank=True, null=True)
    comments        = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)
    # role_type       = models.ForeignKey('RoleType', models.CASCADE, blank=True, null=True)


    class Meta:
        managed     = True
        db_table    = 'party_contact_mech'
        unique_together = (('party', 'contact_mech', 'from_date'),)
        verbose_name_plural = 'PartyContactMech'



class PartyContactMechPurpose(models.Model):
    pcm_purpose_id              = models.CharField(max_length=30, primary_key=True, unique=True, default=generate_pcm_porpuse)
    party                       = models.ForeignKey(Party, models.CASCADE)  # The composite primary key (party_id, contact_mech_id, contact_mech_purpose_type_id, from_date) found, that is not supported. The first column is selected.
    contact_mech                = models.ForeignKey(ContactMech, models.CASCADE)
    contact_mech_purpose_type   = models.ForeignKey(ContactMechPurposeType, models.CASCADE)
    from_date                   = models.DateTimeField(auto_now_add=True)
    thru_date                   = models.DateTimeField(blank=True, null=True)
    updated_stamp               = models.DateTimeField(auto_now_add=True)
    created_stamp               = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'party_contact_mech_purpose'
        unique_together = (('party', 'contact_mech', 'contact_mech_purpose_type', 'from_date'),)
        verbose_name_plural = 'PartyContactMechPurpose'



class PartyContent(models.Model):
    party_content_id    = models.CharField(max_length=30, primary_key=True, unique=True, default=gen_party_content)
    party               = models.OneToOneField(Party, models.CASCADE)  # The composite primary key (party_id, content_id, party_content_type_id, from_date) found, that is not supported. The first column is selected.
    content             = models.ForeignKey('Content', models.CASCADE)
    party_content_type  = models.ForeignKey('PartyContentType', models.CASCADE)
    from_date           = models.DateTimeField(auto_now_add=True)
    thru_date           = models.DateTimeField(blank=True, null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'party_content'
        unique_together = (('party', 'content', 'party_content_type', 'from_date'),)
        verbose_name_plural = 'PartyContent'



class PartyContentType(models.Model):
    party_content_type_id   = models.CharField(primary_key=True, max_length=20)
    parent_type             = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    description             = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'party_content_type'
        verbose_name_plural = 'PartyContentType'



class PartyGroup(models.Model):
    party                   = models.OneToOneField(Party, models.CASCADE, primary_key=True)
    group_name              = models.CharField(max_length=100, blank=True, null=True)
    group_name_local        = models.CharField(max_length=100, blank=True, null=True)
    office_site_name        = models.CharField(max_length=100, blank=True, null=True)
    annual_revenue          = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    num_employees           = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    ticker_symbol           = models.CharField(max_length=10, blank=True, null=True)
    comments                = models.CharField(max_length=255, blank=True, null=True)
    logo_image_url          = models.CharField(max_length=2000, blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)


    class Meta:
        managed = True
        db_table = 'party_group'
        verbose_name_plural = 'PartyGroup'



class ContentAssocType(models.Model):
    content_assoc_type_id   = models.CharField(primary_key=True, max_length=20)
    description             = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)


    class Meta:
        managed     = True
        db_table    = 'content_assoc_type'
        verbose_name_plural = 'ContentAssocType'



class ContentPurposeType(models.Model):
    content_purpose_type_id = models.CharField(primary_key=True, max_length=20)
    description             = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)


    class Meta:
        managed     = True
        db_table    = 'content_purpose_type'
        verbose_name_plural = 'ContentPurposeType'



class ContentType(models.Model):
    content_type_id     = models.CharField(primary_key=True, max_length=20)
    parent_type         = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    has_table           = models.CharField(max_length=1, blank=True, null=True)
    description         = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed     = True
        db_table    = 'content_type'
        verbose_name_plural = 'ContentType'



class PostalAddress(models.Model):
    contact_mech        = models.OneToOneField(ContactMech, models.CASCADE, primary_key=True)
    to_name             = models.CharField(max_length=100, blank=True, null=True)
    attn_name           = models.CharField(max_length=100, blank=True, null=True)
    address1            = models.CharField(max_length=255, blank=True, null=True)
    address2            = models.CharField(max_length=255, blank=True, null=True)
    house_number        = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    house_number_ext    = models.CharField(max_length=60, blank=True, null=True)
    directions          = models.CharField(max_length=255, blank=True, null=True)
    city                = models.CharField(max_length=100, blank=True, null=True)
    postal_code         = models.CharField(max_length=60, blank=True, null=True)
    postal_code_ext     = models.CharField(max_length=60, blank=True, null=True)
    city_geo            = models.ForeignKey('Geo', models.CASCADE, blank=True, null=True)
    country_geo         = models.ForeignKey('Geo', models.CASCADE, related_name='postaladdress_country_geo_set', blank=True, null=True)
    state_province_geo  = models.ForeignKey('Geo', models.CASCADE, related_name='postaladdress_state_province_geo_set', blank=True, null=True)
    country_geo         = models.ForeignKey('Geo', models.CASCADE, related_name='postaladdress_country_geo_set', blank=True, null=True)
    municipality_geo    = models.ForeignKey('Geo', models.CASCADE, related_name='postaladdress_municipality_geo_set', blank=True, null=True)
    postal_code_geo     = models.ForeignKey('Geo', models.CASCADE, related_name='postaladdress_postal_code_geo_set', blank=True, null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)
    # geo_point           = models.ForeignKey(GeoPoint, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'postal_address'
        verbose_name_plural = 'PostalAddress'



class Content(models.Model):
    content_id              = models.CharField(primary_key=True, max_length=20)
    content_type            = models.ForeignKey('ContentType', models.CASCADE, blank=True, null=True)
    owner_content           = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    decorator_content       = models.ForeignKey('self', models.CASCADE, related_name='content_decorator_content_set', blank=True, null=True)
    instance_of_content     = models.ForeignKey('self', models.CASCADE, related_name='content_instance_of_content_set', blank=True, null=True)
    data_resource           = models.ForeignKey('DataResource', models.CASCADE, blank=True, null=True)
    template_data_resource  = models.ForeignKey('DataResource', models.CASCADE, related_name='content_template_data_resource_set', blank=True, null=True)
    status                  = models.ForeignKey('StatusItem', models.CASCADE, blank=True, null=True)
    privilege_enum          = models.ForeignKey('Enumeration', models.CASCADE, blank=True, null=True)
    service_name            = models.CharField(max_length=255, blank=True, null=True)
    content_name            = models.CharField(max_length=255, blank=True, null=True)
    description             = models.CharField(max_length=255, blank=True, null=True)
    locale_string           = models.CharField(max_length=10, blank=True, null=True)
    mime_type_id            = models.CharField(max_length=255, blank=True, null=True)
    child_leaf_count        = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    child_branch_count      = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    created_by_user_login   = models.ForeignKey('UserLogin', models.CASCADE, db_column='created_by_user_login', blank=True, null=True)
    updated_by_user_login   = models.ForeignKey('UserLogin', models.CASCADE, db_column='updated_by_user_login', related_name='content_updated_by_user_login_login_set', blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)
    # custom_method           = models.ForeignKey('CustomMethod', models.CASCADE, blank=True, null=True)
    # data_source             = models.ForeignKey('DataSource', models.CASCADE, blank=True, null=True)
    # character_set           = models.ForeignKey(CharacterSet, models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'content'
        verbose_name_plural = 'Content'



class ContentAssoc(models.Model):
    content_assoc_id        = models.CharField(primary_key=True, max_length=30,default=gen_content_assoc)
    content                 = models.ForeignKey(Content, models.CASCADE)  # The composite primary key (content_id, content_id_to, content_assoc_type_id, from_date) found, that is not supported. The first column is selected.
    content_id_to           = models.ForeignKey(Content, models.CASCADE, db_column='content_id_to', related_name='contentassoc_content_id_to_set')
    content_assoc_type      = models.ForeignKey('ContentAssocType', models.CASCADE)
    from_date               = models.DateTimeField(auto_now_add=True)
    thru_date               = models.DateTimeField(blank=True, null=True)
    sequence_num            = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    map_key                 = models.CharField(max_length=100, blank=True, null=True)
    upper_coordinate        = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    left_coordinate         = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    created_by_user_login   = models.ForeignKey('UserLogin', models.CASCADE, db_column='created_by_user_login', blank=True, null=True)
    updated_by_user_login   = models.ForeignKey('UserLogin', models.CASCADE, db_column='updated_by_user_login', related_name='contentassoc_updated_by_user_login_set', blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)
    # data_source             = models.ForeignKey('DataSource', models.CASCADE, blank=True, null=True)
    # content_assoc_predicate = models.ForeignKey('ContentAssocPredicate', models.CASCADE, blank=True, null=True)



    class Meta:
        managed = True
        db_table = 'content_assoc'
        unique_together = (('content', 'content_id_to', 'content_assoc_type', 'from_date'),)
        verbose_name_plural = 'ContentAssoc'



class TelecomNumber(models.Model):
    contact_mech            = models.OneToOneField(ContactMech, models.CASCADE, primary_key=True)
    country_code            = models.CharField(max_length=10, blank=True, null=True)
    area_code               = models.CharField(max_length=10, blank=True, null=True)
    contact_number          = models.CharField(max_length=60, blank=True, null=True)
    ask_for_name            = models.CharField(max_length=100, blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'telecom_number'
        verbose_name_plural = 'TelecomNumber'




class ElectronicText(models.Model):
    data_resource   = models.OneToOneField('DataResource', models.CASCADE, primary_key=True)
    text_data       = models.TextField(blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'electronic_text'
        verbose_name_plural = 'ElectronicText'



class DataResource(models.Model):
    data_resource_id        = models.CharField(primary_key=True, max_length=20,default=gen_data_resource)
    data_resource_type      = models.ForeignKey('DataResourceType', models.CASCADE, blank=True, null=True)
    status                  = models.ForeignKey('StatusItem', models.CASCADE, blank=True, null=True)
    data_resource_name      = models.CharField(max_length=255, blank=True, null=True)
    locale_string           = models.CharField(max_length=10, blank=True, null=True)
    mime_type_id            = models.CharField(max_length=255, blank=True, null=True)
    object_info             = models.CharField(max_length=255, blank=True, null=True)
    related_detail_id       = models.CharField(max_length=20, blank=True, null=True)
    is_public               = models.CharField(max_length=1, blank=True, null=True)
    created_by_user_login   = models.ForeignKey('UserLogin', models.CASCADE, db_column='created_by_user_login', blank=True, null=True)
    updated_by_user_login   = models.ForeignKey('UserLogin', models.CASCADE, db_column='updated_by_user_login', related_name='dataresource_updated_by_user_login_set', blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)
    # data_source             = models.ForeignKey('DataSource', models.CASCADE, blank=True, null=True)
    # survey                  = models.ForeignKey('Survey', models.CASCADE, blank=True, null=True)
    # survey_response         = models.ForeignKey('SurveyResponse', models.CASCADE, blank=True, null=True)
    # character_set           = models.ForeignKey(CharacterSet, models.CASCADE, blank=True, null=True)
    # data_category           = models.ForeignKey(DataCategory, models.CASCADE, blank=True, null=True)
    # data_template_type      = models.ForeignKey('DataTemplateType', models.CASCADE, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'data_resource'
        verbose_name_plural = 'DataResource'


class DataResourceType(models.Model):
    data_resource_type_id   = models.CharField(primary_key=True, max_length=20)
    parent_type             = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    has_table               = models.CharField(max_length=1, blank=True, null=True)
    description             = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp           = models.DateTimeField(auto_now_add=True)
    created_stamp           = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'data_resource_type'
        verbose_name_plural = 'DataResourceType'




class Geo(models.Model):
    geo_id          = models.CharField(primary_key=True, max_length=20)
    geo_type        = models.ForeignKey('GeoType', models.CASCADE, blank=True, null=True)
    geo_name        = models.CharField(max_length=100, blank=True, null=True)
    geo_code        = models.CharField(max_length=60, blank=True, null=True)
    geo_sec_code    = models.CharField(max_length=60, blank=True, null=True)
    abbreviation    = models.CharField(max_length=60, blank=True, null=True)
    well_known_text = models.TextField(blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'geo'
        verbose_name_plural = 'Geo'


class GeoAssoc(models.Model):
    geo_assoc_id    = models.CharField(primary_key=True, max_length=20,default=gen_geo_assoc)
    geo             = models.ForeignKey(Geo, models.CASCADE)  # The composite primary key (geo_id, geo_id_to) found, that is not supported. The first column is selected.
    geo_id_to       = models.ForeignKey(Geo, models.CASCADE, db_column='geo_id_to', related_name='geoassoc_geo_id_to_set')
    geo_assoc_type  = models.ForeignKey('GeoAssocType', models.CASCADE, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'geo_assoc'
        unique_together = (('geo', 'geo_id_to'),)
        verbose_name_plural = 'GeoAssoc'


class GeoAssocType(models.Model):
    geo_assoc_type_id   = models.CharField(primary_key=True, max_length=20)
    description         = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'geo_assoc_type'
        verbose_name_plural = 'GeoAssocType'



class GeoType(models.Model):
    geo_type_id     = models.CharField(primary_key=True, max_length=20)
    parent_type     = models.ForeignKey('self', models.CASCADE, blank=True, null=True)
    has_table       = models.CharField(max_length=1, blank=True, null=True)
    description     = models.CharField(max_length=255, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'geo_type'
        verbose_name_plural = 'GeoType'

