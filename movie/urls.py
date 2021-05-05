from django.urls import path
from movie import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('register', views.RegisterApi.as_view()),
    path('movie',views.movie,name='movie'),
    path('collection',views.collection,name='collection'),
    path(
        "collection/<uuid:uuid>/",
        views.Collectionview.as_view(),
        name="collection_uuid",
    ),

]