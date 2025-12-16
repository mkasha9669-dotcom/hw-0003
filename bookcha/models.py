from django.db import models



class Author(models.Model):
    first_name = models.CharField(max_length=250)  
    last_name = models.CharField(max_length=250)    
    nationality = models.CharField(max_length=250)  
    age = models.PositiveIntegerField()              
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      

    def total_books(self):

 return self.books.count()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return store_name