"""le modelviewSet fournit automatiquement toutes les opérations CRUD get post delete..."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer
from .models import OfficialUniversity
from .serializers import OfficialUniversitySerializer
from .models import University
from .serializers import UniversitySerializer
from .models import Student
from .serializers import StudentSerializer



#viewset of account
class AccountViewSet(viewsets.ModelViewSet):

   
    queryset = Account.objects.all() #Récupère tous les objets de la table account
    serializer_class = AccountSerializer #Spécifie quel serializer utiliser pour convertir les objets en JSON.

#viewset of official uni
class OfficialUniversityViewSet(viewsets.ModelViewSet):
    queryset = OfficialUniversity.objects.all()
    serializer_class = OfficialUniversitySerializer

#viewset of unis in certifyme
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

#viewset of students in certifyme

class StudentViewSet(viewsets.ModelViewSet):
    """
    API permettant de gérer les étudiants (CRUD).
    """
    queryset = Student.objects.all()  # Récupère tous les étudiants
    serializer_class = StudentSerializer  # Utilise le serializer défini
