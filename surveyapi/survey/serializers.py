from django.contrib.auth.models import User
from survey.models import Survey, Question, QuestionOption, QuestionReply
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']


class SurveySerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = Survey
        fields = ['id', 'title', 'start_date', 'end_date', 'description', 'questions']


class SurveyUpdateSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = Survey
        fields = ['id', 'title', 'end_date', 'description', 'questions']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    question_options = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=QuestionOption.objects.all()
    )

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'survey', 'url', 'question_options']


class QuestionOptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ['id', 'option', 'question', 'url']


class QuestionReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionReply
        fields = ['id', 'guest_user_id', 'question_option', 'value', 'question']
