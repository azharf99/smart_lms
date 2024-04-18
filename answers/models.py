from django.db import models
from questions.models import Question
from django.utils.translation import gettext as _


class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_("Question"))
    answer_text = models.TextField(_("Answer Text"))
    is_correct = models.BooleanField(_("Is Correct?"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.question} {self.answer_text}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["answer_id"]),
        ]
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["-created_at"]
        db_table = "answers"