""""
Now that our models and migrations are set up we need to configure URLs so that the API can handle requests

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet
from .views import OfficialUniversityViewSet
from .views import UniversityViewSet
from .views import StudentViewSet



#configure urls for accounts
router = DefaultRouter() # Création du routeur 
router.register(r'accounts', AccountViewSet)  # Enregistrement de la route pour accounts

urlpatterns = [
    path('api/', include(router.urls)),  # Inclusion de toutes les routes générées automatiquement get post delete..
]



#configure urls for official unis
router = DefaultRouter()
router.register(r'official-universities', OfficialUniversityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#configure urls for our plateforme unis
router = DefaultRouter()
router.register(r'universities', UniversityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#configure urls for students

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),  ]