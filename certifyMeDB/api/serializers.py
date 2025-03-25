"""Les serializers sont essentiels en Django REST Framework car ils permettent de convertir des objets Django (modèles) 
en JSON et vice versa

Ils sont utilisés pour :

Envoyer des données au format JSON lorsqu’une API renvoie une réponse.

Valider les données entrantes avant de les enregistrer en base de données.

Simplifier la manipulation des objets entre la base de données et l’API.*\

"""

from rest_framework import serializers
from .models import Account
from .models import OfficialUniversity
from .models import University
from .models import Student
from .models import Company
from .models import Ministry

#serializer of account 
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account  # Spécifie le modèle à sérialiser
        fields = '__all__'  # Inclut tous les champs du modèle
        extra_kwargs = {'password': {'write_only': True}}  # Empêche l'affichage du mot de passe dans la réponse API



#si en enleve cette fonction le mot de passe sera stocké en clair dans la base de données au lieu d’être hashé

    def create(self, validated_data):
        """
        Création d'un nouvel utilisateur avec hashage du mot de passe.
        """
        user = Account.objects.create_user(**validated_data)
        return user
    

#serailizer of official unis
class OfficialUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialUniversity
        fields = '__all__'
  

#serailizer of our plateforme unis
class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


#serailizer of students
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



#serailizer of companies
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

#serailizer of ministry
class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = '__all__'