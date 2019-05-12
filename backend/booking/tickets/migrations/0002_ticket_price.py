# Generated by Django 2.1.2 on 2019-05-12 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, help_text='Price of the ticket', max_digits=10),
            preserve_default=False,
        ),
    ]
