# Generated by Django 3.0.7 on 2020-06-25 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offers',
            old_name='karma_points',
            new_name='karma_points_required',
        ),
        migrations.AddField(
            model_name='offers',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='offer_end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='offers',
            name='offer_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='offers',
            name='offer_start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]