###     Copyright (C) 2020 : Raynald Laheurte
###
###     This program is free software: you can redistribute it and/or modify
###     it under the terms of the GNU Lesser General Public License as published by
###     the Free Software Foundation, either version 3 of the License, or
###     (at your option) any later version.
###
###     This program is distributed in the hope that it will be useful,
###     but WITHOUT ANY WARRANTY; without even the implied warranty of
###     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
###     GNU Lesser General Public License for more details.
###
###     You should have received a copy of the GNU Lesser General Public License
###     along with this program.  If not, see <http://www.gnu.org/licenses/>.
###
##### \file main.py
##### \file _Fonctions_Enseignant.py
#####
##### \author Raynald Laheurte (raynald.laheurte@u-bordeaux.fr)
##### GMP (IUT de BORDEAUX / University of Bordeaux)


from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport
from enum import Enum


#########################################
######## Recuperer variables config
######################################## 
import configparser
config = configparser.ConfigParser();
config.read('config.cfg');

login_HP = config .get('session_HP', 'login');
password_HP = config .get('session_HP', 'password');
url_HP = config .get('session_HP', 'url');

print(str(login_HP) + str(password_HP) + str(url_HP)

#########################################
######## Connection base HP / ServiceWeb
######################################## 
session = Session()
session.auth = HTTPBasicAuth(login_HP, password_HP")

lPrefixeWsdl=url_HP


# Interfaces utilisées
Admin = Client(lPrefixeWsdl + 'IHpSvcWAdmin', transport=Transport(session=session))

Enseigant = Client(lPrefixeWsdl + 'IHpSvcWEnseignants', transport=Transport(session=session))
Matiere = Client(lPrefixeWsdl + 'IHpSvcWMatieres', transport=Transport(session=session))
Famille = Client(lPrefixeWsdl + 'IHpSvcWFamilles', transport=Transport(session=session))


# Affichage de la version
print ('Connecté à ' + Admin.service.Version());

########################################
######## MATIERES
########################################    
# # Affichage du nombre de matières
# print ('Il y a ' + str(Matiere.service.NombreMatieres()) + ' matières dans la base ');

# # Affichage de la liste des matières
# Matiere_lCles = Matiere.service.TrierTableauDeMatieresParLibelleEtCode ({'THpSvcWCleMatiere' : Matiere.service.ToutesLesMatieres()});
# Matiere_lClesIn = {'THpSvcWCleMatiere' : Matiere_lCles};

# Matiere_lCodes = Matiere.service.CodesTableauDeMatieres(Matiere_lClesIn);
# Matiere_lLibelles = Matiere.service.LibellesTableauDeMatieres(Matiere_lClesIn);
# Matiere_lLibellesLongg = Matiere.service.LibellesLongsTableauDeMatieres(Matiere_lClesIn);

# for i in range (len (Matiere_lCles)): 
#   print (str(Matiere_lCles[i]) + ' '  + str(Matiere_lCodes[i] if Matiere_lCodes[i] is not None else '') + ' '  + str(Matiere_lLibelles[i]) + ' : '  + str(Matiere_lLibellesLongs[i] if Matiere_lLibellesLongs[i] is not None else '-'))
######## Validé




########################################
######## ENSEIGNANTS
########################################
# Affichage du nombre de Enseignants
# print ('Il y a ' + str(Enseigant.service.NombreEnseignants()) + ' Enseignants dans la base ');

# Affichage du nom d'un enseignant à partir de son ID (valeur INT)
E_cle = '4187';
# print(type(E_cle))
E_Nom = Enseigant.service.NomEnseignant(E_cle);
# print(type(E_Nom))
# print(E_Nom)
######## Validé

# Affichage de la liste des enseignats
Enseignant_lCles = Enseigant.service.TrierTableauDEnseignantsParNomPrenomEtCode ({'THpSvcWCleEnseignant' : Enseigant.service.TousLesEnseignants()});
# Enseignant_lClesIn = {'THpSvcWCleEnseignant' : Enseignant_lCles};

# Enseignant_lcivilite = Enseigant.service.CivilitesTableauDEnseignants(Enseignant_lClesIn);
# Enseignant_lnom = Enseigant.service.NomsTableauDEnseignants(Enseignant_lClesIn);
# Enseignant_lprenom = Enseigant.service.PrenomsTableauDEnseignants(Enseignant_lClesIn);
# for i in range (len (Enseignant_lCles)): 
#   print (str(Enseignant_lCles[i]) + ' '  + str(Enseignant_lcivilite[i]) + ' '  + str(Enseignant_lnom[i])+ ' '  + str(Enseignant_lprenom[i])  )
# ####### Validé


# Extraction à partir du tableau d'un nom 
# print(type(Enseignant_lnom))
# index_zwang = Enseignant_lnom.index('ZWANG');
# print(str(index_zwang))

# print(Enseignant_lnom[index_zwang])
######## Validé


########################################
######## FAMILLES
#########################################
## Énumération des genres utilisants des familles  
#class Genre(Enum):
#    e_gfAppariteur = 'gfAppariteur'
#    e_gfCalendrier = 'gfCalendrier'
#    e_gfContacts = 'gfContacts'
#    e_gfCours = 'gfCours'
#    e_gfCursus = 'gfCursus'
#    e_gfEnseignant = 'gfEnseignant'
#    e_gfEntreprise = 'gfEntreprise'
#    e_gfEtudiant = 'gfEtudiant'
#    e_gfMatiere = 'gfMatiere'
#    e_gfModule = 'gfModule'
#    e_gfPanneauLumieux = 'gfPanneauLumieux'
#    e_gfPeriodeNotation = 'gfPeriodeNotation'
#    e_gfPromotion = 'gfPromotion'
#    e_gfRegroupement = 'gfRegroupement'
#    e_gfSalle = 'gfSalle'
#    e_gfType = 'gfType'
#
#    
## Recherche clé pour Rubrique GMP dans la famille Département pour le Genre Enseignant  
#Famille_Enseignant_lCles = Famille.service.ToutesLesFamillesDuGenre (Genre.e_gfEnseignant.value);
#Famille_Enseignant_lClesIn = {'THpSvcWCleFamille' : Famille_Enseignant_lCles};
#
#Famille_Enseignant_llibelle = Famille.service.LibellesTableauDeFamilles (Famille_Enseignant_lClesIn);
#
#print('Clés de ToutesLesFamilles Enseignant = ' + str(Famille_Enseignant_lCles))
#print('Libellés de ToutesLesFamilles Enseignant = ' + str(Famille_Enseignant_llibelle))
#
## Extraction de la clé de la famille Département 
#index_Departement_Enseignant = Famille_Enseignant_llibelle.index('Département');
#lcle_Departement_Enseignant = Famille_Enseignant_lCles[index_Departement_Enseignant];
#print('Clé de la famille Département = ' + str(lcle_Departement_Enseignant))
#print(Famille.service.LibelleFamille(lcle_Departement_Enseignant))
#
#Rubrique_Departement_Enseignant_lCles = Famille.service.ToutesLesRubriquesDeLaFamille (lcle_Departement_Enseignant);
#Rubrique_Departement_Enseignant_lClesIn = {'THpSvcWCleRubrique' : Rubrique_Departement_Enseignant_lCles};
#
#Rubrique_Departement_Enseignant_llibelle = Famille.service.LibellesTableauDeRubriques(Rubrique_Departement_Enseignant_lClesIn);
#
#print('Clé des rubriques de la famille Département dans Enseignant = ' + str(Rubrique_Departement_Enseignant_lCles))
#print('Libellés de LibellesTableauDeRubriques Département/Enseignant = ' + str(Rubrique_Departement_Enseignant_llibelle))
#
## Extraction de la clé de la rubrique GMP de la famille Département 
#index_GMP_Departement_Enseignant = Rubrique_Departement_Enseignant_llibelle.index('GMP');
#
#
#
#
#
#
#cle_Departement_Enseignant = Famille.service.FamillesDeLibelle ('Département')
#print(str(cle_Departement_Enseignant))
Famille_Enseignant_lClesIn2 = {'THpSvcWCleFamille' : [17] };
# La meme chose mais en une seule ligne  Extraction de la clé de la rubrique GMP de la famille Département 
print('###### La meme chose mais en une seule ligne')
cle_GMP_Departement_Enseignant = Famille.service.RubriquesDeLaFamilleParLibelle (Famille.service.FamillesDeLibelle ('Département')[0],'GMP')[0];
#cle_GMP_Departement_Enseignant = Famille.service.RubriquesDeLaFamilleParLibelle (cle_Departement_Enseignant[0],'GMP');
print(str(type(cle_GMP_Departement_Enseignant)))
print(str(cle_GMP_Departement_Enseignant))









print(str(Enseignant_lCles[-1]))


lcle_GMP_Departement_Enseignant = Rubrique_Departement_Enseignant_lCles[index_GMP_Departement_Enseignant];
print('Clé de la rubrique GMP de la famille Département = ' + str(lcle_GMP_Departement_Enseignant))
print(Famille.service.LibelleRubrique(lcle_GMP_Departement_Enseignant))

# Clé des rubriques de la famille Département pour un enseignant  
#tota = Famille.service.RubriqueDeLEnseignantDeFamille (lcle_Departement_Enseignant,E_cle);
#tota = Famille.service.RubriqueDeLEnseignantDeFamille (lcle_Departement_Enseignant,E_cle);
print('Cle enseignant famille = ' + str(tota))


Rubrique_Departement_Enseignant_lClesIn = {'THpSvcWCleRubrique' : tota};
Rubrique_Departement_Enseignant_llibelle = Famille.service.LibellesTableauDeRubriques(Rubrique_Departement_Enseignant_lClesIn);

print('L enseignant ' + str(Enseigant.service.NomEnseignant(E_cle)) + ' est au(x) département(s) ' + str(Rubrique_Departement_Enseignant_llibelle))
######## Validé

###### A faire 
# *Construction d'un tableau d'enseignant appartenant au département GMP
#   - boucle pour construire un tableau





