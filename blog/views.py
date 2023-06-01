from django.http import HttpResponse, HttpRequest
from django.urls import path
from django.shortcuts import render
from . import models
# from django.http import render

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

