# Generated by Django 3.1.1 on 2020-09-08 12:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatusController',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('desired_status', models.CharField(choices=[('INIT', 'INIT'), ('RUN', 'RUN'), ('SUSPEND', 'SUSPEND'), ('TERMINATE', 'TERMINATE')], default='RUN', max_length=10)),
                ('current_status', models.CharField(choices=[('INIT', 'INIT'), ('RUN', 'RUN'), ('SUSPEND', 'SUSPEND'), ('TERMINATE', 'TERMINATE')], default='INIT', max_length=10)),
            ],
        ),
    ]
