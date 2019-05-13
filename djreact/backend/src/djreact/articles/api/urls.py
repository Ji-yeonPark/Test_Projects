from django.conf.urls import url, include

from .views import ArticleListView, ArticleDetailView


urlpatterns = [
    url(r'', ArticleListView.as_view()),
    url(r'<pk>', ArticleDetailView.as_view()),
]
