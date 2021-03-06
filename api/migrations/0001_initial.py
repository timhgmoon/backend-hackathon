# Generated by Django 4.0.3 on 2022-03-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('postalZip', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('Company', models.CharField(max_length=100)),
                ('companyFunded', models.CharField(max_length=100)),
                ('userID', models.CharField(max_length=500)),
                ('team', models.CharField(max_length=100)),
                ('paid', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
