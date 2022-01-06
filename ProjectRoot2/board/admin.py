from django.contrib import admin
from .models import Post

#관리자 모드에 Post테이블을 등록
admin.site.register(Post)
