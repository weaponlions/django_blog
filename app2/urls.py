from django.urls import path
from app2 import views

urlpatterns = [
    ## ----------------------- TEmplate View -----------------------------------
    path('', views.UserView.as_view(template_name = "app2/main.html", extra_context={'name':'Harsh Saini', 'age':20}), name='app2'),

    ## ----------------------- Redirect View -----------------------------------
    path('redirect/', views.UserRedirectView.as_view(), name='redirects'),


    ## ----------------------- FORM View -----------------------------------
    path('Userform/', views.MyFormView.as_view(), name='userform'),


    ## ----------------------- LIST View -----------------------------------
    path('Userlist/', views.UserList.as_view(), name='userlist'),


    ## ----------------------- CREATE View -----------------------------------
    path('Createform/', views.MyModelsCreateView.as_view(), name='createform'),


    ## ----------------------- DETAIL View -----------------------------------
    path('Detail/<int:pk>', views.MyModelsDetail.as_view(), name='detail'),


    ### ----------------------- UPDATE View -----------------------------------
    path('Update/<int:pk>', views.MyModelsUpdateView.as_view(), name='update'),


    ### ----------------------- DELETE View -----------------------------------
    path('Delete/<int:pk>', views.MyModelsDeleteView.as_view(), name='delete'),
]
