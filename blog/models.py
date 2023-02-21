from django.db import models
from django.contrib.auth.models import User

# Category 클래스 구현
# SlugField : url로 통신하는 Django의 통신방식에 걸맞게 입력한 값이 URL화 되도록 자동으로 변경
# 특수문자 에러처리, allow_unicode=True를 입력하면 한국어 등 영어 외의 언어도 사용 가능
# unique=True : 전체 테이블의 해당 categoryName은 1개만 만들어지도록 구현

class Category(models.Model):
    categoryName = models.CharField(max_length=30, unique=True) 
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)

    def __str__(self):
        return self.categoryName

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'categories'


class Tag(models.Model):
    tagName = models.CharField(max_length=30, unique=True) 
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)

    def __str__(self):
        return self.tagName

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'


# Create your models here. 
# DB의 테이블을 좀더 쉽게 꺼내오기 위해 클래스 형식으로 바꿔주는 기능
class Post(models.Model):
    # 게시글에 필요한 필드: Primary Key, 제목, 내용, 작성일, 수정일, 작성자
    title = models.CharField(max_length=50)
    content = models.TextField()

    # upload_to= 경로
    # 어딘가 똑같은 폴더에 저장해주면 좋겠습니다
    # warm cold - 출신/년/월/일 경로로 처음에 지정을 해줄게요
    # blank=True : SQL 쿼리문으로 변환시 Null 가능(Nullable)한 필드를 만드는 옵션
    header_img = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    updated_at = models.DateTimeField(auto_now=True)  # 값을 변경할 수 있음. default 값으로 현재시간이 찍혀있음 
    
    # 작성자 - 외래키로 참조
    # CASCADE : User를 삭제하면 현재 테이블의 관련된 모든 데이터 삭제
    # author = models.ForeignKey(User, on_delete=models.CASCADE) 
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # blank=True : 글 작성시 옵셔널 필드
    # 다대다 관계는 ManyToManyField를 통해 관계를 맺음
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[[{self.pk}] {self.title}        by {self.author}]'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def first_post_query(self):
        return Post.objects.all().last().title

    def get_file_extension(self):
        return f'{self.file_upload}'.split('.')[-1]
