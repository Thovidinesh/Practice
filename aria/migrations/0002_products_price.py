# Generated by Django 5.0.6 on 2024-06-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
