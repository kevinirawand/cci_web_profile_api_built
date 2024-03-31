from django.urls import path, include

from .v1.views import SettingViewSet, ContactViewSet

urlpatterns_v1 = [
    path('cms/', include([
        path('setting/', SettingViewSet.as_view({
            'post': 'create',
            'put': 'update',
        }), name='setting'),
        path('contact/', ContactViewSet.as_view({
            'post': 'create',
            'put': 'update',
            'delete': 'destroy',
        }), name='contact'),
    ])),
    path('setting/', SettingViewSet.as_view({
        'get': 'retrieve',
    }), name='setting-detail'),
    path('contact/', ContactViewSet.as_view({
        'get': 'list',
    }), name='setting-detail'),
]
