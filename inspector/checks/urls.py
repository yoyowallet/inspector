from django.urls import path, include
from rest_framework import routers

from inspector.checks.views import (
    check_list_view,
    check_detail_view,
    check_delete_view,
    checkrun_create_view
)
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'checkgroup', api.CheckGroupViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for CheckGroup
    path('checks/checkgroup/', views.CheckGroupListView.as_view(), name='checks_checkgroup_list'),
    path('checks/checkgroup/create/', views.CheckGroupCreateView.as_view(), name='checks_checkgroup_create'),
    path('checks/checkgroup/update/<int:pk>/', views.CheckGroupUpdateView.as_view(), name='checks_checkgroup_update'),
    path('checks/checkgroup/delete/<int:pk>', views.CheckGroupDeleteView.as_view(), name='checks_checkgroup_delete'),
)

urlpatterns += (
    # urls for CheckRun
    path('checks/checkrun/', views.CheckRunListView.as_view(), name='checks_checkrun_list'),
    path('checks/checkrun/create/', views.CheckRunCreateView.as_view(), name='checks_checkrun_create'),
    path('checks/checkrun/detail/<int:pk>/', views.CheckRunDetailView.as_view(), name='checks_checkrun_detail'),

)

urlpatterns += (
    path("checks/datacheck/", view=check_list_view, name="checks_datacheck_list"),
    path("checks/datacheck/detail/<int:pk>/", view=check_detail_view, name="checks_datacheck_detail"),
    path("checks/datacheck/delete/<int:pk>", check_delete_view, name="checks_datacheck_delete"),
    path("checkrun/create/<int:check_id>/", checkrun_create_view, name="checkrun_create"),
    path('checks/datacheck/create/', views.DatacheckCreateView.as_view(), name='checks_datacheck_create'),
    path('checks/datacheck/update/<int:pk>/', views.DatacheckUpdateView.as_view(), name='checks_datacheck_update'),
)

urlpatterns += (
    # urls for EnvironmentStatus
    path('checks/environmentstatus/', views.EnvironmentStatusListView.as_view(), name='checks_environmentstatus_list'),
)
