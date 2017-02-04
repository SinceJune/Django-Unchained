from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from article.models import Article


def index(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 2)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'articles': articles})
