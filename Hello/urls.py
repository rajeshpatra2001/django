from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Administrator"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to Xperience Portal"



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
]
