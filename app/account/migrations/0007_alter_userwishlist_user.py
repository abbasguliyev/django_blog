# Generated by Django 4.1.1 on 2022-09-18 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_userreadblogs_read_blogs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwishlist',
            name='user',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='wish_lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
