# Generated by Django 5.0.2 on 2024-02-15 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_milage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='milage',
            options={'ordering': ('-year',), 'verbose_name': 'пробег', 'verbose_name_plural': 'пробег'},
        ),
    ]
