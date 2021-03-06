# Generated by Django 2.0.4 on 2018-04-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180421_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=30, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Логин'),
        ),
    ]
