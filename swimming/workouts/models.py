from django.db import models
from django.core.validators import RegexValidator

class Workouts_gym(models.Model):
    title = models.CharField('Название тренировки', max_length=50)
    description = models.CharField('Описание тренировки', max_length=250)
    full_text = models.TextField('Упражнения и дозировка нагрузки')

    def __str__(self) -> str:
        return self.title
    

class Workouts_swimming(models.Model):
    title = models.CharField('Название тренировки', max_length=50)
    description = models.CharField('Описание тренировки', max_length=250)
    full_text = models.TextField('Упражнения и дозировка нагрузки')

    def __str__(self) -> str:
        return self.title

class Workouts_swimming_pro(models.Model):
    title = models.CharField('Название тренировки', max_length=50)
    description = models.CharField('Описание тренировки', max_length=250)
    full_text = models.TextField('Упражнения и дозировка нагрузки')

    def __str__(self) -> str:
        return self.title


class Registrations(models.Model):
    phone_regex = RegexValidator(regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$', message='Phone number must me entered in format : "+9965592812')
    name = models.CharField('Ваше имя',max_length=30)
    age = models.IntegerField('Ваш возраст')
    purpose = models.CharField('Желаемый результат от занятий', max_length=250)
    phone = models.CharField(validators=[phone_regex], max_length=17, blank= True)
    comment = models.CharField('Комментарий', max_length=250)

    def __str__(self) -> str:
        return self.name

