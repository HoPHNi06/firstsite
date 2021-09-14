from django.shortcuts import render, redirect, get_object_or_404
from .models import Articles, ArticleStatistic
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, View
from django.db.models import Q
from django.utils import timezone
from django.db.models import Sum

class SearchResultsView(ListView):
    model = Articles
    template_name = 'news/search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Articles.objects.filter(
            Q(title__icontains=query) | Q(anons__icontains=query) | Q(full_text__icontains=query)
        )
        return object_list
def news_home(request):
    news = Articles.objects.order_by('-id')
    return render(request, 'news/news_home.html', {'news': news})


class ArticlesView(DetailView):
    model = Articles
    template_name = 'news/news_view.html'  # Шаблон статьи
    context_object_name = 'art'

    def update_views(self, request, *args, **kwargs):
        model = Articles
        model.views += 1  # инкрементируем счётчик просмотров и обновляем поле в базе данных
        model.save(update_fields=['views'])

        return render(template_name=self.template_name)
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_view.html'
    context_object_name = 'art'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/news_update.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'

def news_add(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.photo = request.FILES['photo']
            article.author = request.user
            article.save()
            return redirect('news_home')
        else:
            error = "Форма была неверной!"

    form = ArticlesForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/news_add.html', data)

