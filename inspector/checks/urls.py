from django.urls import path

from inspector.checks.views import (
        check_list_view,
        check_detail_view,
        checkrun_create_view

)

app_name = "checks"
urlpatterns = [
    path("", view=check_list_view, name="index"),
    path("<str:code>/", view=check_detail_view, name="detail"),
    path("checkrun/create/<int:check_id>/", checkrun_create_view, name="checkrun_create"),
]
