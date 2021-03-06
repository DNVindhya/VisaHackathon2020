# Generated by Django 3.0.7 on 2020-07-02 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('karmapoints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pull_transaction_identifier', models.IntegerField(null=True)),
                ('push_transaction_identifier', models.IntegerField(null=True)),
                ('pull_action_code', models.CharField(max_length=2, null=True)),
                ('push_action_code', models.CharField(max_length=2, null=True)),
                ('pull_approval_code', models.CharField(max_length=8, null=True)),
                ('push_approval_code', models.CharField(max_length=8, null=True)),
                ('pull_response_code', models.CharField(max_length=2, null=True)),
                ('push_response_code', models.CharField(max_length=2, null=True)),
                ('pull_status', models.CharField(max_length=300, null=True)),
                ('push_status', models.CharField(max_length=300, null=True)),
                ('pull_transmission_date_time', models.CharField(max_length=25, null=True)),
                ('push_transmission_date_time', models.CharField(max_length=25, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('sender_card_id', models.CharField(max_length=19, null=True)),
                ('recipient_card_id', models.CharField(max_length=19, null=True)),
                ('txn_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='karmapoints.Orders')),
            ],
        ),
    ]
