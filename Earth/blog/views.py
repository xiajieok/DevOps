from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from  blog import models
import json
#from blog import comment_hander
#from blog.forms import ArticleForm,handle_uploaded_file
def index(request):
    category_obj = models.Category.objects.get(position_index=1)
    article_list = models.Article.objects.filter(status='published')
    return render(request,'blog/index.html',{'category_list':category_list,
                                            'article_list':article_list,
                                            'category_obj':category_obj,
                                            })


