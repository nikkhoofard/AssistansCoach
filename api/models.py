from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
    name = models.CharField(max_length=50, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class UserAction(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    numbers = models.IntegerField(validators=[validate_number])
    numbers_sets = models.IntegerField(validators=[validate_set])
    time_duration = models.DurationField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.action}--{self.user}"

