# Generated by Django 4.1.7 on 2023-05-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0004_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Review',
            new_name='review',
        ),
        migrations.RemoveField(
            model_name='review',
            name='email',
        ),
        migrations.AlterField(
            model_name='review',
            name='food',
            field=models.CharField(max_length=55),
        ),
    ]
