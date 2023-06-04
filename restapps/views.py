from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
    # 클래스 기반 뷰에서 요청이 들어올 때마다 실행되는 함수
    def dispatch(self, request, *args, **kwargs):
        
        # print보단 logger를 사용하는 것을 추천
        print("request.body:", request.body)
        print("request.POST:", request.POST)
        return super().dispatch(request, *args, **kwargs)
    
# def post_list(request):
#     # 2개 분기
#     # pass
    
# def post_detail(request, pk):
#     # request.method # => 3개 분기
#     # pass