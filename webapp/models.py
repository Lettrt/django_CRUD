from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название', )
    author = models.CharField(max_length=30, verbose_name='Автор')
    content = models.TextField(max_length=3000, verbose_name='Содержание', help_text='Не больше 3000 символов')
    created_at  = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return f'{self.id}. {self.title}: {self.author}'
