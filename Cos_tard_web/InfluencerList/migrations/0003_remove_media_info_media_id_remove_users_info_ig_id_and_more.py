# Generated by Django 4.2.3 on 2023-08-07 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InfluencerList', '0002_alter_media_fix_table_alter_media_info_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media_info',
            name='media_id',
        ),
        migrations.RemoveField(
            model_name='users_info',
            name='ig_id',
        ),
        migrations.DeleteModel(
            name='Media_fix',
        ),
        migrations.DeleteModel(
            name='Media_info',
        ),
        migrations.DeleteModel(
            name='Users_fix',
        ),
        migrations.DeleteModel(
            name='Users_info',
        ),
    ]
