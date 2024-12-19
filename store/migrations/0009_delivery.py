# Generated by Django 5.0.6 on 2024-12-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
