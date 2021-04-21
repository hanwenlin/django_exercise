from django.urls import path, re_path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetList)
router.register(r'users', views.UserList)

# API URL现在由路由器自动确定。
# 另外，我们还要包含可浏览的API的登录URL。
# urlpatterns = [
#     re_path(r'^', include(router.urls)),
#     re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


urlpatterns = [
    re_path(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='snippet-detail'),
    re_path(r'^users/$', views.UserList.as_view(), name='user-list'),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    re_path(r'^$', views.api_root),
    re_path(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight')
]

# urlpatterns = [
#     re_path(r'^snippets/$', views_bk.snippet_list),
#     re_path(r'^snippets/(?P<pk>[0-9]+)/$', views_bk.snippet_detail),
# ]


urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    re_path(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
]