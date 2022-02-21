from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):

    def create_user(self, username,password=None):

        if not username:
            raise ValueError('User must have a username')
        user = self.model(
            username = username,
        )

        user.is_staff = True
        user.is_active = True
        user.role = 3
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):

        user = self.create_user(
            username = username,
            # password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.role = 1
        user.is_active = True
        user.is_superadmin = True
        user.set_password(password)
        user.save(using=self._db)
        return user
        

class Account(AbstractBaseUser):

    USER_TYPE_CHOICES = (
      (1, 'admin'),
      (2, 'level adviser'),
      (3, 'student'),
  )
  
    LEVEL_TYPE_CHOICES = (
      ('100', '100'),
      ('200', '200'),
      ('300', '300'),
      ('400', '400'),
      ('500', '500'),
      ('ALUMNI', 'ALUMNI'),
  )

    username = models.CharField(max_length=50, unique=True)
    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=3)
    level = models.CharField(choices=LEVEL_TYPE_CHOICES,max_length=255, blank=True, null=True)
    
    login_counter = models.IntegerField(default=0, blank=True)
    
    #required
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_adviser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'username'

    objects = MyAccountManager()

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


