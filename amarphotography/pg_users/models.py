from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class PG_users(AbstractUser):
    first_name=models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "pg_user"

class pg_login(models.Model):
    login_username=models.CharField(max_length=30)
    user_password=models.CharField(max_length=30)

    def __str__(self):
        return self.login_username

    class Meta:
        verbose_name_plural = "pg_login"

class pg_roles(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "role"

class pg_permission(models.Model):
    per_name=models.CharField(max_length=30)
    per_module=models.CharField(max_length=30)
    per_role_id=models.ForeignKey(pg_roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.per_name

    class Meta:
        verbose_name_plural = "permission"
