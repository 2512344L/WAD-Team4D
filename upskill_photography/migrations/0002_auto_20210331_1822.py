# Generated by Django 2.2.17 on 2021-03-31 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upskill_photography', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
