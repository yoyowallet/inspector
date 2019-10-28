from allauth.account.forms import LoginForm, SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Field, HTML

from .constants import SUBMIT_CSS_CLASSES


class InspectorLoginForm(LoginForm):
    helper = FormHelper()
    helper.layout = Layout(
        Field("login", placeholder="Username"),
        Field("password", placeholder="******"),
        Field("remember"),
        Row(
            Column(
                Submit("submit", "Login", css_class=SUBMIT_CSS_CLASSES),
                css_class="form-group col-md-6 mb-0",
            ),
            Column(
                HTML(
                    """
                <a class="small" href="{% url 'account_reset_password' %}">
                Forgot Password?
                </a>
                """
                ),
                css_class="text-right col-md-6 mb-0",
            ),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].label = ""
        self.fields["password"].label = ""


class InspectorSignupForm(SignupForm):
    helper = FormHelper()
    helper.form_show_labels = False
    helper.add_input(Submit("submit", "Sign Up", css_class=SUBMIT_CSS_CLASSES))
