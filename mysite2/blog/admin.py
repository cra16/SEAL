
# Register your models here.
from django.contrib import admin  
from blog.models import Publisher, Author, Book  

admin.site.register(Publisher)  
admin.site.register(Author)  
admin.site.register(Book)  

