from . import views

from django.urls import path

urlpatterns = [
        path('',views.home,name='home'),
        # path('details',views.details,name='details')
        path('delete/<int:taskid>/',views.delete,name='delete'),
        path('update/<int:id>/',views.update,name='update'),
        path('home1/',views.TaskListView.as_view(),name='home1'),
        path('detail1/<int:pk>/',views.TaskDetailView.as_view(),name='detail1'),
        path('update1/<int:pk>/',views.TaskUpdateView.as_view(),name='update1'),
        path('delete1/<int:pk>/',views.TaskDeleteView.as_view(),name='delete1')

]