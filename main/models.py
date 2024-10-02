from django.db import models

from django.contrib.auth.hashers import make_password

# Create your models here.

class students(models.Model):
     name = models.CharField(max_length=100 ,null=True,blank=True)
     age = models.IntegerField()
     email = models.EmailField(null=True,blank=True)
     session = models.CharField(max_length=50 ,null=True,blank=True)
     grade = models.CharField(max_length=10 ,null=True,blank=True)

     def _str_(self):
        return f"{self.name}"
 

class singup(models.Model):
     username = models.CharField(max_length=70, null=True, blank=True, unique=True)
     email = models.EmailField(unique=True)
     password = models.CharField(max_length=128)  # CharField for storing hashed passwords
    
    
     def save(self, *args, **kwargs):
        # Check if the password is not already hashed
        if not self.password.startswith('pbkdf2_'):  # To avoid rehashing an already hashed password
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


def __str__(self):
        return f"{self.username}"




class  ClassStudent(models.Model):
    class_name = models.CharField(max_length=70, null=True, blank=True)
    student_names = models.JSONField(default=list, help_text="Enter student names in JSON format")
    subject = models.CharField(max_length=70, null=True, blank=True)
    teacher = models.CharField(max_length=70, null=True, blank=True)
    start_time = models.TimeField()  
    end_time = models.TimeField()  

    def __str__(self):
        return f"{self.class_name}"

    def get_student_names_list(self):
        # Return the student names as a list (already in list format with JSONField)
        return self.student_names













