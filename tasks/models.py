from django.db import models

# Create your models here.
class Task(models.Model):
    status_choices =[('I','Incomplete'),('C','Completed')]
    tag_choices =[('S','Shopping'),('W','work'),('O','Other'),('A','All')]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=1,choices=status_choices,default='I')
    tag = models.CharField(max_length=1,choices=tag_choices,default='A')
    deadline = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name