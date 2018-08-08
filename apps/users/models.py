from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.db.models import signals
from django.conf import settings
from django.core.files.storage import FileSystemStorage

file_storage = FileSystemStorage(location=settings.FILE_STORAGE)


class ApplicationForm(models.Model):
    Martial_status = (
        ('M', 'Married'),
        ('S', 'Single'),
    )
    BOOL_CHOICES = (('Y', 'Yes'), ('N', 'No'))
    Gender_choises = (('M', 'Male'), ('F', 'Female'))

    first_name = models.CharField(verbose_name=_("First Name"),
        max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email"), unique=False)
    phoneNumber = models.CharField(verbose_name=_("Phone Number"),max_length=17, unique=True)
    gender = models.CharField(verbose_name=_("Gender"), max_length=30, choices=Gender_choises)
    Martial_status = models.CharField(verbose_name=_("Martial Status"),
        max_length=1, choices=Martial_status)

    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be treated as ' 'active. '
                                                                           'Unselect this instead of deleting accounts.'))

    home_address1 = models.CharField(verbose_name=_("Home Address1"),max_length=1000)
    home_address2 = models.CharField(verbose_name=_("Home Address2"),max_length=1000)
    city =  models.CharField(verbose_name=_("City"),max_length=100)
    state =  models.CharField(verbose_name=_("State"), max_length=100, blank=True)
    postCode = models.IntegerField(verbose_name=("Post code / Zip code"), max_length=5)
    #form_date = models.DateField(verbose_name=_("Form Date"),max_length=100, blank=True)
    dateOFBirth = models.DateField(verbose_name=_("Date OF Birth"), max_length=100)
    socialSecurityNumber = models.CharField(verbose_name=_("Martial Status"),max_length=70)

    no_year_experience = models.IntegerField(verbose_name=_("Years Of Experience"),max_length=20, blank=True,null=True)
    no_of_dependents = models.IntegerField(verbose_name=_("Number Of Dependents"),max_length=20, blank=True,null=True)
    emergency_contact_firstName = models.CharField(verbose_name=_("Emergency Contact FirstName"),max_length=500)
    emergency_contact_lastName = models.CharField(verbose_name=_("Emergency Contact LastName"),max_length=500)
    emergency_contact_phoneNumber = models.CharField(verbose_name=_("Emergency Contact PhoneNumber"),
        max_length=17)
    emergency_contact_relation  = models.CharField(verbose_name=_("Emergency Contact Relation"),
        max_length=17)

    ceiling_mechanic  = models.BooleanField(verbose_name=_("Ceiling Mechanic"),blank=True)
    framing_mechanic = models.BooleanField(verbose_name=_("Framing Mechanic"))
    drywall_hanger = models.BooleanField(verbose_name=_("DryWall Hanger"))
    drywall_finisher = models.BooleanField(verbose_name=_("DryWall Finisher"))
    general_larborer = models.BooleanField(verbose_name=_("General Larborer"))
    painter_tradesman = models.BooleanField(verbose_name=_("Painter Tradesman"))
    plaster_tradesman =  models.BooleanField(verbose_name=_("Plaster Tradesman"))

    masonry_bricklayer = models.BooleanField(verbose_name=_("Masonry BrickLayer"))
    masonry_blocklayer = models.BooleanField(verbose_name=_("Masonry BlockLayer"))
    carpenter = models.BooleanField(verbose_name=_("Carpenter"),default=False)
    concrete_forming = models.BooleanField(verbose_name=_("Concrete Forming"))
    concrete_finisher = models.BooleanField(verbose_name=_("Concrete Finisher"))
    osha_manager = models.BooleanField(verbose_name=_("Osha Manager"))
    project_manager = models.BooleanField(verbose_name=_("Project Manager"))

    #experience
    is_ladder_user = models.BooleanField(default=False)
    is_wheelbrrow_user = models.BooleanField(default=False)
    is_general_hand_tools = models.BooleanField(default=False)
    is_walking_slits = models.BooleanField(default=False)
    is_electric_screw_gun = models.BooleanField(default=False)
    is_electric_chop_saw = models.BooleanField(default=False)
    is_power_nail_gun =  models.BooleanField(default=False)
    is_wallboard_hoist = models.BooleanField(default=False)
    is_scissor_lift = models.BooleanField(default=False)
    is_boom_lift = models.BooleanField(default=False)
    is_bucket_truck_lift = models.BooleanField(default=False)
    is_new_skill = models.BooleanField(default=False)

    is_osha10 = models.BooleanField(default=False)
    is_osha30 = models.BooleanField(default=False)
    is_osha_training_manager = models.BooleanField(default=False)
    is_power_tool_certified = models.BooleanField(default=False)
    is_hiltl = models.BooleanField(default=False)
    is_ladder_user_certified = models.BooleanField(default=False)
    is_scissor_lift_certified = models.BooleanField(default=False)
    is_broom_lift_certified = models.BooleanField(default=False)

    convicted_or_not = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='')
    allowed_in_usa = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='')
    work_eligible_usa = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='')
    domicile_address = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='')
    law_suite = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='')
    compensation_claim = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='')
    other_city = models.CharField(max_length=1, choices=BOOL_CHOICES,blank=False,default='')

    agreement_signed_date = models.DateField(verbose_name=_("Agreement Signed Date"), auto_created=True, auto_now=True)

    driver_license = models.ImageField(upload_to='Upload_documents/', null=True)
    signature = models.ImageField(upload_to='Upload_documents/',null=True)
    social_security_copy = models.ImageField(upload_to='Upload_documents/',null=True)
    certification_copy = models.FileField(upload_to='Upload_documents/',null=True)
    resume_copy = models.FileField(upload_to='Upload_documents/',null=True)
    comments_area = models.TextField(verbose_name=_("Comments"), null=True, blank=True)

    def get_full_name(self):
        name = '%s %s' % self.first_name, self.last_name
        return name

    def get_short_name(self):
        return '%s' % (self.first_name)

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
