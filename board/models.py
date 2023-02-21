from django.db import models

# Create your models here.
<<<<<<< HEAD
=======
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
>>>>>>> ffa52d4a9521118ceee6cf9ce2a372a58f5bf6c7
