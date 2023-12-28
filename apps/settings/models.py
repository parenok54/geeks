from django.db import models

# Create your models here.
class Geeks(models.Model):
    logo = models.ImageField(
        upload_to="logo_image/",
        verbose_name="Логотип"
    )
    title1 = models.CharField(
        max_length=255,
        verbose_name="Название курса"
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self) -> str:
        return self.title1
    
    class Meta:
        verbose_name="Основные параметры"
        verbose_name_plural="Основные параметры"

class About(models.Model):
    image = models.ImageField(
        upload_to="about_image/",
        verbose_name="Фото"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="О нас"
        verbose_name_plural="О нас"

class Why(models.Model):
    title1 = models.CharField(
        max_length=255,
        verbose_name="Вопрос"
    )

    def __str__(self):
        return self.title1
    
    class Meta:
        verbose_name="Вопрос"
        verbose_name_plural="Вопросы"    

class Benefits(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название преимущества"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Преимущества"
        verbose_name_plural="Преимуществы"
    
class Count(models.Model):
    student_count = models.CharField(
        max_length=255,
        verbose_name="Колличество студентов"
    )
    teacher_count = models.CharField(
        max_length=255,
        verbose_name="Колличество учителей"
    )
    mentors_count = models.CharField(
        max_length=255,
        verbose_name="Колличество менторов"
    )
    branches_count = models.CharField(
        max_length=255,
        verbose_name="Колличество филиалов"
    )

    def __str__(self):
        return self.student_count
    
    class Meta:
        verbose_name="Цифры в курсе"
        verbose_name_plural="Цифры в курсах"

class Works(models.Model):
    image = models.ImageField(
        upload_to="reviews_image/",
        verbose_name="Фото"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Работа"
        verbose_name_plural="Работы"