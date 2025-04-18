# Generated by Django 4.2 on 2024-01-16 18:07

import Helpers.Utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_delete_userloginhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoginHistory',
            fields=[
                ('ulh_id', models.CharField(default=Helpers.Utils.gen_user_login_history, max_length=30, primary_key=True, serialize=False, unique=True)),
                ('visit_id', models.CharField(blank=True, max_length=20, null=True)),
                ('from_date', models.DateTimeField(auto_now_add=True)),
                ('thru_date', models.DateTimeField(blank=True, null=True)),
                ('password_used', models.CharField(blank=True, max_length=255, null=True)),
                ('successful_login', models.CharField(blank=True, max_length=1, null=True)),
                ('updated_stamp', models.DateTimeField(auto_now_add=True)),
                ('created_stamp', models.DateTimeField(auto_now_add=True)),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Users.party')),
                ('user_login', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserLoginHistory',
                'db_table': 'user_login_history',
                'managed': True,
                'unique_together': {('user_login', 'from_date')},
            },
        ),
    ]
