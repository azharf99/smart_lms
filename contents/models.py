from django.db import models
from django.utils.translation import gettext as _  
from lessons.models import Lesson
# Create your models here.
class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_("Lesson"))
    content_type = models.CharField(_("Contect Type"), max_length=20, choices=(
        ('text', 'Text'),
        ('image', 'Image'),
        ('video_url', 'Video URL'),
        ('pdf_url', 'PDF URL')
    ))
    content_data = models.TextField(_("Content Data"))  # Store text, URLs, etc. 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.lesson} {self.content_data[:20]}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["content_id"]),
        ]
        verbose_name = _("Content")
        verbose_name_plural = _("Contents")
        ordering = ["-created_at"]
        db_table = "contents"