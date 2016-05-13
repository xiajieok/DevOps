from django.shortcuts import render
from django.shortcuts import HttpResponse,HttpResponseRedirect
from store import  models
# Create your views here.
def reg(request):
    if request.method == "POST":
        print(request.POST)
        i_username = request.POST.get('username')
        i_passwd = request.POST.get('passwd')
        tmp_dic = models.UserInfo.objects.filter(username=i_username)
        models.UserInfo.objects.create(username=i_username,
                                        password=i_passwd)
        return HttpResponseRedirect('/store/home/')

    else:
        return render(request, 'store/registry.html')
def login(request):
    user_list_obj = models.UserInfo.objects.all()
    return render(request, 'store/login.html', {'li': user_list_obj})
def check(request):
    i_username = request.POST.get('username')
    i_passwd = request.POST.get('password')
    #查询用户名和密码,然后对比
    user_list_obj = models.UserInfo.objects.filter(username=i_username)
    for line in user_list_obj:
        # print(line.username,line.password)
        if line.password == i_passwd:
            return HttpResponseRedirect('/store/home/')
        else:
            print('wrong!')
            return render(request, 'store/login.html', {'li': user_list_obj})

def home(request):
    # return HttpResponse('this is index')
    if request.method == 'POST':
        print(request.POST)
    else:
        return render(request,'store/start.html')
def books(request):
    books = models.Book.objects.all()
    publisher_list = models.Publisher.objects.all()
    author_list = models.Author.objects.all()
    return render(request,'store/book_list.html',{'li':books,
                                              'publishers':publisher_list,
                                             'authors':author_list
                                                  })
def authors(request):
    author_list = models.Author.objects.all()
    return render(request,'store/author_list.html',{'li':author_list})
def publishers(request):
    publisher_list = models.Publisher.objects.all()
    return render(request,'store/publisher_list.html',{'li':publisher_list})

def author_edit(request):
    if request.method == 'POST':
        first = request.POST.get('first_name')
        last = request.POST.get('last_name')
        models.Author.objects.create(first_name = first,
                                     last_name = last)
        return HttpResponseRedirect('/store/authors/')

def author_del(request):
    if request.method == 'POST':
        print(request.POST)
        ids = request.POST.getlist('choice')
        for i in ids:
            models.Author.objects.filter(id = i).delete()
        return HttpResponseRedirect('/store/authors/')
def book_edit(request):
     if request.method == 'POST':
        book_name = request.POST.get('name')
        publisher_id = request.POST.get('publisher_id')
        author_ids = request.POST.getlist('author_ids')
        new_book = models.Book(
            name = book_name,
            publisher_id = publisher_id,
            pulication_date = '2016-05-22'
        )
        new_book.save()
        new_book.authors.add(*author_ids)
        return HttpResponseRedirect('/store/books/')

def book_del(request):
    if request.method == 'POST':
        print(request.POST)
        ids = request.POST.getlist('choice')
        for i in ids:
            models.Book.objects.filter(id = i).delete()
        return HttpResponseRedirect('/store/books/')

def publisher_edit(request):
    if request.method == 'POST':
        p_name = request.POST.get('name')
        p_city = request.POST.get('city')
        p_state_province = request.POST.get('state_province')
        p_country = request.POST.get('country')
        p_website = request.POST.get('website')
        print(request.POST)
        models.Publisher.objects.create(name = p_name,
                                     city = p_city,
                                     state_province = p_state_province,
                                     country = p_country,
                                     website = p_website)
        return HttpResponseRedirect('/store/publishers/')

def publisher_del(request):
    if request.method == 'POST':
        print(request.POST)
        ids = request.POST.getlist('choice')
        for i in ids:
            models.Publisher.objects.filter(id = i).delete()
        return HttpResponseRedirect('/store/publishers/')

# def book(request):
#  if request.method == 'POST':
#         print(request.POST)
#         book_name = request.POST.get('name')
#         publisher_id = request.POST.get('publisher_id')
#         print('==>',request.POST.get('author_ids'))
#         author_ids = request.POST.getlist('author_ids')
#         #print(dir( request.POST))
#         print(book_name,publisher_id,author_ids)
#
#         new_book = models.Book(
#             name=book_name,
#             publisher_id = publisher_id,
#             publish_date = '2016-05-22'
#         )
#         new_book.save()
#         new_book.authors.add(*author_ids)
#         #new_book.authors.add(1,2,3,4)
#
#     books = models.Book.objects.all()
#     publisher_list = models.Publisher.objects.all()
#     author_list = models.Author.objects.all()
#
#
#     return render(request,'app01/book.html',{'books':books,
#                                                   'publishers':publisher_list,
#                                                  'authors':author_list
#                                                   })