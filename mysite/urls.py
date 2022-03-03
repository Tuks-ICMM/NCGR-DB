from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from gene_details import views as gene_views
from home import views as home_views
from search import views as search_views
from variant_details import views as variant_views
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    # path("hpo_list/", home_views.hpo_list, name="hpo_list"),
    # path("hpo/<str:gene>/", gene_views.genehpo_view, name="genehpo_view"),
    # path("vep/<str:variant_name>/", variant_views.vep_view, name="vep_view"),
    # # path("filter_and_rank/", home_views.filter_view, name="filter_and_rank"),
    path("filter_results/", home_views.filter_view, name="filter_view"),
    path("search/", search_views.search, name="search"),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add django-advanced-filters urls
urlpatterns = urlpatterns + [
    url(r"^advanced_filters/", include("advanced_filters.urls"))
]
urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
