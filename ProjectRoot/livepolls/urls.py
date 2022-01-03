from django.urls import path
from . import views

app_name='livepolls'
urlpatterns = [
    
    #네임스페이스로 처리되므로 livepolls/를 제외한 URL패턴을 기술하면 된다.
    path('', views.index, name="index"),
    path('<int:question_id>/', views.detail, name='detail'), #livepolls/일련변호/
    path('<int:question_id>/results/', views.results, name='results'), #livepolls/일련변호/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), #livepolls/일련변호/vote/
]
