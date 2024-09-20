# Generated by Django 5.1 on 2024-09-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomur', '0003_tomurcuk_aciklama_tomurcuk_email_tomurcuk_oda_adi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(default='Not Provided', help_text='+90 ile başlayacak şekilde giriniz', max_length=20)),
                ('adres', models.TextField(default='Adres girilmedi')),
            ],
            options={
                'verbose_name_plural': 'İletişim Bilgileri',
            },
        ),
        migrations.AlterModelOptions(
            name='tomurcuk',
            options={'verbose_name_plural': 'Kreşimizin Oda Bilgileri'},
        ),
        migrations.RemoveField(
            model_name='tomurcuk',
            name='telefon',
        ),
    ]
