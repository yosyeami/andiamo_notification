# Generated by Django 3.1.1 on 2020-12-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=250)),
                ('is_Accepted', models.BooleanField(default=False)),
            ],
        ),
    ]
