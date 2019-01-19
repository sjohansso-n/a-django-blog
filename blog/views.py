from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Tag
from itertools import chain


POSTS_PER_PAGE = 6


def blog(request):
	posts = Post.objects.all().order_by('pub_date').reverse()

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
	posts = Post.objects.all().order_by('pub_date').reverse()
	latest_posts = Post.objects.all().order_by('pub_date').reverse()[:10]

	post_number = 0
	for thepost in posts:
		if post == thepost:
			break
		else:
			post_number += 1

	modulo = post_number % POSTS_PER_PAGE
	n = ((post_number - modulo) / POSTS_PER_PAGE)

	page = n + 1

	return render(request, 'blog/post.html', {
		'post' : post,
		'latest_posts' : latest_posts,
		'page': page,
	})




