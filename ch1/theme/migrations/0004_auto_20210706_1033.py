# Generated by Django 2.2.16 on 2021-07-06 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_hint_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='content',
        ),
        migrations.AddField(
            model_name='theme',
            name='currentCount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='hintCount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
