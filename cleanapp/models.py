from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField


class CityModel(models.Model):
    City_Name = models.CharField(max_length=20)

    def __str__(self):
        return self.City_Name



class Title(models.Model):
    Title_text = models.CharField(max_length=20)

    def __str__(self):
        return self.Title_text


class Question(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answare_type = models.BooleanField(default=True)
    answare = models.CharField(default=None, max_length=2000)
    answare_id = models.IntegerField()
    image = ProcessedImageField(upload_to='images/%Y/%m/%d/', default='uploads/No_image_3x4.svg.png', blank=True, null=True,format='JPEG',options={'quality': 60})

    def __str__(self):
        return self.question_text


class Reports(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    city = models.ForeignKey(CityModel, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question, default=False,related_name='questions')
    questions_answers = models.CharField(max_length=2000, null=True,)
    questions_images = models.CharField(max_length=2000, null=True)


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    city = models.ManyToManyField(CityModel)
    admin = models.BooleanField(default=False)

    def get_user_city(self):
        return self.city


class BillImge(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=200,default=None)
    image = ProcessedImageField(upload_to='bills/%Y/%m/%d/',blank=True, null=True,format='JPEG',options={'quality': 60})
    notes = models.CharField(max_length=2000,default=None)









