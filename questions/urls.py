from django.conf.urls import url
from .views import QuestionsView

urlpatterns = [
    url(r'', QuestionsView.as_view(), name="questions-list"),
]
