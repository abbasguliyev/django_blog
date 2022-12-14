# Generated by Django 4.1.1 on 2022-09-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('account', '0005_alter_userreadblogs_read_blogs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreadblogs',
            name='read_blogs',
            field=models.ManyToManyField(blank=True, related_name='read_blogs', to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='userwishlist',
            name='wish_list',
            field=models.ManyToManyField(blank=True, related_name='wish_lists', to='blog.blog'),
        ),
    ]
