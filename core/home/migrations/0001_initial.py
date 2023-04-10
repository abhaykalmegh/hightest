# Generated by Django 4.2 on 2023-04-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(default=10)),
                ('recipients', models.TextField()),
                ('hashtags', models.TextField()),
                ('comments', models.TextField(null=True)),
                ('image', models.ImageField(max_length=255, null=True, upload_to='photos/user_form')),
            ],
        ),
    ]
