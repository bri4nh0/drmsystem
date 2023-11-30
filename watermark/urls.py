from django.urls import path

from watermark import views
from watermark.views import ImageFileDetailView

urlpatterns = [
    path("", views.ImageListView.as_view(), name="index"),
    path("image/<int:pk>/", ImageFileDetailView.as_view(), name="image-detail"),
    path("delete/<int:pk>", views.delete_image_file, name='delete_image')
]
