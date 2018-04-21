# Generated by Django 2.0.4 on 2018-04-21 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180421_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'публикацию', 'verbose_name_plural': 'публикации'},
        ),
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'подписчиков', 'verbose_name_plural': 'подписчики'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default='', max_length=255, verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]