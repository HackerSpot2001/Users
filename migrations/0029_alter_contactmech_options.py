# Generated by Django 4.2.15 on 2024-09-29 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0028_userloginfcm_device_type_userloginfcm_fcm_data_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactmech',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'ContactMech'},
        ),
    ]
