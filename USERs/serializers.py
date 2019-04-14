from django.contrib.auth.models import User
from rest_framework import serializers
from USERs.models import Account, Topup, TranferBalance#, Payment

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'name',
            'phone_number',
            'account_number',
            'balance',
        )


class TransferBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranferBalance
        fields = "__all__"


class TopUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topup
        fields = "__all__"