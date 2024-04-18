from django.db import models
from django.utils.translation import gettext as _  
from lessons.models import Lesson
# Create your models here.
class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_("Lesson"))
    quiz_name = models.CharField(_("Quiz Name"), max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.lesson} {self.quiz_name}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["quiz_id"]),
        ]
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["-created_at"]
        db_table = "quizzes"