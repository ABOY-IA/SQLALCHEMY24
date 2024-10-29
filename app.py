from models.modelsusers import Users, Pays, Prix, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import os

try:
    os.remove('database.sqlite') 
except:
    print("bllaaahhh")


# Déclaration du moteur de base de données
engine = create_engine('sqlite:///database.sqlite')

# Création de la base de données
Base.metadata.create_all(engine)

# Création d'une session
session = Session(bind=engine)
# Création d'un utilisateur
toto = Users(name="toto")
fr = Pays(pays="france")
p1 = Prix(prix=10)

# Insertion de l'utilisateur 
session.add(toto)
session.add(fr)
session.add(p1)
session.commit()

# Création d'une fonction pour ajouter de nouveaux utilisateurs
def ajouter_utilisateur(name, pays, prix):
    """
    Ajoute un nouvel utilisateur à la base de données.
    """
    # Création des instances
    new_user = Users(name=name)
    new_pays = Pays(pays=pays)
    new_prix = Prix(prix=prix)

    # Ajout des instances à la session
    session.add(new_user)
    session.add(new_pays)
    session.add(new_prix)

    # Validation de la transaction
    session.commit()

# Utilisation de la fonction pour ajouter des nouveaux utilisateurs
ajouter_utilisateur('tata', 'espagne', 20)
ajouter_utilisateur('titi', 'italie', 30)
ajouter_utilisateur('tutu', 'allemagne', 40)

def mettre_a_jour_utilisateur(name_user, name_pays):
    """Actualise l'utilisateur pour lui attribuer le pays spécifié."""
    # Récupérer l'utilisateur et le pays depuis la base de données
    user = session.query(Users).filter_by(name=name_user).first()
    pays = session.query(Pays).filter_by(pays=name_pays).first()
    
    if user and pays:
        # Mettre à jour l'utilisateur pour lui attribuer le pays
        user.pays_id = pays.pays_id
        session.commit()
        print(f"L'utilisateur {name_user} a été mis à jour avec le pays {name_pays}.")
    else:
        print("Utilisateur ou pays non trouvé.")

# Utiliser la fonction pour mettre à jour l'utilisateur toto
mettre_a_jour_utilisateur('toto', 'france')
mettre_a_jour_utilisateur('tata', 'espagne')
mettre_a_jour_utilisateur('titi', 'italie')
mettre_a_jour_utilisateur('tutu', 'allemagne')


