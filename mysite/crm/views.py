from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from crm import  models
from crm import forms
import hashlib
from django.contrib.auth import logout
#from django import forms
# Create your views here.

@login_required
def index(request):
    return render(request,'crm/index.html')
def acc_login(request):
    if request.method == 'POST':
        # print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            #pass authentication
            login(request,user)
            return HttpResponseRedirect('/crm/index/')
        else:
            login_err = "Wrong username or password!"
            return render(request,'crm/login.html',{'login_err':login_err})
    return render(request,'crm/login.html')
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/crm/index/')


# def login(request):
#     if request.method == 'POST':
#         i_username = request.POST.get('username')
#         i_passwd = md5Encode(request.POST.get('password'))
#
#         #查询用户名和密码,然后对比
#         user_list_obj = models.UserInfo.objects.filter(username=i_username)
#         for line in user_list_obj:
#             print(line.username,line.password)
#             if line.password == i_passwd:
#                 request.session['username'] = i_username
#                 print('%s is login...' %(i_username))
#                 return HttpResponseRedirect('/store/home/')
#             else:
#                 print('wrong!')
#                 return render(request, 'store/login.html')
#     return render(request,'store/login.html')
def Course(request):
    form = forms.CourseModelForm()
    if request.method == 'POST':
        form = forms.CourseModelForm(request.POST)
        if form.is_valid():
            print('form is ok')
            print(form)
            form.save()

    list = models.Course.objects.all()
    return render(request,'crm/Course.html',{'model_form':form,
                                             'li':list}
                  )

def Course_update(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('id'))
        new_id = request.POST.get('id')
        new_name = request.POST.get('name')
        new_price = request.POST.get('price')
        new_online_price = request.POST.get('online_price')
        new_brief = request.POST.get('brief')
        # Publisher.objects.filter(id=52).update(name='Apress Publishing')
        models.Course.objects.filter(id=new_id).update(name= new_name,
                                                       price = new_price,
                                                       online_price = new_online_price,
                                                       brief = new_brief)
    return HttpResponseRedirect('/crm/Course/')

def Course_del(request):
    if request.method == 'POST':
        print(request.POST)
        ids = request.POST.getlist('choice')
        for i in ids:
            models.Course.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/Course/')
def UserProfile(request):
    form = forms.UserProfileModelForm()
    if request.method == 'POST':
        # print(request.POST)
        form = forms.UserProfileModelForm(request.POST)
        if form.is_valid():
            print('form is ok')
            # print(form)
            form.save()
        else:
            print('NO     .......',form)
    list = models.UserProfile.objects.all()
    return render(request,'crm/UserProfile.html',{'model_form':form,
                                             'li':list}
                  )
def UserProfile_update(request):
    if request.method == 'POST':
        print(request.POST.get('id'))
        new_name = request.POST.get('name')
        models.UserProfile.objects.filter(name=new_name).update(name=new_name,
                                                           )
    return HttpResponseRedirect('/crm/UserProfile/')

def UserProfile_del(request):
    if request.method == 'POST':
        print(request.POST)
        ids = request.POST.getlist('choice')
        for i in ids:
            models.UserProfile.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/UserProfile/')
def ClassList(request):
    form = forms.ClassListModelForm()
    if request.method == 'POST':
        print(request.POST)
        form = forms.ClassListModelForm(request.POST)
        if form.is_valid():
            print('form is ok')
            print(form)
            form.save()
    Course_list = models.Course.objects.all()
    teachers_list = models.UserProfile.objects.all()
    list = models.ClassList.objects.all()
    return render(request,'crm/ClassList.html',{'model_form':form,
                                                'li':list,
                                                'Course_list':Course_list,
                                                'teachers_list':teachers_list,
                                                }
                  )
def ClassList_update(request):
    if request.method == 'POST':
        print(request.POST.get('course_id'))
        print(request.POST)
        s_id = request.POST.get('id')
        s_semster = request.POST.get('semster')
        s_course_type = request.POST.get('course_type')
        s_star_date = request.POST.get('star_date')
        s_gratute_date = request.POST.get('gratute_date')
        models.ClassList.objects.filter(id=s_id).update(semster=s_semster,
                                                        course_type=s_course_type,
                                                             star_date=s_star_date,
                                                             gratute_date=s_gratute_date,
                                                           )
    return HttpResponseRedirect('/crm/ClassList/')

def ClassList_del(request):
    if request.method == 'POST':
        print(request.POST)
        ids = request.POST.getlist('choice')
        for i in ids:
            models.ClassList.objects.filter(id = i).delete()
    return HttpResponseRedirect('/crm/ClassList/')
def Customer(request):
    form = forms.CustomerModelForm()
    if request.method == 'POST':
        print(request.POST)
        form = forms.CustomerModelForm(request.POST)
        if form.is_valid():
            print('form is ok')
            print(form)
            form.save()
    list = models.Customer.objects.all()
    consulant_list = models.UserProfile.objects.all()
    return render(request,'crm/Customer.html',{'model_form':form,
                                               'consulant_list':consulant_list,
                                            'li':list}
                  )
def School(request):
    form = forms.SchoolModelForm()
    if request.method == 'POST':
        print(request.POST)
        form = forms.SchoolModelForm(request.POST)
        if form.is_valid():
            print('form is ok')
            print(form)
            form.save()
    list = models.School.objects.all()
    return render(request,'crm/School.html',{'model_form':form,
                                            'li':list}
                  )
def School_update(request):
    if request.method == 'POST':
        print(request.POST.get('id'))
        new_name = request.POST.get('name')
        new_addr = request.POST.get('addr')
        models.School.objects.filter(name=new_name).update(addr = new_addr,)
    return HttpResponseRedirect('/crm/School/')
def School_del(request):
    if request.method == 'POST':
        print(request.POST)
        ids = request.POST.getlist('choice')
        for i in ids:
            models.School.objects.filter(id = i).delete()
        return HttpResponseRedirect('/crm/School/')
def ConultRecord(request):
    form = forms.ConultRecordModelForm()
    if request.method == 'POST':
        print(request.POST)
        form = forms.ConultRecordModelForm(request.POST)
        if form.is_valid():
            print('form is ok')
            print(form)
            form.save()
    list = models.ConultRecord.objects.all()
    return render(request,'crm/ConultRecord.html',{'model_form':form,
                                            'li':list}
                  )
def CourseRecord(request):
    form = forms.CourseRecordModelForm()
    if request.method == 'POST':
        print(request.POST)
        form = forms.CourseRecordModelForm(request.POST)
        if form.is_valid():
            print('form is ok')
            print(form)
            form.save()
    list = models.CourseRecord.objects.all()
    return render(request,'crm/CourseRecord.html',{'model_form':form,
                                            'li':list}
                  )
def StudyRecord(request):
    form = forms.StudyRecordModelForm()
    if request.method == 'POST':
        print(request.POST)
        form = forms.StudyRecordModelForm(request.POST)
        if form.is_valid():
            print('form is ok')
            print(form)
            form.save()
    list = models.StudyRecord.objects.all()
    return render(request,'crm/StudyRecord.html',{'model_form':form,
                                            'li':list}
                  )
def StudyRecord_update(request):
    if request.method == 'POST':
        print(request.POST.get('id'))
        new_name = request.POST.get('name')
        new_addr = request.POST.get('addr')
        models.StudyRecord.objects.filter(name=new_name).update(addr = new_addr,)
    return HttpResponseRedirect('/crm/StudyRecord/')


# form = forms.BookModelForm()
#     if request.method == 'POST':
#         print(request.POST)
#         form = forms.BookModelForm(request.POST)
#         if form.is_valid():
#             print('form is ok')
#             print(form)
#             form.save()
#     return render(request,'store/book_modelform.html',{'book_form':form})



