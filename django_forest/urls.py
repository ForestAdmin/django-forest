from django.urls import path, include

from . import views
from .authentication import urls as authentication_urls
from .resources import urls as collection_urls
from .stats import urls as stats_urls
from .actions import urls as actions_urls

app_name = 'django_forest'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('/authentication', include(authentication_urls)),
    path('/<slug:resource>', include(collection_urls)),
    path('/stats', include(stats_urls)),
    path('/actions/<slug:action_name>', include(actions_urls)),
]
