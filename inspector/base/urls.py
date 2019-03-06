from django.urls import path, include

from .views import InspectorLoginView, InspectorSignupView

urlpatterns = [
    path('health', include('health_check.urls')),
    path('accounts/login/', InspectorLoginView.as_view(), name='account_login'),
    path('accounts/signup/', InspectorSignupView.as_view(), name='account_signup'),
]
