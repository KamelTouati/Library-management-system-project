from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategoryForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save()
        

    context =  {
        'books' : Book.objects.all(),
        'categories' : Category.objects.all(),
        'BookForm' : BookForm(),
        'CategoryForm' : CategoryForm(),
        'allBooks' : Book.objects.filter(active = True).count(),
        'booksSold' : Book.objects.filter(status = 'sold').count(),
        'booksRetal' : Book.objects.filter(status = 'rental').count(),
        'booksAvailable' : Book.objects.filter(status = 'available').count(),
    }
    return render(request, 'pages/index.html', context)

def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title: 
            search = search.filter(title__icontains=title)

    context =  {
        'books' : search,
        'categories' : Category.objects.all(),
        'BookForm' : BookForm(),
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else: 
        book_save = BookForm(instance=book_id)
    context = {
        'form' : book_save,
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')
