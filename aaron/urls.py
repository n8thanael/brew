from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from aaron.views import AdaptiveGameView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('adaptive-game/', AdaptiveGameView, name="AdaptiveGame"),
    path('upload/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)