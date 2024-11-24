from django.urls import path, include

from workoutPlanner.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('delete_account/', views.UserDeleteView.as_view(), name='delete_account'),
        path('profile-details/', views.ProfileDetailView.as_view(), name='profile-details' ),
        path('configure-profile/', views.ProfileConfView.as_view(), name='configure-profile'),
        ])
    )
]
