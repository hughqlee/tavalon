from django.urls import path
from .views import home, TeaListView

app_name = "teas"

urlpatterns = [
    path("", home, name="home"),
    path("list/", TeaListView.as_view(), name="list"),
]
