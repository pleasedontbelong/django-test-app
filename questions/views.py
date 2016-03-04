from django.views import generic
from .models import Question


class QuestionsView(generic.ListView):
    template_name = 'questions.html'
    model = Question
