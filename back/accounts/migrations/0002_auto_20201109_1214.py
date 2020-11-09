# Generated by Django 2.2.15 on 2020-11-09 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('post', '0002_auto_20201109_1214'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='like_user', to='post.RecommendMusic'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]