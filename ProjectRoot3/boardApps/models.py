from django.db import models

#멤버 테이블
class Member(models.Model):
    name = models.CharField(max_length=50) #작성자의 이름
    email=models.EmailField() #이메일   
    def __str__(self):
        return self.name

#게시판 테이블
class Post(models.Model):
    titles = models.CharField(max_length=50) #제목
    writer = models.ForeignKey('Member', on_delete=models.CASCADE) #작성자
    contents = models.TextField() #내용
    postdate = models.DateField() #작성일
    visitcount = models.CharField(max_length=50) #조회수
    file = models.ImageField(blank=True, null=True) #첨부
    
    def __str__(self):
        return self.titles

#게시판 테이블 다시 생성..
class Post00(models.Model):
    titles = models.CharField(max_length=50) #제목
    writer = models.CharField(max_length=50) #작성자
    contents = models.TextField() #내용
    postdate = models.DateField() #작성일
    visitcount = models.CharField(max_length=50) #조회수
    file = models.ImageField(blank=True, null=True) #첨부
    
    def __str__(self):
        return self.titles
    
class Post01(models.Model):
    titles = models.CharField(max_length=50) #제목
    writer = models.CharField(max_length=50) #작성자
    email=models.EmailField() #이메일
    contents = models.TextField() #내용
    postdate = models.DateField() #작성일
    visitcount = models.CharField(max_length=50) #조회수
    file = models.ImageField(blank=True, null=True) #첨부
    
    
    def __str__(self):
        return self.titles