# Generated by Django 2.2.5 on 2020-04-21 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=90)),
                ('enrollment_num', models.IntegerField(unique=True)),
                ('complaintbox', models.TextField(max_length=255)),
            ],
        ),
    ]
