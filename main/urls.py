from django.urls import path
from .views import evaluate_expression

urlpatterns = [
    path('evaluate/', evaluate_expression, name='evaluate-expression'),
]
