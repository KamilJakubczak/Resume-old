from django.db import models

# Create your models here.
#EDUCATION
class Education(models.Model):
    school_name = models.CharField(max_length=100)
    course_name = models.CharField(max_length=100)
    spec = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    grade = models.DecimalField(decimal_places=1, max_digits=2)
    start_date = models.DateField()
    end_date = models.DateField()
    school_logo = models.ImageField(upload_to='media/cv/education/')
    order = models.IntegerField(unique=True, null=True)
    disabled = models.BooleanField(default=True)

    def __str__(self):
        return self.school_name + '-' + self.course_name

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    compoany_logo = models.ImageField(upload_to='media/cv/jobs/')

    def __str__(self):
        return self.company_name


class Position(models.Model):
    position_title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    order = models.IntegerField(unique=True, null=True)
    disabled = models.BooleanField(default=True)

    def __str__(self):
        return self.company.company_name \
                + '-' + self.position_title


class Provider(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    completion_date = models.DateField(blank=True, null=True)
    certificat_id = models.CharField(max_length=100, blank=True, null=True)
    certificat_img = models.ImageField(upload_to='media/cv/courses', \
                                       blank=True, \
                                       null=True)
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField(unique=True, null=True)
    disabled = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name + '-' + self.provider.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='media/cv/skills',blank=True,null=True)
    order = models.IntegerField(unique=True, null=True)
    disabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Info(models.Model):
    title = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='media/cv/info',blank=True,null=True)
    description = models.CharField(max_length=100)
    order = models.IntegerField(unique=True, null=True)
    disabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title
