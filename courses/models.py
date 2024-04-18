from django.db import models
from django.utils.translation import gettext as _  
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(_("Course Name"), max_length=255)
    course_description = models.TextField(_("Course Description"))
    start_date = models.DateField(_("Start Date"))
    end_date = models.DateField(_("End Date"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Instructor"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.course_name} {self.instructor}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["course_id"]),
        ]
        verbose_name = _("course")
        verbose_name_plural = _("courses")
        ordering = ["-created_at"]
        db_table = "courses"