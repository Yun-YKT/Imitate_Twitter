from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view())  # 何も書かないと、指定したビューがトップページに表示される
]