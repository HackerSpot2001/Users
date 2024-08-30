# Generated by Django 5.0.2 on 2024-04-08 15:58

import Helpers.Utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0025_alter_partyrelationship_relationship_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'Content'},
        ),
        migrations.AlterModelOptions(
            name='contentassoc',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'ContentAssoc'},
        ),
        migrations.AlterModelOptions(
            name='contentassoctype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'ContentAssocType'},
        ),
        migrations.AlterModelOptions(
            name='contentpurposetype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'ContentPurposeType'},
        ),
        migrations.AlterModelOptions(
            name='contenttype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'ContentType'},
        ),
        migrations.AlterModelOptions(
            name='dataresource',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'DataResource'},
        ),
        migrations.AlterModelOptions(
            name='dataresourcetype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'DataResourceType'},
        ),
        migrations.AlterModelOptions(
            name='electronictext',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'ElectronicText'},
        ),
        migrations.AlterModelOptions(
            name='geo',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'Geo'},
        ),
        migrations.AlterModelOptions(
            name='geoassoctype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'GeoAssocType'},
        ),
        migrations.AlterModelOptions(
            name='geotype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'GeoType'},
        ),
        migrations.AlterModelOptions(
            name='partycontactmech',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'PartyContactMech'},
        ),
        migrations.AlterModelOptions(
            name='partycontent',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'PartyContent'},
        ),
        migrations.AlterModelOptions(
            name='partycontenttype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'PartyContentType'},
        ),
        migrations.AlterModelOptions(
            name='partygroup',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'PartyGroup'},
        ),
        migrations.AlterModelOptions(
            name='partyrelationship',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'PartyRelationship'},
        ),
        migrations.AlterModelOptions(
            name='partyrelationshiptype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'PartyRelationshipType'},
        ),
        migrations.AlterModelOptions(
            name='partyrole',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'PartyRole'},
        ),
        migrations.AlterModelOptions(
            name='postaladdress',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'PostalAddress'},
        ),
        migrations.AlterModelOptions(
            name='roletype',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'RoleType'},
        ),
        migrations.AlterModelOptions(
            name='telecomnumber',
            options={'managed': True, 'ordering': ['-created_stamp'], 'verbose_name_plural': 'TelecomNumber'},
        ),
        migrations.CreateModel(
            name='PartyClassificationType',
            fields=[
                ('party_classification_type_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('has_table', models.CharField(blank=True, max_length=1, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_stamp', models.DateTimeField(auto_now_add=True)),
                ('created_stamp', models.DateTimeField(auto_now_add=True)),
                ('parent_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Users.partyclassificationtype')),
            ],
            options={
                'verbose_name_plural': 'PartyClassificationType',
                'db_table': 'party_classification_type',
                'ordering': ['-created_stamp'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PartyClassificationGroup',
            fields=[
                ('party_classification_group_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_stamp', models.DateTimeField(auto_now_add=True)),
                ('created_stamp', models.DateTimeField(auto_now_add=True)),
                ('parent_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Users.partyclassificationgroup')),
                ('party_classification_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Users.partyclassificationtype')),
            ],
            options={
                'verbose_name_plural': 'PartyClassificationGroup',
                'db_table': 'party_classification_group',
                'ordering': ['-created_stamp'],
                'managed': True,
                'unique_together': {('party_classification_group_id', 'party_classification_type')},
            },
        ),
        migrations.CreateModel(
            name='PartyClassification',
            fields=[
                ('party_classification_id', models.CharField(default=Helpers.Utils.gen_party_classification, max_length=40, primary_key=True, serialize=False)),
                ('from_date', models.DateTimeField(auto_now_add=True)),
                ('thru_date', models.DateTimeField(blank=True, null=True)),
                ('updated_stamp', models.DateTimeField(auto_now_add=True)),
                ('created_stamp', models.DateTimeField(auto_now_add=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.party')),
                ('party_classification_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Users.partyclassificationgroup')),
            ],
            options={
                'verbose_name_plural': 'PartyClassification',
                'db_table': 'party_classification',
                'ordering': ['-created_stamp'],
                'managed': True,
                'unique_together': {('party', 'party_classification_group', 'from_date')},
            },
        ),
    ]
