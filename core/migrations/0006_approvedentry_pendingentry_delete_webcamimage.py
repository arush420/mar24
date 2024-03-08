# Generated by Django 5.0.1 on 2024-03-06 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_webcamimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovedEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PendingEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=100)),
                ('field2', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='WebcamImage',
        ),
    ]
