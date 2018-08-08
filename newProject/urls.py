from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'newProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
     url(r'^users/', include('apps.users.urls',namespace='users', app_name='users'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
