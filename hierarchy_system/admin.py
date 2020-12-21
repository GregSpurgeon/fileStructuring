from django.contrib import admin
from hierarchy_system.models import Folder
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
# Register your models here.
admin.site.register(Folder, DraggableMPTTAdmin)