from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user_id',
            'password',
            'address',
            'private_key',
            'created_at',
        )
        model = Wallet
