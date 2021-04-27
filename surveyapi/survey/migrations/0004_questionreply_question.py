# Generated by Django 2.2.10 on 2021-04-27 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_questionreply'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionreply',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question_replies', to='survey.Question'),
            preserve_default=False,
        ),
    ]
