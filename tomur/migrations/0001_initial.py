# Generated by Django 5.1 on 2024-09-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kresler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(help_text='+90 ile başlayacak şekilde giriniz', max_length=20)),
            ],
        ),
    ]
