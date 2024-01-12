# Generated by Django 5.0.1 on 2024-01-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_car_kuzov_alter_car_manzil_alter_car_modeli_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='locations',
            field=models.CharField(choices=[('andijon', 'Andijon'), ('buxoro', 'Buxoro'), ("farg'ona", "Farg'ona"), ('jizzax', 'Jizzax'), ('xorazm', 'Xorazm'), ('namangan', 'Nmanagan'), ('navoiy', 'Navoiy'), ('qashqadaryo', 'Qashqadaryo'), ("qoraqalpog'iston respublikasi", "Qoraqalpog'iston Respublikasi"), ('samarqand', 'Samarqand'), ('sirdaryo', 'Sirdaryo'), ('surxondaryo', 'Surxondaryo'), ('toshkent', 'Toshkent')], default=True, max_length=50),
        ),
    ]