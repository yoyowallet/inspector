from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'system', api.SystemViewSet)
router.register(r'environment', api.EnvironmentViewSet)
router.register(r'instance', api.InstanceViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for System
    path('systems/system/', views.SystemListView.as_view(), name='systems_system_list'),
    path('systems/system/create/', views.SystemCreateView.as_view(), name='systems_system_create'),
    path('systems/system/update/<int:pk>/', views.SystemUpdateView.as_view(), name='systems_system_update'),
)

urlpatterns += (
    # urls for Environment
    path('systems/environment/', views.EnvironmentListView.as_view(), name='systems_environment_list'),
    path('systems/environment/create/', views.EnvironmentCreateView.as_view(), name='systems_environment_create'),
    path('systems/environment/update/<int:pk>/', views.EnvironmentUpdateView.as_view(),
         name='systems_environment_update'),
)

urlpatterns += (
    # urls for Instance
    path('systems/instance/', views.InstanceListView.as_view(), name='systems_instance_list'),
    path('systems/instance/create/', views.InstanceCreateView.as_view(), name='systems_instance_create'),
    path('systems/instance/detail/<int:pk>/', views.InstanceDetailView.as_view(), name='systems_instance_detail'),
    path('systems/instance/update/<int:pk>/', views.InstanceUpdateView.as_view(), name='systems_instance_update'),
)
