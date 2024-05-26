import datetime

from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.core.exceptions import ValidationError
from typing import cast
from django.utils.translation import gettext_lazy as _

timedelta_object = datetime.timedelta(microseconds=10)


def validate_number(value):
    if 0 < value < 999:
        return value
    else:
        raise ValidationError(
            _('%(value)s is not an valid number'),
            params={'value': value},
        )


def validate_set(value):
    if 0 < value < 50:
        return value
    else:
        raise ValidationError(
            _('%(value)s is not an valid number'),
            params={'value': value},
        )


class Action(models.Model):
    name = models.CharField(max_length=50, default='rope')
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class UserAction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    numbers = models.IntegerField(validators=[validate_number])
    numbers_sets = models.IntegerField(validators=[validate_set])
    weight = models.IntegerField(default=0, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, blank=True)
    time_duration = models.DurationField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.action}--{self.user}"


class UserProgram(models.Model):
    SATURDAY = "SA"
    Sunday = "SU"
    Monday = "MO"
    Tuesday = "TU"
    Wednesday = "WE"
    Thursday = "TH"
    Friday = "FR"

    DAYS = [
        (SATURDAY, "Saturday"),
        (Sunday, "Sunday"),
        (Monday, "Monday"),
        (Tuesday, "Tuesday"),
        (Wednesday, "Wednesday"),
        (Thursday, "Thursday"),
        (Friday, "Friday"),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    day = models.CharField(max_length=50, choices=DAYS, default=SATURDAY)
    numbers = models.IntegerField(validators=[validate_number], blank=True)
    numbers_sets = models.IntegerField(validators=[validate_set], blank=True)
    time_duration2 = models.DurationField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PROGRAM OF{self.user} FOR {self.day} ----"


class Master(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    field = models.CharField(max_length=50)

    def __str__(self):
        return f"Master in {self.field} name is : {self.user}"


