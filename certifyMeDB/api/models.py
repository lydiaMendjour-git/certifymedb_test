from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

#la table account


class AccountManager(BaseUserManager): 

#cette classe permet de creer un user normal
    def create_user(self, username, email, password=None, role='startup', is_verified=False):
        if not email:
            raise ValueError("L'adresse email est obligatoire")#assurer que un email est fournis
        email = self.normalize_email(email) #Convertit l’email en minuscule et enlève les espaces inutiles
        user = self.model(username=username, email=email, role=role, is_verified=is_verified)#creer un user
        user.set_password(password)#Hash automatiquement le mot de passe
        user.save(using=self._db)#save dans la bdd
        return user

#cette classe permet de creer un super admmin  qui peut gerer la bdd (obligatoire) elle fait appel a la classse createuser
    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
      #les droits d'administration


class Account(AbstractBaseUser, PermissionsMixin):
    
    #definition des roles utilisée pour eviter les erreurs
    ROLE_CHOICES = [
        ('université', 'Université'),
        ('entreprise', 'Entreprise'),
        ('ministère', 'Ministère'),
        ('école_privée', 'École Privée'),
        ('école_formation', 'École de Formation'),
        ('startup', 'Startup'),
    ]

    id_account = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Django gère le hashage automatiquement
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)#limiter le choix
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #idk whats this chatgpt fixed it mais askip kayan conflict mea Django’s default authentication system
    groups = models.ManyToManyField(Group, related_name="account_users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="account_permissions", blank=True)


    objects = AccountManager()#Associe le AccountManager au modèle

    USERNAME_FIELD = 'email'#Connexion avec l’email au lieu du username
    REQUIRED_FIELDS = ['username'] #Django demandera username en plus du mot de passe lors de la création d’un super utilisateur.

    def __str__(self):
        return f"{self.username} ({self.role})" #Affiche username role quand on affiche un utilisateur



#la table official uni( les unis qui existent en algerie)
class OfficialUniversity(models.Model):
    id_official_uni = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    region = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email_domain = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

#la table unis (les unis qui ont fait une inscription sur notre plateforme)

class University(models.Model):
    id_university = models.AutoField(primary_key=True)
    id_account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="university")  # Relation 1-1 avec Account
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
  

    def __str__(self):
        return f"{self.name} - {self.id_account.username}"  # Affiche le nom + user associé



#les etudiants de chaque université cette table est initialement vide apres labonnement de une uni sa bdd va etre integrée dans cette table 
class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    id_account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="student")  # Un compte par étudiant
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="students")  # Plusieurs étudiants par université
    matricule = models.CharField(max_length=50, unique=True)  # Identifiant unique de l'étudiant
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.matricule}"
    

#la table entreprise
class Company(models.Model):
    id_company = models.AutoField(primary_key=True)
    id_account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="company")
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#la table ministere

class Ministry(models.Model):
    id_ministry = models.AutoField(primary_key=True)
    id_account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="ministry")
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name