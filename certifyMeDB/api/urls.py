""""
Now that our models and migrations are set up we need to configure URLs so that the API can handle requests

"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet
from .views import OfficialUniversityViewSet
from .views import UniversityViewSet
from .views import StudentViewSet
from .views import MinistryViewSet
from .views import CompanyViewSet


router = DefaultRouter()# Création du routeur 

router.register(r'accounts', AccountViewSet)  # Enregistrement de la route pour accounts
router.register(r'official-universities', OfficialUniversityViewSet)# Enregistrement de la route off unis
router.register(r'universities', UniversityViewSet)# Enregistrement de la route pour unis
router.register(r'students', StudentViewSet, basename='student')# Enregistrement de la route pour students
router.register(r'companies', CompanyViewSet)# Enregistrement de la route pour companies
router.register(r'ministries', MinistryViewSet)# Enregistrement de la route pour minstry

urlpatterns = [
    path('', include(router.urls)),# Inclusion de toutes les routes générées automatiquement 
]