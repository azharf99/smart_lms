from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from enrollments.models import Enrollment
from quizzes.models import Quiz
# Create your models here.
class Submission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, verbose_name=_("Enrollment"))
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_("Quiz"))
    submission_date = models.DateTimeField(_("Submission Date"), auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.question} {self.answer_text}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["submission_id"]),
        ]
        verbose_name = _("Submission")
        verbose_name_plural = _("Submissions")
        ordering = ["-created_at"]
        db_table = "submissions"