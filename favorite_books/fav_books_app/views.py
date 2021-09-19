from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from login_and_reg_app.models import *


def books_index(request): #dashboard
    context={
        # 'all_books': Book.objects.get(id = book_id),
        'book' : Book.objects.all()
    }
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        return render(request, 'books_homepage.html', context) #dashboard.html

def add_fav_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        Book.objects.create (title = request.POST['title'], desc = request.POST['desc'], uploaded_by = User.objects.get(id=request.session['user_id']))
        return redirect("/books")




#   WHERE SHOULD I PUT THIS??? NO SKIPPING LOGIN/REG AND USING URL PATH TO GET TO PAGE
    # if 'user_id' not in request.session:
    #     return redirect('/')
    # else:
    #     return render(request, 'books_homepage.html')
