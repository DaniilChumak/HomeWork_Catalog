# Generated by Django 5.1 on 2024-08-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        help_text="Введите ссылку",
                        max_length=50,
                        unique=True,
                        verbose_name="Ссылка",
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        help_text="Введите текст",
                        max_length=1000,
                        verbose_name="Содержимое",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото",
                        null=True,
                        upload_to="BlogPost/photo",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False,
                        help_text="Опубликовать запись",
                        verbose_name="Опубликовано",
                    ),
                ),
                (
                    "view_count",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Укажите кол-во просмотров",
                        verbose_name="Счетчик просмотров",
                    ),
                ),
            ],
            options={
                "verbose_name": "Блог-пост",
                "verbose_name_plural": "Блог-посты",
            },
        ),
    ]
