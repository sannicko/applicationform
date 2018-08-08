# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=50, null=True, verbose_name='First Name', blank=True)),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email', blank=True)),
                ('phoneNumber', models.CharField(max_length=17, unique=True, null=True, verbose_name='Phone Number', blank=True)),
                ('Martial_status', models.CharField(max_length=1, null=True, verbose_name='Martial Status', choices=[(b'M', b'Married'), (b'S', b'Single')])),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('home_address1', models.CharField(max_length=1000, null=True, verbose_name='Home Address1')),
                ('home_address2', models.CharField(max_length=1000, null=True, verbose_name='Home Address2')),
                ('city', models.CharField(max_length=100, null=True, verbose_name='City')),
                ('state', models.CharField(max_length=100, null=True, verbose_name='State')),
                ('form_date', models.DateField(max_length=100, null=True, verbose_name='Form Date', blank=True)),
                ('dateOFBirth', models.DateField(max_length=100, null=True, verbose_name='Date OF Birth', blank=True)),
                ('socialSecurityNumber', models.CharField(max_length=70, verbose_name='Martial Status', blank=True)),
                ('no_year_experience', models.IntegerField(max_length=20, null=True, verbose_name='Years Of Experience', blank=True)),
                ('no_of_dependents', models.IntegerField(max_length=20, null=True, verbose_name='Number Of Dependents', blank=True)),
                ('emergency_contact_firstName', models.CharField(max_length=500, null=True, verbose_name='Emergency Contact FirstName')),
                ('emergency_contact_lastName', models.CharField(max_length=500, null=True, verbose_name='Emergency Contact LastName')),
                ('emergency_contact_phoneNumber', models.CharField(max_length=17, null=True, verbose_name='Emergency Contact PhoneNumber', blank=True)),
                ('emergency_contact_relation', models.CharField(max_length=17, null=True, verbose_name='Emergency Contact Relation', blank=True)),
                ('ceiling_mechanic', models.BooleanField(default=False, verbose_name='Ceiling Mechanic')),
                ('framing_mechanic', models.BooleanField(default=False, verbose_name='Framing Mechanic')),
                ('drywall_hanger', models.BooleanField(default=False, verbose_name='DryWall Hanger')),
                ('drywall_finisher', models.BooleanField(default=False, verbose_name='DryWall Finisher')),
                ('general_larborer', models.BooleanField(default=False, verbose_name='General Larborer')),
                ('painter_tradesman', models.BooleanField(default=False, verbose_name='Painter Tradesman')),
                ('plaster_tradesman', models.BooleanField(default=False, verbose_name='Plaster Tradesman')),
                ('masonry_bricklayer', models.BooleanField(default=False, verbose_name='Masonry BrickLayer')),
                ('masonry_blocklayer', models.BooleanField(default=False, verbose_name='Masonry BlockLayer')),
                ('carpenter', models.BooleanField(default=False, verbose_name='Carpenter')),
                ('concrete_forming', models.BooleanField(default=False, verbose_name='Concrete Forming')),
                ('concrete_finisher', models.BooleanField(default=False, verbose_name='Concrete Finisher')),
                ('osha_manager', models.BooleanField(default=False, verbose_name='Osha Manager')),
                ('project_manager', models.BooleanField(default=False, verbose_name='Project Manager')),
                ('is_ladder_user', models.BooleanField(default=False)),
                ('is_wheelbrrow_user', models.BooleanField(default=False)),
                ('is_general_hand_tools', models.BooleanField(default=False)),
                ('is_walking_slits', models.BooleanField(default=False)),
                ('is_electric_screw_gun', models.BooleanField(default=False)),
                ('is_electric_chop_saw', models.BooleanField(default=False)),
                ('is_power_nail_gun', models.BooleanField(default=False)),
                ('is_wallboard_hoist', models.BooleanField(default=False)),
                ('is_scissor_lift', models.BooleanField(default=False)),
                ('is_boom_lift', models.BooleanField(default=False)),
                ('is_bucket_truck_lift', models.BooleanField(default=False)),
                ('is_new_skill', models.BooleanField(default=False)),
                ('is_osha10', models.BooleanField(default=False)),
                ('is_osha30', models.BooleanField(default=False)),
                ('is_osha_training_manager', models.BooleanField(default=False)),
                ('is_power_tool_certified', models.BooleanField(default=False)),
                ('is_hiltl', models.BooleanField(default=False)),
                ('is_ladder_user_certified', models.BooleanField(default=False)),
                ('is_scissor_lift_certified', models.BooleanField(default=False)),
                ('is_broom_lift_certified', models.BooleanField(default=False)),
                ('convicted_or_not', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('allowed_in_usa', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('work_eligible_usa', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('domicile_address', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('law_suite', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('compensation_claim', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('other_city', models.CharField(default=b'N', max_length=1, choices=[(b'y', b'Yes'), (b'N', b'No')])),
                ('agreement_signed_date', models.DateField(max_length=100, null=True, verbose_name='Agreement Signed Date', blank=True)),
                ('driver_license', models.ImageField(default=b'Upload_documents/blank.jpg', null=True, upload_to=b'Upload_documents/')),
                ('social_security_copy', models.ImageField(default=b'Upload_documents/blank.jpg', null=True, upload_to=b'Upload_documents/')),
                ('certification_copy', models.FileField(default=b'Upload_documents/blank.jpg', null=True, upload_to=b'Upload_documents/')),
                ('resume_copy', models.FileField(default=b'Upload_documents/blank.jpg', null=True, upload_to=b'Upload_documents/')),
                ('comments_area', models.TextField(null=True, verbose_name='Comments', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
