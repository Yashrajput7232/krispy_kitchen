# Generated by Django 4.1.7 on 2023-05-14 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0003_alter_reservations_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=50)),
                ('food', models.CharField(max_length=50)),
                ('Review', models.TextField()),
            ],
        ),
    ]
