# Generated by Django 2.1.5 on 2019-01-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20190120_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='ref_id',
        ),
        migrations.AddField(
            model_name='join',
            name='reference_id',
            field=models.CharField(default='abc', max_length=120),
        ),
    ]
