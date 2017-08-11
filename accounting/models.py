from django.db import models
from datetime import datetime
from .constants import *


class Record(models.Model):

    ACTION_CHOICES = (
        (Actions.BUY, 'BUY'),
        (Actions.SELL, 'SELL'),
    )
    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES,
        default=Actions.BUY,
    )
    # 买入或者卖出的单价
    unit_price = models.DecimalField(max_digits=10, decimal_places=3)
    # 份额
    quantity = models.IntegerField()
    # 手续费
    charge = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    created_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"

    def __str__(self):
        pass
    
