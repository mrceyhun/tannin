from django.urls import path, include, re_path
from wordapi import views

from rest_framework.routers import DefaultRouter
from wordapi.views import WordViewSet, QuestionViewSet, AnswerViewSet

router = DefaultRouter()
router.register(prefix='words', viewset=WordViewSet)
router.register(prefix='qs', viewset=QuestionViewSet)
router.register(prefix='as', viewset=AnswerViewSet)

urlpatterns = [
	path('docs/', views.SwaggerSchemaView.as_view()),
]
urlpatterns += router.urls



"""
╔══╗ 
║██║ 
║(O)║♫ ♪ ♫ ♪
╚══╝
▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █
Min- - - - - - - - - - - -●Max
"""