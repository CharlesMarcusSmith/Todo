from django.db import models

# Create your models here:
class Task (models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    

    #def str(self): is a python method which is called when we use print/str to convert object into a string. 
    #It is predefined , however can be customised.
    def __str__(self):
        return self.title       #Returns the title as a string
    