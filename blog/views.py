from django.http import HttpResponse, HttpRequest
from django.urls import path
from django.shortcuts import render, redirect
from . import models
from . import forms
from django.views.generic import ListView, DetailView


# Create your views here

# 클라이언트 자원, 텍스트 형식
# 방문할때마다 쿠키 +1씩 추가
# 개발자 도구/application/cookies 확인
def counter1(req):
    visits = int(req.COOKIES.get('visits', 0)) + 1
    res = HttpResponse( f"cookie: {visits}")
    res.set_cookie('visits', visits)
    return res

# 서버 자원, object형
# 방문할때마다 쿠키 +1씩 추가
# 개발자도구/application/session 확인
def counter2(req):
    req.session['count'] = req.session.get('count', 0) + 1
    return HttpResponse( f"session: {req.session['count']}")

def post_detail(req: HttpRequest, pk: int) -> HttpResponse:
    post = models.Post.objects.get(pk=pk)
    return render(req, 'blog/detail.html' , { 'post': post })

def index(request):
    posts = models.Post.objects.all()    
    return render(request, 'blog/index.html', {'posts':posts})
    # return HttpResponse(posts)
    
def post_create(req):
    if req.method == "POST":
        form = forms.PostModelForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect("/blog/")
    
    else:
        form = forms.PostModelForm()
        return render(req, 'blog/create.html' , {'form': form})
    
    
# Generic views
# 클래스 뷰 중 가장 많이 사용되는 구조로 CRUD 작업을 위한 기본 구조 제공
# 설정을 통한 기능 변경 및 커스터마이징
# 간결한 코드 작성

# class PostListView (ListView):
#     model = models.Post
#     template_name = "blog/post_list.html"
#     context_object_name = "post_list"

# class PostDetailView (DetailView):
#     model = models.Post
#     template_name = "blog/post_detail.html"
#     context_object_name = "post"

# class PostCreateView (CreateView):
#     model = models.Post
#     form_class = forms.PostModelForm
#     template_name = "blog/post_create.html"
#     success_url = "/blog/posts/"



# ORM
# Post.objects. filter(title__contains=’test’)
# Post.objects. filter(title__icontains=’this’)
# Post.objects. filter(title__startswith=’This’)
# Post.objects. filter(title__endswith=’title’)
# Post.objects. filter(id__in=[1, 2, 3])
# Post.objects. filter(id__range=( 1, 
# 10))Post.objects. filter(published_at__lt=timezone.now())
# Post.objects. filter(published_at__gte=timezone.now())
# Post.objects. filter(created_at__year=’ 2019’)
# Post.objects. filter(created_at__month=’ 5’)
# Post.objects. filter(created_at__day=’ 21’)
# Post.objects. filter(published_at__isnull= True)

