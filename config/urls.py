from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path('api-auth/', include('rest_framework.urls')),

    path("api/", include("apps.users.api.urls")),
    path("api/", include("apps.tasks.api.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)