from django.db import models
from django.utils import timezone


class Account(models.Model):
    account_number = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    balance = models.DecimalField(max_digits=15, decimal_places=3)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.account_number


class TranferBalance(models.Model):
    choice = (
        ('Dr', 'Debit'),
        ('Cr', 'Credit'),
    )
    debit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Debit')
    credit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Credit')
    transection_type = models.CharField(max_length=6, choices=choice, default='Debit')
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    transection_time = models.DateTimeField(default=timezone.now)


class Topup(models.Model):
    topup_account_number = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    transection_time = models.DateTimeField(default=timezone.now)

"""
class Payment(models.Model):
    payments_to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='')
    payments_from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Debit')

    amount = models.DecimalField(max_digits=15, decimal_places=3)
    transection_time = models.DateTimeField(default=timezone.now)
"""

