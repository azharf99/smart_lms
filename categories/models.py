from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(_("Category Name"), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f"{self.category_name}"
    
    # from django.urls import reverse 
    # def get_absolute_url(self):
    #     return reverse()

    class Meta:
        indexes = [
            models.Index(fields=["category_id"]),
        ]
        verbose_name = _("category")
        verbose_name_plural = _("categories")
        ordering = ["-created_at"]
        db_table = "categories"