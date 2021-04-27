from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date')
    description = models.TextField()


class Question(models.Model):
    TEXTINPUT = 'TEXTINPUT'
    SINGLECHOICE = 'SINGLECHOICE'
    MULTYCHOICE = 'MULTYCHOICE'
        
    QUESTION_TYPE = [
        (TEXTINPUT, 'Text Input'),
        (SINGLECHOICE, 'Single Choice'),
        (MULTYCHOICE, 'Multy choice'),
    ]

    text = models.CharField(max_length=300)
    question_type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPE,
        default=TEXTINPUT
    )
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)


class QuestionOption(models.Model):
    option = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='question_options', on_delete=models.CASCADE)


class QuestionReply(models.Model):
    guest_user_id = models.IntegerField()
    question_option = models.ForeignKey(
        QuestionOption,
        blank=True,
        null=True,
        related_name='question_option_replies',
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        related_name='question_replies',
        on_delete=models.CASCADE
    )
    value = models.CharField(max_length=200, blank=True, null=True)
