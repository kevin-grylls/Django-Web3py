from django.db import models

# Create your models here.


class Wallet(models.Model):
    """
    개인 계정과 지갑을 연동합니다.
    지갑의 비밀번호는 사용자의 아이디를 저장합니다. (유니크키 특성을 사용)
    """
    user_id = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=42, unique=True)
    private_key = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return self.address


class Transaction(models.Model):
    """
    Token Transaction 을 기록합니다.
    노드에서 일어난 거래 기록을 동기화하는 테이블입니다.
    """
    origin = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    destination = models.CharField(max_length=42)
    amount = models.FloatField(default=0.0)
    block_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return self.block_number


class Contract(models.Model):
    """
    발급된 컨트랙트 어드레스를 관리합니다.
    """
    ca = models.CharField(max_length=42, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at', ]

    def __str__(self):
        return self.erc20_token
