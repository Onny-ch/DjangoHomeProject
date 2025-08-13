from django.db import models

from users.models import User


class Blogs(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
    )
    content = models.TextField(
        verbose_name="Содержимое записи",
    )
    preview = models.ImageField(
        upload_to="previews",
        verbose_name="Изображение",
        null=True,
        blank=True,
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    publication_sign = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )
    creator = models.ForeignKey(
        User,
        verbose_name="Создатель",
        help_text="Укажите создателя публикации",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = [
            "created_at",
        ]
