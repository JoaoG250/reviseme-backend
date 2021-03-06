import typing
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls.resolvers import URLPattern, URLResolver

from rest_framework import routers
from rest_framework.schemas import get_schema_view

import subject.views as subject_views
import topic.views as topic_views

router = routers.DefaultRouter()
router.register(r"subjects", subject_views.SubjectViewSet, basename="subject")
router.register(r"topics", topic_views.TopicViewSet, basename="topic")
router.register(r"topic-files", topic_views.TopicFileViewSet, basename="topic-file")
router.register(r"topic-links", topic_views.TopicLinkViewSet, basename="topic-link")
router.register(
    r"topic-revisions", topic_views.TopicRevisionViewSet, basename="topic-revision"
)

URL = typing.Union[URLPattern, URLResolver]
URLList = typing.List[URL]

schema_view = get_schema_view(
    title="Revise.me",
    description="Revise.me API documentation",
    version="1.0.0",
)

urlpatterns: URLList = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/openapi/", schema_view, name="openapi-schema"),
]

# djoser urls
urlpatterns += [
    url(r"^api/", include("djoser.urls")),
    url(r"^api/", include("djoser.urls.authtoken")),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "api/schema/",
            TemplateView.as_view(template_name="swagger-ui.html"),
            name="api-schema",
        ),
    ]
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )  # Not for production
