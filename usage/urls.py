from django.urls import path

from . import views


urlpatterns = [
    path(
        "usage-types/",
        views.ListCreateUsageTypesAPIView.as_view(),
        name="get_post_usage_types",
    ),
    path(
        "usage-types/<uuid:pk>/",
        views.RetrieveUpdateDestroyUsageTypesAPIView.as_view(),
        name="get_delete_update_usage_types",
    ),
    path(
        "usages/<uuid:pk>/",
        views.RetrieveUpdateDestroyUsageAPIView.as_view(),
        name="get_delete_update_usage",
    ),
    path("usages/", views.ListCreateUsageAPIView.as_view(), name="get_post_usages"),
]
