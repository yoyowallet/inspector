# Generated by Django 2.1.7 on 2019-03-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='application',
            field=models.IntegerField(choices=[(0, 'Postgresql'), (1, 'Redshift'), (2, 'MySQL')]),
        ),
    ]