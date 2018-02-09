from django.urls import path, include, re_path
from game import views

#from game.views import WordViewSet, QuestionViewSet, AnswerViewSet

urlpatterns = [
	path('', views.HomePageView.as_view()),
]