from django.shortcuts import render

from rest_framework import viewsets
from wordapi.models import Word, Question, Answer
from wordapi.serializers import WordSerializer, QuestionSerializer, AnswerSerializer

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers

from rest_framework.decorators import detail_route, list_route
from random import shuffle
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