from django.urls import path, re_path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r'^snippets/$', views.SnippetList.as_view()),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

# urlpatterns = [
#     re_path(r'^snippets/$', views_bk.snippet_list),
#     re_path(r'^snippets/(?P<pk>[0-9]+)/$', views_bk.snippet_detail),
# ]


urlpatterns = format_suffix_patterns(urlpatterns)