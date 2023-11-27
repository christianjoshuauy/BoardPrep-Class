from django.db import models
from User.models import Teacher

# Create your models here.
class Class(models.Model):
    classId = models.AutoField(primary_key=True)
    className = models.CharField(max_length=255)
    classDescription = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.className