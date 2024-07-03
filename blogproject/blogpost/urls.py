from django.urls import path
# from .views import BlogList, BlogDetail, BlogCreate, BlogDelete, BlogUpdate
from django.contrib import admin
from .views import BlogList, BlogDetail


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetail.as_view(), name='detail'),
]
