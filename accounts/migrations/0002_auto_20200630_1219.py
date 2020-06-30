# Generated by Django 3.0.7 on 2020-06-30 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='contact_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='curr_lat',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='curr_long',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='current_karma_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='annual_revenue',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='business_category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=16, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='merchant',
            name='zip_code',
            field=models.CharField(max_length=5, null=True, verbose_name='zip code'),
        ),
        migrations.CreateModel(
            name='Card_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=19)),
                ('expiry_data', models.CharField(max_length=7)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
