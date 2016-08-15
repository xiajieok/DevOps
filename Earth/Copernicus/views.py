from django.shortcuts import render, get_object_or_404
from Copernicus.models import Post
from Copernicus.forms import PostForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('Copernicus.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        print('判断form')
        if form.is_valid():
            post = form.save(commit=False)
            print('表单正常')
            post.author = request.user
            print('开始保存')
            post.save()
            print('ok')
            return redirect('Copernicus.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('Copernicus.views.post_detail', pk=pk)


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('Copernicus.views.post_list')


# def post_list(request):
#     posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
#     # posts = Post.objects.all().order_by('-published_date')
#     return render(request, 'blog/post_list.html', {'posts':posts})
def post_list(request):
    """所有已发布文章"""
    # postsAll = Post.objects.annotate(num_comment=Count('comment')).filter(
    #     published_date__isnull=False).prefetch_related(
    #     'category').prefetch_related('tags').order_by('-published_date')
    postsAll = Post.objects.annotate(num_comment=Count('id')).filter(published_date__isnull=False).order_by(
            '-published_date')
    # for p in postsAll:

    paginator = Paginator(postsAll, 3)  # Show 10 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts, 'page': True})
