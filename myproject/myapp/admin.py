from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Patients)
admin.site.register(models.PatientProfile)
admin.site.register(models.Specialty)
admin.site.register(models.Doctors)
admin.site.register(models.PatientDoctor)
admin.site.register(models.Appointments)
admin.site.register(models.Diagnosis)
admin.site.register(models.PaymentStatus)
admin.site.register(models.Billing)

#url routing -> middleware -> view logic -> match url -> generate response -> middle ware -> send to client