from django.db import models

# Create your models here.
class BaseModel(models.Model):
    """
    Base model for each model we use in our project
    """
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_updated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
