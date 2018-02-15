from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers

from rest_framework.decorators import detail_route, list_route

from rest_framework import viewsets

from wordapi.models import Word, Question, Answer
from wordapi.models import Q_and_W_rel, A_and_W_rel, Q_A_and_W_rel
from wordapi.models import Q_quality, A_quality, Q_and_A_compatibility

from wordapi.serializers import WordSerializer, QuestionSerializer, AnswerSerializer
from wordapi.serializers import Q_and_W_relSerializer, A_and_W_relSerializer, Q_A_and_W_relSerializer
from wordapi.serializers import Q_qualitySerializer, A_qualitySerializer, Q_and_A_compatibilitySerializer

#********************************************
#Word
class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    def retrieve(self, request, pk=None):
        #Random Word
        if pk == '0':
            random_word = Word.objects.order_by('?').first()
            serializer = WordSerializer(random_word)
            return Response(serializer.data)
        else:
            return super(WordViewSet, self).retrieve(request, pk)
#Question
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def retrieve(self, request, pk=None):
        #Random Question
        if pk == '0':
            random_question = Question.objects.order_by('?').first()
            serializer = QuestionSerializer(random_question)
            return Response(serializer.data)
        else:
            return super(QuestionViewSet, self).retrieve(request, pk)
#Answer
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def retrieve(self, request, pk=None):
        #Random Answer
        if pk == '0':
            random_answer = Answer.objects.order_by('?').first()
            serializer = AnswerSerializer(random_answer)
            return Response(serializer.data)
        else:
            return super(AnswerViewSet, self).retrieve(request, pk)

#Question and Word Relation
class Q_and_W_relViewSet(viewsets.ModelViewSet):
    queryset = Q_and_W_rel.objects.all()
    serializer_class = Q_and_W_relSerializer

#Answer and Word Relation
class A_and_W_relViewSet(viewsets.ModelViewSet):
    queryset = A_and_W_rel.objects.all()
    serializer_class = A_and_W_relSerializer

#Question, Answer and Word Relation
class Q_A_and_W_relViewSet(viewsets.ModelViewSet):
    queryset = Q_A_and_W_rel.objects.all()
    serializer_class = Q_A_and_W_relSerializer

#Question Quality
class Q_qualityViewSet(viewsets.ModelViewSet):
    queryset = Q_quality.objects.all()
    serializer_class = Q_qualitySerializer

#Answer Quality
class A_qualityViewSet(viewsets.ModelViewSet):
    queryset = A_quality.objects.all()
    serializer_class = A_qualitySerializer

#Question and Answer Compatibility Check
class Q_and_A_compatibilityViewSet(viewsets.ModelViewSet):
    queryset = Q_and_A_compatibility.objects.all()
    serializer_class = Q_and_A_compatibilitySerializer


"""
      ___           ___           ___           ___           ___           ___     
     /\  \         /\  \         |\__\         /\__\         /\__\         /\__\    
    /::\  \       /::\  \        |:|  |       /:/  /        /:/  /        /::|  |   
   /:/\:\  \     /:/\:\  \       |:|  |      /:/__/        /:/  /        /:|:|  |   
  /:/  \:\  \   /::\~\:\  \      |:|__|__   /::\  \ ___   /:/  /  ___   /:/|:|  |__ 
 /:/__/ \:\__\ /:/\:\ \:\__\     /::::\__\ /:/\:\  /\__\ /:/__/  /\__\ /:/ |:| /\__\
 \:\  \  \/__/ \:\~\:\ \/__/    /:/~~/~    \/__\:\/:/  / \:\  \ /:/  / \/__|:|/:/  /
  \:\  \        \:\ \:\__\     /:/  /           \::/  /   \:\  /:/  /      |:/:/  / 
   \:\  \        \:\ \/__/     \/__/            /:/  /     \:\/:/  /       |::/  /  
    \:\__\        \:\__\                       /:/  /       \::/  /        /:/  /   
     \/__/         \/__/                       \/__/         \/__/         \/__/    
"""
#********************************************
class SwaggerSchemaView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator(title='Pastebin API')
        schema = generator.get_schema(request=request)
        return Response(schema)


"""
 ██████╗███████╗██╗   ██╗██╗  ██╗██╗   ██╗███╗   ██╗
██╔════╝██╔════╝╚██╗ ██╔╝██║  ██║██║   ██║████╗  ██║
██║     █████╗   ╚████╔╝ ███████║██║   ██║██╔██╗ ██║
██║     ██╔══╝    ╚██╔╝  ██╔══██║██║   ██║██║╚██╗██║
╚██████╗███████╗   ██║   ██║  ██║╚██████╔╝██║ ╚████║
 ╚═════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                    
"""