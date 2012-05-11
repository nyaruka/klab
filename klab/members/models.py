from smartmin.models import SmartModel
from django.db import models

class Application(SmartModel):
    """
    The application model
    """

    PROFESSIONAL_STATUS = (
        ('STU', "Student"),
        ('ENT', "Entrepreneur"),
        ('EIT', "Employed in IT"),
        ('NIT', "Employed in non-IT"),
        ('UNE', "Not currently employed")
    )

    MEMBERSHIP_TYPES = (
        ('G', "Green - kLab Tenant"),
        ('B', "Blue - kLab Mentor")
    )

    FREQUENCY_TYPES = (
        ('D', "Daily"),
        ('W', "A few times a week"),
        ('M', "A few times a month")
    )

    first_name = models.CharField(max_length=64, help_text="Your first (given) name")
    last_name = models.CharField(max_length=64, help_text="Your last (family) name")
    phone = models.CharField(max_length=12, help_text="Your phone number (including country code) - eg: 250788123456")
    email = models.EmailField(max_length=75, help_text="Your email address")
    picture = models.ImageField(upload_to="members", help_text="A close-up photo of yourself")
    country = models.CharField(max_length=18, help_text="The country you live in - eg: Rwanda")
    city = models.CharField(max_length=18, help_text="The city you live in - eg: Kigali")
    neighborhood = models.CharField(max_length=26, help_text="The neighborhood you live in - eg: Nyamirambo")
    professional_status = models.CharField(max_length=3, choices=PROFESSIONAL_STATUS, help_text="Your professional background")
    applying_for = models.CharField(max_length=1, choices=MEMBERSHIP_TYPES, help_text="The type of membership you are applying for")
    frequency = models.CharField(max_length=1, choices=FREQUENCY_TYPES, help_text="How often you plan on visiting kLab")
    goals = models.TextField(max_length=1024, help_text="If you are applying as a tenant, please tell us what your ongoing projects are "
                             "and how you see kLab helping to accomplish your goals. If you are applying as a mentor, please tell us what you have "
                             "to offer the kLab community, and what your goals are as a mentor (1024 character limit).")
    education = models.TextField(max_length=1024, help_text="Your education, including any degrees or certifications earned (1024 character limit).")
    experience = models.TextField(max_length=1024, help_text="Briefly describe your experience, projects you have worked on, and companies you have worked for. "
                                  "Please include the URLs of any projects you worked on and how you contributed (1024 character limit).")

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)
