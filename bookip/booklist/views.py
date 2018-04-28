from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import books
from django.http import HttpResponse
from .forms import user_register,user_login,add_book
from django.views.generic import View
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def list_of_books(request,books=books):
	if request.user.is_authenticated:
		#from .models import books
		all_books=books.objects.order_by('-date')
		paginator = Paginator(all_books,5)
		page = request.GET.get('page')
		try:
			books=paginator.page(page)
		except PageNotAnInteger:
        # If page is not an integer, deliver first page.
			books = paginator.page(1)
		except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
			books = paginator.page(paginator.num_pages)
		return render(request,'booklist/booklist.html',{'books':books})
	else:
		return redirect('home:login_user')

def author_books(request,book_id):
	if request.user.is_authenticated:
		book=get_object_or_404(books, pk=book_id)
		return render(request,'booklist/booklist.html',{'books':books.objects.filter(pk=book_id)})
	else:
		return redirect('home:login_user')		
		
def recent_books(request):
    if request.user.is_authenticated:
        context={'books':books.objects.order_by('-date')[:5],
				"message":"Recently added"}
        return render(request,'booklist/booklist.html',context)
    
    else:
        return redirect('home:login_user')
		
		
		
		
def list_genre(request):
	context={}
	if request.user.is_authenticated:
		
		_genre=list(set(books.objects.values_list('genre',flat=True)))
		
		
		context['filter']=_genre
		
		return render(request,'booklist/genre_template.html',context)
	else:
		return redirect('home:login_user')
		
		
def list_author(request):
	context={}
	if request.user.is_authenticated:
		
		_books=books.objects.order_by('author')
		context={
		'filter':_books,
		
		}
		
		return render(request,'booklist/author_template.html',context)
	else:
		return redirect('home:login_user')
		
		

		
		
		
def genre_books(request,_genre):
	context={}
	if request.user.is_authenticated:
		
		genre_books=list(books.objects.filter(genre=_genre))
		
		
		
		if len(genre_books)>0:
			context['books']=genre_books
				
			return render(request,'booklist/booklist.html',context)
		
		else:
			raise Http404
	else:
		return redirect('home:login_user')
		
	
	

	
def rating_books(request):
	if request.user.is_authenticated:
		return render(request,'booklist/booklist.html',{'books':books.objects.order_by('-rating')})
	else:
		return redirect('home:login_user')

		
		

class add_book(View):
    model = books
    form_class=add_book
    template_name='booklist/book_submit.html'
    template_success='booklist/book_submit_success.html'

    # displays blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    #submits the filled form
    def post(self, request):
        form=self.form_class(request.POST)

        if form.is_valid():

            books=form.save(commit=False)
            _books = books
            #clean normalized data

            _books.name=form.cleaned_data['name']
            _books.author=form.cleaned_data['author']
            _books.genre=form.cleaned_data['genre']
            _books.rating = form.cleaned_data['rating']
            _books.stock=form.cleaned_data['stock']
            _books.book_cover=form.cleaned_data['book_cover']
            


            _books.save()
            return render(request, self.template_success, {'form': form})
        else:

            return render(request, self.template_name, {'form': form})


def search(request):
    if not request.user.is_authenticated:
        return redirect(request,'home:login_user')
    else:
        _books = books.objects.all()
        
        query = request.GET.get("q")
        if query:
            _books = books.objects.filter(
                Q(name__icontains=query) |
                Q(author__icontains=query)
            ).distinct()
            if len(_books)>0:
                return render(request, 'booklist/booklist.html', {
                    'books': _books
                })
            else:
                return render(request, 'booklist/booklist.html', {
                    'result_not_found':'result not found'
                })
            
        else:
            return render(request, 'music/index.html', {'albums': albums})



		

def logout_user(request):
	logout(request)
	return redirect('home:login_user')
        
