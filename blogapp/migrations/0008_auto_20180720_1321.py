# Generated by Django 2.0.7 on 2018-07-20 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_auto_20180720_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtype',
            name='type_name',
            field=models.CharField(max_length=15),
        ),
    ]