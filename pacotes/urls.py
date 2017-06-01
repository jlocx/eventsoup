from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'crud-itens', views.ItemViewSet)
router.register(r'crud-pacotes', views.PacoteViewSet)
router.register(r'crud-item-pacote/(?P<slug_produto>[^/.]+)', views.ItemPacoteViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
