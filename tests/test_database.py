import pytest
import os
import sys
sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from models.modelsusers import Users, Pays, Prix, Base

# Fixture pour créer un moteur de base de données
@pytest.fixture(scope='module')
def engine():
    return create_engine('sqlite:///test_database.sqlite')

# Fixture pour créer une session de base de données
@pytest.fixture(scope='module')
def session(engine: Engine):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

# Test pour ajouter un utilisateur
def test_ajouter_utilisateur(session):
    new_user = Users(name='TestUser')
    session.add(new_user)
    session.commit()
    
    user = session.query(Users).filter_by(name='TestUser').first()
    assert user is not None
    assert user.name == 'TestUser'

# Test pour ajouter un pays
def test_ajouter_pays(session):
    new_pays = Pays(pays='TestCountry')
    session.add(new_pays)
    session.commit()
    
    pays = session.query(Pays).filter_by(pays='TestCountry').first()
    assert pays is not None
    assert pays.pays == 'TestCountry'

# Test pour ajouter un prix
def test_ajouter_prix(session):
    new_prix = Prix(prix=100)
    session.add(new_prix)
    session.commit()
    
    prix = session.query(Prix).filter_by(prix=100).first()
    assert prix is not None
    assert prix.prix == 100

# Test pour mettre à jour un utilisateur avec un pays
def test_mettre_a_jour_utilisateur(session):
    new_pays = Pays(pays='France')
    session.add(new_pays)
    session.commit()

    new_user = Users(name='Toto', pays_id=new_pays.pays_id)
    session.add(new_user)
    session.commit()
    
    updated_user = session.query(Users).filter_by(name='Toto').first()
    assert updated_user is not None
    assert updated_user.pays_id == new_pays.pays_id
