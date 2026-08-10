from django.shortcuts import render
from .models import Author, Book
from django.db import connection , reset_queries


def show_query(description, queryset):
    reset_queries()
    print(f"-------- {description} ---------") 

    # execute the queryset related fields
    for book in queryset:
       print(book.title, book.author.name)

    # count and print queries 
    queries = len(connection.queries)
    print(f"Total queries executed: {queries}")
    for i , query in enumerate(connection.queries):
        print(f"{1} : {query['sql']}")
    print("\n")


# Create your views here.
def home(request):
    # books = Book.objects.all()
    # for book in books:
    #     print(book.title , book.author.name)
    # return render(request, 'myap/home.html')

    books = Book.objects.select_related('author').all()
    for book in books:
        print(book.title , book.author.name)
    return render(request, 'myap/home.html')


# def home(request):

#     # without select_related() method
#     without_sr_books = Book.objects.all()
#     show_query("without_select_related()", without_sr_books)

#     # with select_related() method
#     with_sr_books = Book.objects.select_related('author').all()
#     show_query("with_select_related()", with_sr_books)

#     return render(request, 'myap/home.html')
