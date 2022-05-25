from datetime import datetime
from django.db import models
from django.urls import reverse




# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Body = models.TextField(max_length=10000, blank = True)
    Author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#foreign key allows one user to own many objects. The objects are indexed to him. You must
# have a on delete option for all many to one relationships.
    Date = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('Post_Detail', args=[str(self.id)])


    