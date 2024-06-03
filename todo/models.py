from django.db import models
from django.utils import timezone

# Create your models here.
CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(verbose_name="タスク",max_length=100, null=False,)
    memo = models.TextField(null=True,)
    priority = models.CharField(
        max_length=50,
        choices = CHOICE,
        null = True
    )
    duedate = models.DateField(verbose_name="期日", null=False, default=timezone.now)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

