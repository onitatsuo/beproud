# Generated by Django 2.1.5 on 2019-01-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='fruit_ID',
        ),
        migrations.AlterField(
            model_name='master',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
