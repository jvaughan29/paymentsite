# Generated by Django 3.0.5 on 2020-10-19 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entryapp', '0003_auto_20201019_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='location_text',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='paymententry',
            old_name='location_text',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='paymententry',
            old_name='type_text',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='type_text',
            new_name='type',
        ),
    ]