from django.urls import path, include

from ClassBased_Views.web_app.views import ArticleView

urlpatterns = [
    path("", ArticleView.as_view(), name="List of Articles"),
]