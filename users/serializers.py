from rest_framework import serializers

from users.validators import WrongPriceValidator
from .models import Payments, User


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
        # validators = [WrongPriceValidator(field='payment_amount')]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
