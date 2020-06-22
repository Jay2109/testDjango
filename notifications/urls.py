from django.urls import path
from . import views

app_name = "notifications"
urlpatterns = [
    path("all/", views.NotificationListView.as_view(), name="notifications",),
    path(
        "<int:pk>", views.NotificationDetailView.as_view(), name="notification_detail",
    ),
]
