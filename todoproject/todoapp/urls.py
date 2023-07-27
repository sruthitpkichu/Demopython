
from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('xyhome/',views.Tasklistview.as_view(),name='xyhome'),
    path('xydetail/<int:pk>/',views.TaskDetailview.as_view(),name='xydetail'),
    path('xyupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='xyupdate'),
    path('xydelete/<int:pk>/',views.TaskDeleteview.as_view(),name='xydelete'),

]