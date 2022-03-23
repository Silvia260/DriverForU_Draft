from django.db import models

class pro_skills(models.Model):
    pro_skills = models.CharField(max_length=100)

    def __str__(self):
        return self.pro_skills

    def save_pro_skills(self):
        self.save()

    @classmethod
    def delete_pro_skills(cls,pro_skills):
        cls.objects.filer(pro_skills=pro_skills).delete()

class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

# Create your models here.
class Nanny(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField(default=0)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    pro_skills = models.ManyToManyField(pro_skills)
    rate = models.IntegerField(default=400)
    phonenumber = models.IntegerField()
    featured = models.BooleanField(default=False)
    bio = models.CharField(blank=True, max_length=200)
