from django.db import models
from . import fields





class books(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    genre=models.CharField(max_length=20)
    rating=fields.IntegerRangeField(min_value=1, max_value=5)
    stock=fields.IntegerRangeField(min_value=1, max_value=10000)
    book_cover=models.CharField(max_length=1000,default='cover_not_available.jpg')
    date = models.DateTimeField(auto_now_add=True)
    
    
    


    def __str__(self):
        return(str(self.pk)+" "+self.name+" "+self.author)

##    def get_absolute_url(self):
##        return reverse('submitresume:submit-resume')
