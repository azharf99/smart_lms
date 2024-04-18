from django.db import models
from django.utils.translation import gettext as _  
from courses.models import Course
# Create your models here.
class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    module_name = models.CharField(_("Module Name"), max_length=255)
    module_order = models.IntegerField(_("Module Order"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.course} {self.module_name}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["module_id"]),
        ]
        verbose_name = _("Module")
        verbose_name_plural = _("Modules")
        ordering = ["-created_at"]
        db_table = "modules"