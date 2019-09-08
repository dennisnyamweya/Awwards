from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.HomePageView.as_view(),name="home"),
    # path('detail/<int:id>',views.detail,name="detail"),
    path('detail/<int:pk>',views.ProjectDetailView.as_view(),name="detail"),
    path('search/',views.search,name="search"),
    path('projects/create',views.ProjectCreateView.as_view(),name="create"),
    path('projects/update/<int:pk>',views.ProjectUpdateView.as_view(),name="update"),
    path('projects/delete/<int:pk>',views.ProjectDeleteView.as_view(),name="delete"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
]