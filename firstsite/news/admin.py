from django.contrib import admin

from .models import Articles, ArticleStatistic, ArticleStatisticAdmin

admin.site.register(Articles)

admin.site.register(ArticleStatistic, ArticleStatisticAdmin)