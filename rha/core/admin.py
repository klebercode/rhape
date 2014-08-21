# coding: utf-8
from django.contrib import admin

from models import (Enterprise, Contact, Partner,
                    Step, Gallery, Course, Objective,
                    Public, Team, Cost, Graduation,
                    Institute, Subscribe)
from forms import (CourseModelForm, ObjectiveModelForm, PublicModelForm,
                   ContactModelForm)


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'phone3', 'email')
    search_fields = ['name', 'description', 'address', 'cep',
                     'district', 'city', 'state',
                     'phone1', 'phone2', 'phone3', 'email']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['content']
    search_fields = ['content']
    form = ContactModelForm


class CourseAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
    form = CourseModelForm


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
    form = ObjectiveModelForm


class PublicAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
    form = PublicModelForm


class SubscribeAdmin(admin.ModelAdmin):
    list_filter = ['module', 'state', 'city', 'institute__name',
                   'graduation__name', 'special']
    list_display = ['subscribe_date', 'name', 'module',
                    'email', 'mobile', 'phone', 'state',
                    'city']
    search_fields = ['subscribe_date', 'module', 'name', 'cpf',
                     'email', 'mobile', 'phone', 'cep', 'address',
                     'number', 'complement', 'district', 'city',
                     'state', 'graduation__name', 'year_conclusion',
                     'institute__name', 'special', 'which']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'description', 'image']
    search_fields = ['name', 'link', 'description', 'image']


class InstituteAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_per_page = 30


admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Partner)
admin.site.register(Step)
admin.site.register(Gallery)
admin.site.register(Course, CourseAdmin)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(Public, PublicAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Cost)
admin.site.register(Graduation)
admin.site.register(Institute, InstituteAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
