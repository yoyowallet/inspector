from allauth.account.views import LoginView, SignupView

from .forms import InspectorLoginForm, InspectorSignupForm


class InspectorLoginView(LoginView):
    form_class = InspectorLoginForm


class InspectorSignupView(SignupView):
    form_class = InspectorSignupForm
