from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

# Création de la base de données
Base = declarative_base()

# Déclaration de la table `pays`
class Pays(Base):
    __tablename__ = "pays"
    pays_id = Column(Integer, primary_key=True)
    pays = Column(String(255))    

# Déclaration de la table `users`
class Users(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    pays_id = Column(Integer)

    pays = relationship(
    'Pays',
    primaryjoin='Pays.pays_id == Users.pays_id',
    foreign_keys=pays_id)

# Déclaration de la table `prix`
class Prix(Base):
    __tablename__ = "prix"
    prix_id = Column(Integer, primary_key=True)
    prix = Column(Integer)

