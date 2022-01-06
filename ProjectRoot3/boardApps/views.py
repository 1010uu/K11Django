from django.shortcuts import render, redirect
from .models import Post01

#첫화면 메인 띄우기
def main(request):
    return render(request, 'boardApps/main.html')

#리스트 게시물 가져오기
def list(request):
    postlist = Post01.objects.all().order_by('-id')
    return render(request, 'boardApps/list.html', {'postlist':postlist})

#리스트 상세보기
def view(request, pk):
    post = Post01.objects.get(pk=pk)
    return render(request, 'boardApps/view.html', {'post':post})

def write(request):
    if request.method=='POST':
        try:
            Post01.objects.create(
                titles = request.POST['titles'],
                writer = request.POST['writer'],
                email = request.POST['cookie@naver.com'],
                contents = request.POST['contents'],
                postdate = request.POST['postdate'],
                visitcount = request.POST['123'],
                file =  request.FILES['file'],
            )
        except:
            Post01.objects.create(
                titles = request.POST['titles'],
                writer = request.POST['writer'],
                email = request.POST['cookie@naver.com'],
                contents = request.POST['contents'],
                postdate = request.POST['2022-01-06'],
                visitcount = request.POST['123'],
            )
        return redirect('../list')
    return render(request, 'boardApps/write.html')