from django.db import models
from django.db.models import Q

# Create your models here.
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
    image = models.ImageField(upload_to='images/', default='./static/images/img_10_sq')

    def __str__(self):
        return self.first_name

    @classmethod
    def filter_nannies(cls,search_term,skill_search):
        nannies = cls.objects.filter(Q(location__location=search_term) | Q(pro_skills__pro_skills=skill_search))
        return nannies
