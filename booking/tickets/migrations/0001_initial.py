# Generated by Django 2.1.2 on 2019-05-12 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Airline',
                'verbose_name_plural': 'Airlines',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Description of the ticker', null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('airline', models.ForeignKey(help_text='Airline of the ticket', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tickets.Airline')),
                ('end_city', models.ForeignKey(help_text='Ticket end endpoint', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tickets.City')),
                ('start_city', models.ForeignKey(help_text='Ticket start endpoint', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tickets.City')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('name', 'country')},
        ),
    ]