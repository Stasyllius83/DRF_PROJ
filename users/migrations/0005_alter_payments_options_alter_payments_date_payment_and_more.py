# Generated by Django 5.0.2 on 2024-02-16 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_payments_paid_course_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payments',
            options={'verbose_name': 'платеж', 'verbose_name_plural': 'платежы'},
        ),
        migrations.AlterField(
            model_name='payments',
            name='date_payment',
            field=models.DateField(verbose_name='Дата платежа'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='payment_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='сумма платежа'),
        ),
    ]
