from django.urls import path, include, re_path
from wordapi import views

from rest_framework.routers import DefaultRouter
from wordapi.views import WordViewSet, QuestionViewSet, AnswerViewSet
from wordapi.views import Q_and_W_relViewSet, A_and_W_relViewSet, Q_A_and_W_relViewSet
from wordapi.views import Q_qualityViewSet, A_qualityViewSet, Q_and_A_compatibilityViewSet

router = DefaultRouter()
router.register(prefix='words', viewset=WordViewSet)
router.register(prefix='qs', viewset=QuestionViewSet)
router.register(prefix='as', viewset=AnswerViewSet)
router.register(prefix='qw_rel', viewset=Q_and_W_relViewSet)
router.register(prefix='aw_rel', viewset=A_and_W_relViewSet)
router.register(prefix='qaw_rel', viewset=Q_A_and_W_relViewSet)
router.register(prefix='q_qual', viewset=Q_qualityViewSet)
router.register(prefix='a_qual', viewset=A_qualityViewSet)
router.register(prefix='qa_comp', viewset=Q_and_A_compatibilityViewSet)


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