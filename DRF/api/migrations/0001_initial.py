# Generated by Django 4.2.3 on 2023-07-06 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pages', models.IntegerField()),
                ('publish_date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
