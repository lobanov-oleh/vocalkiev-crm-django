from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
]

urlpatterns += i18n_patterns(
    path('', include('vocalkiev.apps.vocalkiev_com.urls')),
    path('crm/', include('vocalkiev.apps.crm.urls')),
)
