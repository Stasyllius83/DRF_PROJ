from rest_framework import serializers

from materials.models import Course
from users.models import Payments


class WrongPriceValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, price):
        products = Course.objects.all()
        for product in products:
            print(product.price)

        product_price = Course.objects.get(pk = Payments.objects)

        if price != product_price:
            raise serializers.ValidationError("Введите установленную стоимость")
