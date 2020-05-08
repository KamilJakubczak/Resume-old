from django.contrib import admin
from .models import Course,Provider,Education,Company,Position,Skill,Info


# Register your models here.
admin.site.register(Course)
admin.site.register(Provider)
admin.site.register(Education)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Skill)
admin.site.register(Info)
