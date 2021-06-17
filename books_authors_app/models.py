from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.title}"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    notes = models.TextField(null=True)
    books = models.ManyToManyField(Book, related_name='authors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __repr__(self):
        return f"{self.last_name}"
