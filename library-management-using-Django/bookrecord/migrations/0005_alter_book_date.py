# Generated by Django 4.0.3 on 2022-03-31 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookrecord', '0004_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 31, 13, 9, 29, 667843)),
        ),
    ]
