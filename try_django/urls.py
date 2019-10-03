from django.contrib import admin
from django.urls import path, include
from blog.views import blog_post_create_view
from .views import (
        home_page,
        about_page,
        contact_page,
        example_page,
)

urlpatterns = [
    path('', home_page),
    path('blog/', include('blog.urls')),
    path('blog-new/', blog_post_create_view),
    path('about/', about_page),
    path('contact/', contact_page),
    path('example/', example_page),
    path('admin/', admin.site.urls),
]
