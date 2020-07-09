from django.db import models

# Create your models here.
class HomeSlide(models.Model) :
    slide_id = models.AutoField(primary_key=True)
    slide_heading = models.CharField(max_length=100)
    slide_desc = models.TextField()
    slide_img = models.ImageField(upload_to = "Evento/images")

    def __str__(self) :
        return self.slide_heading

class Feature(models.Model) :
    F_id = models.AutoField(primary_key = True)
    F_heading = models.CharField(max_length=100)
    F_desc = models.CharField(max_length=500)
    F_img = models.ImageField(upload_to = "Evento/images")

    def __str__(self) :
        return self.F_heading

class Gold_Plan(models.Model) :
    GP_id = models.AutoField(primary_key =True)
    GP_heading = models.CharField(max_length=20)
    GP_plan = models.CharField(max_length=100)

    def __str__(self) :
        return self.GP_heading

class Platinum_Plan(models.Model) :
    PP_id = models.AutoField(primary_key =True)
    PP_heading = models.CharField(max_length=20)
    PP_plan = models.CharField(max_length=100)

    def __str__(self) :
        return self.PP_heading

class Team(models.Model) :
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=100)
    tdesc = models.TextField()
    trole = models.CharField(max_length=50)
    timg = models.ImageField(upload_to="Evento/images")

    def __str__(self) :
        return self.tname

class EventsImage(models.Model) :
    EI_id = models.AutoField(primary_key=True)
    EI_heading = models.CharField(max_length=100)
    EI_loc = models.CharField(max_length=50)
    EI_category = models.CharField(max_length=100)
    EI_img = models.ImageField(upload_to="Evento/images")

    def __str__(self) :
        return self.EI_heading

class EventStat(models.Model) :
    ES_id = models.AutoField(primary_key=True)
    ES_heading = models.CharField(max_length=100)
    ES_count = models.IntegerField()
    ES_img = models.ImageField(upload_to="Evento/images")

    def __str__(self) :
        return self.ES_heading 

class Contact(models.Model) :
    C_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13,default="")
    msg = models.TextField()

    def __str__(self) :
        return self.fname + self.lname + ' : ' + self.email