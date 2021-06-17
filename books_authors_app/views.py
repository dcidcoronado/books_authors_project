from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author


# Create your views here.
# import pdb; pdb.set_trace()

def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


def new_book(request):
    Book.objects.create(
        title=request.POST['title'],
        description=request.POST['description']
    )
    return redirect('/')


def view_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'GET':
        authors = book.authors.all()
        all_authors = Author.objects.all()
        context = {
            'book': book,
            'authors': authors,
            'all_authors': all_authors
        }
        return render(request, 'view_book.html', context)
    if request.method == 'POST':
        new_author = Author.objects.get(id=request.POST['new_authors'])
        book.authors.add(new_author)
        return redirect(f'/books/{book_id}')


def authors(request):
    authors = Author.objects.all()
    context ={
        'authors': authors
    }
    return render(request, 'authors.html', context)


def new_author(request):
    Author.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        notes=request.POST['notes']
    )
    return redirect('/authors')