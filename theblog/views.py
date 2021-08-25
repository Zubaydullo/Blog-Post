from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# def home(request):
# 	return render(request, 'theblog/home.html', {})


def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class HomeView(ListView):
	model = Post
	template_name = 'theblog/home.html'
	ordering = ['-post_date']
	# ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data()
		context['cat_menu'] = cat_menu
		return context


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'theblog/article_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data()

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()
		
		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context['cat_menu'] = cat_menu
		context['total_likes'] = total_likes
		context['liked'] = liked
		return context

def categories(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	context = {"category_posts": category_posts, "cats": cats.title().replace('-', ' ')}
	return render(request, 'theblog/categories.html', context)


def category_list(request):
	cat_menu_list = Category.objects.all()
	context = {'cat_menu_list': cat_menu_list}
	return render(request, 'theblog/category_list.html', context)


class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = "theblog/add_post.html"
	# fields = "__all__"


class AddCategoryView(CreateView):
	model = Category
	template_name = "theblog/add_category.html"
	fields = "__all__"


class UpdatePostView(UpdateView):
	model = Post
	form_class = UpdatePostForm
	template_name = "theblog/update_post.html"


class DeletePostView(DeleteView):
	model = Post
	template_name = "theblog/delete_post.html"
	success_url = reverse_lazy("home")
