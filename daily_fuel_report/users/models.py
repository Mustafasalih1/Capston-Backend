from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Createing users model

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role= "Operator"):
        if not email:
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email), role=role)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password, role="Admin")
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (("Admin", "Admin"),("Supervisor", "Supervisor"),("Operator", "Operator"),)
        
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    def __str__(self):
        return self.email
    
