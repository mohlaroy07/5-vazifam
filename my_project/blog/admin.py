from django.contrib import admin
# from .models import Post

# admin.site.register(Post)


# from .models import Author, Comment, Category, Tag

# admin.site.register(Author)
# admin.site.register(Comment)
# admin.site.register(Category)
# admin.site.register(Tag)

from .models import Bag, Phone, Animal, Car, Book

admin.site.register(Bag)
admin.site.register(Phone)
admin.site.register(Animal)
admin.site.register(Car)
admin.site.register(Book)