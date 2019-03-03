from django.urls import path

from .views import InspectorLoginView, InspectorSignupView

urlpatterns = [
    path('accounts/login/', InspectorLoginView.as_view(), name='account_login'),
    path('accounts/signup/', InspectorSignupView.as_view(), name='account_signup'),
]
