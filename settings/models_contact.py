from django.db import models

class Contact(models.Model):
    id = models.CharField(primary_key=True, max_length=255)

    platform = models.CharField(max_length=255)
    icon_uri = models.ImageField(upload_to='uploads/contact/')
    value = models.CharField(max_length=255)
    visited_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    created_by = models.CharField(null=True, max_length=255, default="system")
    updated_by = models.CharField(null=True, max_length=255, default="system")

    def __str__(self):
        return self.platform