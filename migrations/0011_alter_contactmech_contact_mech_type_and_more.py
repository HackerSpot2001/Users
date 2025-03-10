# Generated by Django 4.2 on 2024-01-20 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_contactmech_contactmechpurposetype_contentassoctype_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmech',
            name='contact_mech_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.contactmechtype'),
        ),
        migrations.AlterField(
            model_name='contactmechtype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.contactmechtype'),
        ),
        migrations.AlterField(
            model_name='content',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.contenttype'),
        ),
        migrations.AlterField(
            model_name='content',
            name='created_by_user_login',
            field=models.ForeignKey(blank=True, db_column='created_by_user_login', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='content',
            name='data_resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.dataresource'),
        ),
        migrations.AlterField(
            model_name='content',
            name='decorator_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_decorator_content_set', to='Users.content'),
        ),
        migrations.AlterField(
            model_name='content',
            name='instance_of_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_instance_of_content_set', to='Users.content'),
        ),
        migrations.AlterField(
            model_name='content',
            name='owner_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.content'),
        ),
        migrations.AlterField(
            model_name='content',
            name='privilege_enum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.enumeration'),
        ),
        migrations.AlterField(
            model_name='content',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.statusitem'),
        ),
        migrations.AlterField(
            model_name='content',
            name='template_data_resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_template_data_resource_set', to='Users.dataresource'),
        ),
        migrations.AlterField(
            model_name='content',
            name='updated_by_user_login',
            field=models.ForeignKey(blank=True, db_column='updated_by_user_login', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_updated_by_user_login_login_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contentassoc',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.content'),
        ),
        migrations.AlterField(
            model_name='contentassoc',
            name='content_assoc_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.contentassoctype'),
        ),
        migrations.AlterField(
            model_name='contentassoc',
            name='content_id_to',
            field=models.ForeignKey(db_column='content_id_to', on_delete=django.db.models.deletion.CASCADE, related_name='contentassoc_content_id_to_set', to='Users.content'),
        ),
        migrations.AlterField(
            model_name='contentassoc',
            name='created_by_user_login',
            field=models.ForeignKey(blank=True, db_column='created_by_user_login', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contentassoc',
            name='updated_by_user_login',
            field=models.ForeignKey(blank=True, db_column='updated_by_user_login', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contentassoc_updated_by_user_login_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contenttype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.contenttype'),
        ),
        migrations.AlterField(
            model_name='dataresource',
            name='created_by_user_login',
            field=models.ForeignKey(blank=True, db_column='created_by_user_login', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dataresource',
            name='data_resource_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.dataresourcetype'),
        ),
        migrations.AlterField(
            model_name='dataresource',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.statusitem'),
        ),
        migrations.AlterField(
            model_name='dataresource',
            name='updated_by_user_login',
            field=models.ForeignKey(blank=True, db_column='updated_by_user_login', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dataresource_updated_by_user_login_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dataresourcetype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.dataresourcetype'),
        ),
        migrations.AlterField(
            model_name='electronictext',
            name='data_resource',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Users.dataresource'),
        ),
        migrations.AlterField(
            model_name='enumeration',
            name='enum_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.enumerationtype'),
        ),
        migrations.AlterField(
            model_name='enumerationtype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.enumerationtype'),
        ),
        migrations.AlterField(
            model_name='geo',
            name='geo_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.geotype'),
        ),
        migrations.AlterField(
            model_name='geoassoc',
            name='geo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.geo'),
        ),
        migrations.AlterField(
            model_name='geoassoc',
            name='geo_assoc_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.geoassoctype'),
        ),
        migrations.AlterField(
            model_name='geoassoc',
            name='geo_id_to',
            field=models.ForeignKey(db_column='geo_id_to', on_delete=django.db.models.deletion.CASCADE, related_name='geoassoc_geo_id_to_set', to='Users.geo'),
        ),
        migrations.AlterField(
            model_name='geotype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.geotype'),
        ),
        migrations.AlterField(
            model_name='party',
            name='party_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.partytype'),
        ),
        migrations.AlterField(
            model_name='party',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.statusitem'),
        ),
        migrations.AlterField(
            model_name='partycontactmech',
            name='contact_mech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.contactmech'),
        ),
        migrations.AlterField(
            model_name='partycontactmech',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.party'),
        ),
        migrations.AlterField(
            model_name='partycontactmechpurpose',
            name='contact_mech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.contactmech'),
        ),
        migrations.AlterField(
            model_name='partycontactmechpurpose',
            name='contact_mech_purpose_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.contactmechpurposetype'),
        ),
        migrations.AlterField(
            model_name='partycontactmechpurpose',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.party'),
        ),
        migrations.AlterField(
            model_name='partycontent',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.content'),
        ),
        migrations.AlterField(
            model_name='partycontent',
            name='party',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Users.party'),
        ),
        migrations.AlterField(
            model_name='partycontent',
            name='party_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.partycontenttype'),
        ),
        migrations.AlterField(
            model_name='partycontenttype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.partycontenttype'),
        ),
        migrations.AlterField(
            model_name='partygroup',
            name='party',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Users.party'),
        ),
        migrations.AlterField(
            model_name='partytype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.partytype'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='city_geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.geo'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='contact_mech',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Users.contactmech'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='country_geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postaladdress_country_geo_set', to='Users.geo'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='municipality_geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postaladdress_municipality_geo_set', to='Users.geo'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='postal_code_geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postaladdress_postal_code_geo_set', to='Users.geo'),
        ),
        migrations.AlterField(
            model_name='postaladdress',
            name='state_province_geo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postaladdress_state_province_geo_set', to='Users.geo'),
        ),
        migrations.AlterField(
            model_name='statusitem',
            name='status_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.statustype'),
        ),
        migrations.AlterField(
            model_name='statustype',
            name='parent_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.statustype'),
        ),
        migrations.AlterField(
            model_name='telecomnumber',
            name='contact_mech',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Users.contactmech'),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='party',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.party'),
        ),
        migrations.AlterField(
            model_name='userlogin',
            name='salutation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salutation', to='Users.enumeration'),
        ),
        migrations.AlterField(
            model_name='userloginhistory',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.party'),
        ),
        migrations.AlterField(
            model_name='userloginhistory',
            name='user_login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
