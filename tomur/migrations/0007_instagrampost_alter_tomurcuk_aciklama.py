# Generated by Django 5.1 on 2024-09-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomur', '0006_remove_tomurcuk_email_telefon_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_url', models.URLField(verbose_name='Instagram Gönderi Bağlantısı')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='tomurcuk',
            name='aciklama',
            field=models.TextField(default='Açıklama girilmedi', max_length=210),
        ),
    ]
