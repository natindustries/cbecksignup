# Generated by Django 2.1.5 on 2019-01-20 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='abc', max_length=120),
        ),
    ]
