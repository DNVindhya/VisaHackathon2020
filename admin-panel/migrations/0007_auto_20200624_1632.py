# Generated by Django 3.0.7 on 2020-06-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin-panel', '0006_auto_20200622_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='card_details',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
    ]