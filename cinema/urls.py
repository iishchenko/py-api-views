from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenreAPIView, \
    ActorListCreateView, ActorDetailView, CinemaHallViewSet, MovieViewSet

app_name = "cinema"  # Set the app_name here

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"cinema_halls", CinemaHallViewSet)

urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("actors/", ActorListCreateView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("", include(router.urls)),
]
