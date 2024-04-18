from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from courses.models import Course
# Create your models here.
class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    enrollment_date = models.DateField(_("Enrollment Date"), auto_now_add=True)
    completion_status = models.CharField(_("Completion Status"), max_length=20, choices=(
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.user} {self.course} {self.enrollment_date}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["enrollment_id"]),
        ]
        verbose_name = _("Enrollment")
        verbose_name_plural = _("Enrollments")
        ordering = ["-created_at"]
        db_table = "enrollments"