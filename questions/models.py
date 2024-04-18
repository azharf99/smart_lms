from django.db import models
from django.utils.translation import gettext as _
from quizzes.models import Quiz
# Create your models here.
class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_("Quiz"))
    question_text = models.TextField(_("Question Text"))
    question_type = models.CharField(_("Answer Type"), max_length=20, choices=(
        ('multiple_choice', 'Multiple Choice'),
        ('short_answer', 'Short Answer'),
        ('true_false', 'True/False')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.quiz} {self.question_text[:20]}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["question_id"]),
        ]
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ["-created_at"]
        db_table = "questions"