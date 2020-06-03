from django.contrib import admin
from .models import Roles, DatosUser, habilidades, DetaRoles, rates

# Register your models here.
class RoleModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_linl =["RoleName"]
    list_filter = ["RoleName"]
    class Meta:
        model = Roles


admin.site.register(Roles)

class DatosUserModel(admin.ModelAdmin):
    list_display= ["nombUser","apelUser"]
    
    class Meta:
        model = DatosUser

admin.site.register(DatosUser)

class HabilUserModel(admin.ModelAdmin):
    list_display=["nombHabil"]

    class Meta:
        model = habilidades
admin.site.register(habilidades)

class DetaRolesModel(admin.ModelAdmin):
    list_display=["estadoRol"]

    class Meta:
        model = DetaRoles

admin.site.register(DetaRoles)

class RatesModel(admin.ModelAdmin):
    list_display = ["idHabil"]

admin.site.register(rates)


