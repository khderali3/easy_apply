from django.urls import path



from .views import LogView, LogViewDeleteAll






urlpatterns = [
    path('staff/logs/', LogView.as_view()),
    path('staff/logs/delete_all/', LogViewDeleteAll.as_view()),
]