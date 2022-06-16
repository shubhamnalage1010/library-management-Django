from django.shortcuts import render, HttpResponseRedirect
from .forms import BookRegistration
from .models import Book


#Add and Show all items
def add_show(request):

    if request.method == 'POST':
        form = BookRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']

            booksave = Book(name=name, author=author, category=category)
            booksave.save()
            form = BookRegistration()
    else:
        form = BookRegistration()
    
    addbook = Book.objects.all()

    return render(request, 'addshow.html', {'form':form, 'book': addbook})

#delete

def delete_data(request, id):
    if request.method == 'POST':
        books = Book.objects.get(pk=id)
        books.delete()
        return HttpResponseRedirect('/book/bookrecord')

#update and edit
def update_data(request, id):
    if request.method == 'POST':
        books = Book.objects.get(pk=id)
        form = BookRegistration(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book/bookrecord')
    else:
        books = Book.objects.get(pk=id)
        form = BookRegistration(instance=books)
    return render(request, 'updatebook.html', {'form':form})


