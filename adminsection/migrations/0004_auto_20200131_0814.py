# Generated by Django 2.2 on 2020-01-31 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsection', '0003_auto_20200131_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='Ouantity',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='BillingNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
