from django.shortcuts import render
from Copernicus.models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    # posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})