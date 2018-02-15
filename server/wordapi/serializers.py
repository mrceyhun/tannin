from rest_framework import serializers
from wordapi.models import Word, Question, Answer
from wordapi.models import Q_and_W_rel, A_and_W_rel, Q_A_and_W_rel
from wordapi.models import Q_quality, A_quality, Q_and_A_compatibility
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

"""
───│─────────────────────────────────────
───│────────▄▄───▄▄───▄▄───▄▄───────│────
───▌────────▒▒───▒▒───▒▒───▒▒───────▌────
───▌──────▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄─────▌────
───▌────▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄───▋────
▀██████████████████████████████████████▄─
──▀███████████████████████████████████▀──
─────▀██████████████████████████████▀────
"""

class WordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Word
		fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    sentence = serializers.CharField()
    class Meta:
        model = Question
        fields = '__all__'
    def create(self, valid_data):
        return Question.objects.create(**valid_data)
    def update(self, instance, valid_data):
        instance.sentence = valid_data.get('sentence', instance.sentence)
        instance.save()

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
#######################################################
#######################################################

class Q_and_W_relSerializer(serializers.Serializer):
    class Meta:
        model = Q_and_W_rel
        fields = '__all__'
    word = serializers.IntegerField()
    question = QuestionSerializer()
    def to_representation(self, obj):
        try:
            word_obj = Word.objects.filter(pk=obj.word).first()
            # "question": ID, "word": ID
            return {"question": obj.question, "word": obj.word }
        except ObjectDoesNotExist:
            print('Given id of the Word is not in the DB')
    def create(self, validated_data):
        question_data = validated_data.pop('question')
        question_model = Question.objects.create(**question_data)
        relation = Q_and_W_rel.objects.create(question=question_model.pk, **validated_data)
        return relation


class A_and_W_relSerializer(serializers.ModelSerializer):
    class Meta:
        model = A_and_W_rel
        fields = '__all__'
    word = serializers.IntegerField()
    answer = AnswerSerializer()
    def to_representation(self, obj):
        try:
            word_obj = Word.objects.filter(pk=obj.word).first()
            # "answer": ID, "word": ID
            return {"answer": obj.answer, "word": obj.word }
        except ObjectDoesNotExist:
            print('Given id of the Word is not in the DB')
    def create(self, validated_data):
        answer_data = validated_data.pop('answer')
        answer_model = Answer.objects.create(**answer_data)
        relation = A_and_W_rel.objects.create(answer=answer_model.pk, **validated_data)
        return relation

#######################################################
#######################################################
class Q_A_and_W_relSerializer(serializers.ModelSerializer):
    class Meta:
        model = Q_A_and_W_rel
        fields = '__all__' #("question","answer","kelime",)


class Q_qualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Q_quality
        fields = '__all__' #("question","quality",)

class A_qualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = A_quality
        fields = '__all__' #("answer","quality",)

class Q_and_A_compatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Q_and_A_compatibility
        fields = '__all__' #("question","answer","compatibility",)
#-----------------------------------------------------
"""
▀██▀─▄███▄─▀██─██▀██▀▀█
─██─███─███─██─██─██▄█
─██─▀██▄██▀─▀█▄█▀─██▀█
▄██▄▄█▀▀▀─────▀──▄██▄▄█
"""
#-----------------------------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email = validated_data["email"],
            username = validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user

