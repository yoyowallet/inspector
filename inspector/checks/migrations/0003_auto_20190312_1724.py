# Generated by Django 2.1.7 on 2019-03-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0002_auto_20190116_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmentstatus',
            name='last_end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='environmentstatus',
            name='last_start_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='environmentstatus',
            name='result',
            field=models.CharField(choices=[('SUCCESS', 'Success'), ('WARNING', 'Warning'), ('FAILED', 'Failed')], max_length=20, null=True),
        ),
    ]
