# Generated by Django 2.1.4 on 2018-12-06 12:05

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0002_auto_20181206_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='password',
            field=encrypted_model_fields.fields.EncryptedCharField(),
        ),
    ]