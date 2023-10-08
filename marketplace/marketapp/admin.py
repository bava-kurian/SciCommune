from django.contrib import admin
from. import models
# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.Collaborator)
admin.site.register(models.Collaboration)