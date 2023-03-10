# Generated by Django 4.1.7 on 2023-02-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(max_length=30)),
                ('status', models.CharField(choices=[('allowed', 'Allowed'), ('unallowed', 'Unallowed')], max_length=30)),
                ('is_deleted', models.BooleanField()),
            ],
        ),
    ]
