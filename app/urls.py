from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.HomePageView.as_view(),name="home"),
    # path('detail/<int:id>',views.detail,name="detail"),
    path('detail/<int:pk>',views.ProjectDetailView.as_view(),name="detail"),
    path('profile_detail/<int:pk>',views.ProfileDetailView.as_view(),name="profile_detail"),
    path('search/',views.search,name="search"),
    path('projects/create_profile',views.ProfileCreateView.as_view(),name="create_profile"),
    path('projects/profile_update/<int:pk>',views.ProfileUpdateView.as_view(),name="profile_update"),
    path('projects/profile_delete/<int:pk>',views.ProfileDeleteView.as_view(),name="profile_delete"),
    path('rating/',views.review_rating,name="review"),
    path('projects/create',views.ProjectCreateView.as_view(),name="create"),
    path('projects/update/<int:pk>',views.ProjectUpdateView.as_view(),name="update"),
    path('projects/delete/<int:pk>',views.ProjectDeleteView.as_view(),name="delete"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    
]