# Generated by Django 2.2.6 on 2019-11-15 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libman', '0005_auto_20191115_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='isbn_no',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='issue',
            name='isbn',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='return',
            name='isbn_no',
            field=models.CharField(default=9999999999999, max_length=20),
            preserve_default=False,
        ),
    ]
