from django.db import models
from django.utils.translation import gettext as _  
from submissions.models import Submission
# Create your models here.
class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, verbose_name=_("Submission"))
    grade = models.CharField(_("Grade"), max_length=10)  # For numeric, use a suitable field type
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.submission} {self.grade}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["grade_id"]),
        ]
        verbose_name = _("Grade")
        verbose_name_plural = _("Grades")
        ordering = ["-created_at"]
        db_table = "grades"