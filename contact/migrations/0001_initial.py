# Generated by Django 2.0.7 on 2018-07-31 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('phone', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]
