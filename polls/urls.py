from django.conf.urls import url

from .  import views

app_name='polls'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'voter/$',views.voter,name='voter'),
    url(r'candid/$',views.candid,name='candid'),
    url(r'voteredit/$',views.voteredit,name='voteredit'),
    url(r'voterview/$',views.voterview,name='voterview'),
    url(r'edit/$',views.edit,name='edit'),
    url(r'edit2/$',views.edit2,name='edit2')
   

   
      
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
] 



