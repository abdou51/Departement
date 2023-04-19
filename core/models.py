from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError




class Degree(models.Model):
    L2 = 'l2'
    L3 = 'l3'
    M1 = 'm1'
    M2 = 'm2'

    DEGREE_CHOICES = [
        (L2, 'Licence 2'),
        (L3, 'Licence 3'),
        (M1, 'Master 1'),
        (M2, 'Master 2'),
    ]

    name = models.CharField(
        max_length=255,
        choices=DEGREE_CHOICES,
        default=L2,
        unique=True
    )

    def __str__(self):
        return self.get_name_display()

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
    def validate_unique_degrees(value):
        if value.count() != value.distinct().count():
            raise ValidationError('Degrees must be unique')


        




    

    
class Semester(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name



    
class Speciality(models.Model):
    name = models.CharField(max_length=255)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.degree} - {self.name}"
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    Semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    Specialitys = models.ManyToManyField(
        Speciality,
        blank=True
    )
    def __str__(self):
        return self.name

    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')
    bio = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='images', blank=True, null=True , default='images/defaultprofile.png')
    courses = models.ManyToManyField(
        Course,
        blank=True
    )

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]

    def set_password(self, password):
        super().set_password(password)

    def save(self, *args, **kwargs):
        password = self.password
        if password and self.pk:
            orig = User.objects.get(pk=self.pk)
            if password != orig.password:
                self.set_password(password)
        elif password:
            self.set_password(password)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name or self.email
    
    
class DocumentType(models.Model):
    Cours = 'Cours'
    Tp = 'Tp'
    Td = 'Td'
    Extra = 'Extra'

    DEGREE_CHOICES = [
        (Cours, 'Cours'),
        (Tp, 'Tp'),
        (Td, 'Td'),
        (Extra, 'Extra'),
    ]

    name = models.CharField(
        max_length=255,
        choices=DEGREE_CHOICES,
        default=Cours,
        unique=True
    )

    def __str__(self):
        return self.name
    
class Document(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    documenttype = models.ForeignKey(DocumentType, on_delete=models.CASCADE, default='')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    
    def __str__(self):
        specialities = ", ".join([str(s) for s in self.course.Specialitys.all()])
        return f"{self.documenttype} - {self.course} - {self.name} - {self.user.name} - {specialities}"
    
class PlanningExam(models.Model):
    document = models.ImageField(upload_to='images')
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    Speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Speciality',)

    def __str__(self):
        return f"{self.degree} - {self.Speciality.name}"
    
class Planning(models.Model):
    document = models.ImageField(upload_to='images')
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    Speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Speciality',)

    def __str__(self):
        return f"{self.degree} - {self.Speciality.name}"