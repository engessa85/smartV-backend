from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Company(models.Model):
    COUNTRY_CHOICES = [
        ("KUWAIT", "Kuwait"),
        ("UAE", "UAE"),
        ("QATAR", "Qatar"),
        ("SAUDI ARABIA", "Saudi Arabia"),
        ("OMAN", "Oman"),
        ("BAHRAIN", "Bahrain"),
        ("SOUTH AFRICA", "South Africa"),
        ("EGYPT", "Egypt"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    company_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    company_website = models.CharField(max_length=255, null=True, blank=True)
    company_email = models.CharField(max_length=255, null=True, blank=True)
    company_linkedin = models.CharField(max_length=255, null=True, blank=True)
    company_facebook = models.CharField(max_length=255, null=True, blank=True)
    company_twitter = models.CharField(max_length=255, null=True, blank=True)

    person_name = models.CharField(max_length=255, null=True, blank=True)
    person_linked = models.CharField(max_length=255, null=True, blank=True)
    person_email = models.CharField(max_length=255, null=True, blank=True)
    person_contact = models.CharField(max_length=20, null=True, blank=True)

    negotiate = models.BooleanField(default=False, null=True, blank=True)
    contract = models.BooleanField(default=False, null=True, blank=True)
    first_payment = models.BooleanField(default=False, null=True, blank=True)
    final_payment = models.BooleanField(default=False, null=True, blank=True)

    # Country-specific boolean fields
    kuwait = models.BooleanField(default=False, null=True, blank=True)
    uae = models.BooleanField(default=False, null=True, blank=True)
    qatar = models.BooleanField(default=False, null=True, blank=True)
    saudi_arabia = models.BooleanField(default=False, null=True, blank=True)
    oman = models.BooleanField(default=False, null=True, blank=True)
    bahrain = models.BooleanField(default=False, null=True, blank=True)
    south_africa = models.BooleanField(default=False, null=True, blank=True)
    egypt = models.BooleanField(default=False, null=True, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)  # Set when created
    updated_at = models.DateTimeField(auto_now=True)  # Updates on every save
    
    

    def __str__(self):
        return f"{self.company_name} - By:{self.user.username}"


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    follow = models.BooleanField(default=False)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return f"{self.user.username} - {self.company.company_name} - {self.date}"
    
