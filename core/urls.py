from core import views
from django.urls import path

urlpatterns = [
    path('tran/<int:model>', views.TranView.as_view()),
]