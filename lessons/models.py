from django.db import models
from django.utils.translation import gettext as _  
from modules.models import Module
# Create your models here.
class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name=_("Module"))
    lesson_name = models.CharField(_("Lesson Name"), max_length=255)
    lesson_type = models.CharField(_("Lesson Type"), max_length=20, choices=(
        ('text', 'Text'),
        ('video', 'Video'),
        ('quiz', 'Quiz')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.module} {self.lesson_name}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["lesson_id"]),
        ]
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")
        ordering = ["-created_at"]
        db_table = "lessons"