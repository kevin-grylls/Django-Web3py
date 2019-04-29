from rest_framework import serializers
from .models import Wallet, Transaction


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


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'contract_address',
            'origin',
            'destination',
            'amount',
            'gas_used',
            'block_number',
            'tx_hash',
            'created_at'
        )
        model = Transaction
