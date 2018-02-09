from rest_framework import serializers
from wordapi.models import Word, Question, Answer
from django.contrib.auth.models import User

class WordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Word
		fields = ("kelime",)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("question",)

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("answer",)




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