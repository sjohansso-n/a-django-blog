from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Tag
from itertools import chain


POSTS_PER_PAGE = 4


def blog(request):
	posts = Post.objects.all()

	paginator = Paginator(posts, POSTS_PER_PAGE)

	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range, deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render(request, 'blog/blog.html', {
		'posts' : posts,
	})

def post(request, post_id):
	post = Post.objects.get(pk=post_id)

	page = request.GET.get('page')

	return render(request, 'blog/post.html', {
		'post' : post,
		'page': page,
	})




