from django.db import models

# Create your models here.


class Wallet(models.Model):
    user_id = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=42, unique=True)
    private_key = models.CharField(max_length=152, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return self.address


class Transaction(models.Model):
    origin = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    destination = models.CharField(max_length=40)
    amount = models.FloatField(default=0.0)
    block_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return self.block_number
