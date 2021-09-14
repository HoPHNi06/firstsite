from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.db.models import ImageField
from django.contrib.auth.models import User
from django.templatetags.static import static

class Articles(models.Model):
    author = models.ForeignKey(User, related_name="Articles", on_delete=models.SET_NULL, null=True)
    title = models.CharField('Название:', max_length = 50)
    anons = models.CharField('Анонс:', max_length = 250)
    full_text = models.TextField('Статья:')
    date = models.DateTimeField('Дата создания:', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения:', auto_now_add=True, null=True)
    photo = ImageField('Фото статьи:', upload_to="articles", null=True, blank=True)
    views = models.IntegerField('Просмотры', default=0)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('user/img/profile-pic/default-profile-picture.png')


class ArticleStatistic(models.Model):
    class Meta:
        db_table = "ArticleStatistic"

    article = models.ForeignKey(Articles, on_delete=models.CASCADE)  # внешний ключ на статью
    date = models.DateField('Дата', default=timezone.now)  # дата
    views = models.IntegerField('Просмотры', default=0)  # количество просмотров в эту дату

    def __str__(self):
        return self.article.title

class ArticleStatisticAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')  # отображаемые поля в админке
    search_fields = ('__str__', )                # поле, по которому производится поиск


