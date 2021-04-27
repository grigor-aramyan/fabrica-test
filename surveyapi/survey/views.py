from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from datetime import date
from django.contrib.auth.models import User
from survey.models import Survey, Question, QuestionOption, QuestionReply
from rest_framework import viewsets
from rest_framework import permissions
from survey.serializers import UserSerializer, SurveySerializer, SurveyUpdateSerializer, QuestionSerializer, QuestionOptionSerializer, QuestionReplySerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class SurveyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows surveys to be viewed or edited.
    """

    serializer_class = SurveySerializer
    model = Survey

    queryset = Survey.objects.all().order_by('-id')
    serializer_class = SurveySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = SurveyUpdateSerializer

        return serializer_class


@csrf_exempt
def survey_list(request):
    """
    API endpoint that allows active surveys to be viewed
    """
    if request.method == 'GET':
        surveys = Survey.objects.filter(end_date__gte=date.today()).order_by('-id')
        serializer = SurveySerializer(surveys, many=True)
        return JsonResponse(serializer.data, safe=False)
    


@csrf_exempt
def survey_result(request, user_id):
    """
    Retrieve survey list of particular user.
    """
    replies = QuestionReply.objects.filter(guest_user_id=user_id)

    if request.method == 'GET':
        serializer = QuestionReplySerializer(replies, many=True)
        return JsonResponse(serializer.data, safe=False)



class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows survey questions to be viewed or edited.
    """
    queryset = Question.objects.all().order_by('-id')
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionOptionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows question options to be viewed or edited.
    """
    queryset = QuestionOption.objects.all().order_by('-id')
    serializer_class = QuestionOptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionReplyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows question options to be viewed or edited.
    """
    queryset = QuestionReply.objects.all().order_by('-id')
    serializer_class = QuestionReplySerializer
    permission_classes = [permissions.AllowAny]