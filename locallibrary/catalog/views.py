from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Language
from django.views import generic
from django.http import Http404
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # your own name for the list as a template variable
    template_name = 'book_list.html'  # Specify your own template name/location
   
    
class BookDetailView(generic.DetailView):
    model = Book 
    template_name = 'book_details.html'  # Specify your own template name/location

def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('Book does not exist')

    return render (request, 'catalog/templates/book_details.html', context={'book': book})

def index(request):
    """ View function for home page of site."""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    num_authors = Author.objects.count()  # The 'all()' is implied by default
    num_genres = Genre.objects.count()
    
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }
    
    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)