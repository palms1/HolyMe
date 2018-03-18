from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def index(req):

	posts = Post.objects.all()[:10]

	context = {
		'posts': posts
	}
	return render(req, 'blog/index.html', context)

def detalhe(req, id):
	post = get_object_or_404(Post, pk=id)
	#post = Post.objects.get(id=id)
	texto = post.body.strip(' ')
	texto = texto.rstrip()
	#print(texto)
	
	context = {
		'post': post,
		'texto': texto
	}

	return render(req, 'blog/details.html', context)