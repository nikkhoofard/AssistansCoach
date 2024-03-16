from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Custom User Manager


class UserManager(BaseUserManager):
    def create_user(self, email, name, is_admin=False,
                    password=None,
                    is_coach=False,
                    is_sportman=True):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            is_admin=is_admin,
            is_coach=is_coach,
            is_sportman=is_sportman,
        )
        user.set_password(password)
        user.save(using=self._db)
        Sportman.objects.create(user=user)
        if user.is_coach:
            Coach.objects.create(user=user)
        return user
    
    def create_superuser(self, email, name, is_admin=True, password=None):
        """
        Creates and saves a Superuser with the given email, name and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            is_admin=is_admin
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model.


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_coach = models.BooleanField(default=False)
    is_sportman = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'is_coach', 'is_sportman']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)



    def __str__(self):
        return f" username is {self.user.name}"


class Sportman(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coachs = models.ManyToManyField(Coach, related_name="sportmans")


