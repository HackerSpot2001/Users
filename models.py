from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserLoginManager
from Helpers.Utils import gen_user_login_history


class Enumeration(models.Model):
    enum_id             = models.CharField(primary_key=True, max_length=20)
    enum_type           = models.ForeignKey('EnumerationType', models.DO_NOTHING, blank=True, null=True)
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
    parent_type     = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
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
    salutation          = models.CharField(max_length=10, choices=(("Mr.","Mr"),("Mrs","Mrs")) )
    first_name          = models.CharField(max_length=50, null=True)
    middle_name         = models.CharField(max_length=50, null=True)
    last_name           = models.CharField(null=True,max_length=50)
    bio                 = models.TextField(null=True)
    initials            = models.CharField(max_length=10)
    is_private          = models.BooleanField(default=False)
    birth_date          = models.DateField(null=True)
    deceased_date       = models.DateField(null=True)
    gender              = models.CharField(max_length=1,choices=(("M","Male"),("F","Female"),("O","Others")))
    party               = models.ForeignKey('Party', models.DO_NOTHING, blank=True, null=True)
    marital_status      = models.ForeignKey(Enumeration, null=True, on_delete=models.CASCADE)
    marrige_date        = models.DateField(null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD      = 'user_login_id'
    REQUIRED_FIELDS     = [ 'password']

    objects = UserLoginManager()

    def __str__(self):
        return self.user_login_id    

    class Meta:
        managed = True
        db_table = 'user_login'
        ordering = ["-created_stamp"]
        verbose_name_plural    = 'UserLogin'




class Party(models.Model):
    party_id        = models.CharField(primary_key=True, max_length=20)
    party_type      = models.ForeignKey('PartyType', models.DO_NOTHING, blank=True, null=True)
    external_id     = models.CharField(max_length=20, blank=True, null=True)
    description     = models.TextField(blank=True, null=True)
    status          = models.ForeignKey('StatusItem', models.DO_NOTHING, blank=True, null=True)
    created_date    = models.DateTimeField(blank=True, null=True)
    is_unread       = models.CharField(max_length=1, blank=True, null=True)
    updated_stamp   = models.DateTimeField(auto_now_add=True)
    created_stamp   = models.DateTimeField(auto_now_add=True)
    # data_source     = models.ForeignKey(DataSource, models.DO_NOTHING, blank=True, null=True)
    # preferred_currency_uom = models.ForeignKey('Uom', models.DO_NOTHING, blank=True, null=True)


    def __str__(self):
        return self.party_id    
    

    class Meta:
        managed = True
        db_table = 'party'
        verbose_name_plural = 'Party'



class PartyType(models.Model):
    party_type_id   = models.CharField(primary_key=True, max_length=20)
    parent_type     = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
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
    status_type     = models.ForeignKey('StatusType', models.DO_NOTHING, blank=True, null=True)
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
    parent_type     = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
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
    user_login          = models.ForeignKey(UserLogin, models.DO_NOTHING)  # The composite primary key (user_login_id, from_date) found, that is not supported. The first column is selected.
    visit_id            = models.CharField(max_length=20, blank=True, null=True)
    from_date           = models.DateTimeField(auto_now_add=True)
    thru_date           = models.DateTimeField(blank=True, null=True)
    password_used       = models.CharField(max_length=255, blank=True, null=True)
    successful_login    = models.CharField(max_length=1, blank=True, null=True)
    party               = models.ForeignKey(Party, models.DO_NOTHING, blank=True, null=True)
    updated_stamp       = models.DateTimeField(auto_now_add=True)
    created_stamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_login.user_login_id    


    class Meta:
        managed = True
        db_table = 'user_login_history'
        unique_together = (('user_login', 'from_date'),)
        verbose_name_plural = 'UserLoginHistory'

