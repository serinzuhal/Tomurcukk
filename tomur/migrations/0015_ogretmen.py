# Generated by Django 5.1 on 2024-09-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomur', '0014_egitim_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ogretmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('resim', models.ImageField(upload_to='ogretmen_resimleri/')),
                ('verdigi_egitim', models.TextField()),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
