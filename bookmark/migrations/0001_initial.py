# Generated by Django 2.2.6 on 2019-11-18 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='사이트 제목')),
                ('url', models.URLField(unique=True, verbose_name='URL주소')),
            ],
        ),
    ]