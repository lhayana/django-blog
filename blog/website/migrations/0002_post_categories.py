# Generated by Django 4.1 on 2023-02-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TC', 'Tecnologia'), ('GR', 'Geral')], default='GR', max_length=2),
        ),
    ]
