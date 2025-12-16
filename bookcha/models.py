from django.db import models



class Author(models.Model):
    first_name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    written_books = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return first_name




class Book(models.Model):
    book_name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    sold = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return book_name

class Store(models.Model):
    store_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return store_name