from django.db import models

class Translation(models.Model):
    source_language = models.CharField(max_length=50)
    target_language = models.CharField(max_length=50)
    source_text = models.TextField()
    translated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_language} to {self.target_language} - {self.source_text}"
