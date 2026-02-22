import os, sys

import ezdxf

import os
import math

import numpy

import sys
sys.path.append("/home/dgelo/lmgc90_user_2024/build")




if not os.path.isdir('./DATBOX'):
  os.mkdir('./DATBOX')

# import des modules
import math, numpy
from pylmgc90 import pre

# definition des conteneurs:
#   * de corps
bodies = pre.avatars()
#   * de materiaux
mats = pre.materials()
mods = pre.models()
#   * de lois de contacts
tacts = pre.tact_behavs()
#   * de tables de visibilite
svs = pre.see_tables()

# exemple 3D
dim = 3

# definition d'un modele rigide
mR3D = pre.model(name='rigid', physics='MECAx', 
                 element='Rxx3D', dimension=dim)
mods.addModel(mR3D)

# definition du materiau pour la fondation
tdur = pre.material(name='TDURx', materialType='RIGID', 
                    density=1000.)
# definition du materiau pour les blocs
stone = pre.material(name='STONE', materialType='RIGID', 
                     density=2750.)
# ajout des materiaux dans le conteneur
mats.addMaterial(tdur); mats.addMaterial(stone)

# parametres du script
#   * nombre de blocs
nb_blocs = 11
#   * ouverture angulaire d'un joint
theta_joint = math.pi/100.
#   * rayons interieur et exterieur
r_int = 0.8; r_ext = 1.

# calcul de l'ouverture corespondant a un bloc
theta_bloc = (math.pi - (nb_blocs - 1)*theta_joint)/ \
   nb_blocs
# calcul de l'epaisseur d'un bloc
e_bloc = r_ext - r_int
# calcul de l'epaisseur d'un joint
e_joint = r_ext*theta_joint



def extract_bodies_coordinates(file_path):
    bodies = []
    current_body= []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line == "Solid":
                if current_body:
                    bodies.append(current_body)
                    current_body = []
            elif line:
                # Convert coordinate string to tuple of floats
                coords = tuple(map(float, line.split(',')))
                current_body.append(coords)

        # Append last body
        if current_body:
            bodies.append(current_body)

    return bodies

# Example usage
file_path = 'node_middle.txt'  # Make sure this is the correct path
bodies_coords_1 = extract_bodies_coordinates(file_path)

# Example usage
file_path = 'node_edge.txt'  # Make sure this is the correct path
bodies_coords_2 = extract_bodies_coordinates(file_path)

print (bodies_coords_1[0])
print (type(bodies_coords_1[0][0]))
print (len(bodies_coords_1))











##vertices = numpy.zeros([8, 3], 'd')
###       - sommet 1
##vertices[0, 0]=bodies_coords[0][0][0]
##vertices[0, 1]=bodies_coords[0][0][1]
##vertices[0, 2]=bodies_coords[0][0][2]
###       - sommet 2
##vertices[1, 0]=bodies_coords[0][1][0]
##vertices[1, 1]=bodies_coords[0][1][1]
##vertices[1, 2]=bodies_coords[0][1][2]
###       - sommet 3
##vertices[2, 0]=bodies_coords[0][2][0]
##vertices[2, 1]=bodies_coords[0][2][1]
##vertices[2, 2]=bodies_coords[0][2][2]
###       - sommet 4
##vertices[3, 0]=bodies_coords[0][3][0]
##vertices[3, 1]=bodies_coords[0][3][1]
##vertices[3, 2]=bodies_coords[0][3][2]
###       - sommet 5
##vertices[4, 0]=bodies_coords[0][4][0]
##vertices[4, 1]=bodies_coords[0][4][1]
##vertices[4, 2]=bodies_coords[0][4][2]
###       - sommet 6
##vertices[5, 0]=bodies_coords[0][5][0]
##vertices[5, 1]=bodies_coords[0][5][1]
##vertices[5, 2]=bodies_coords[0][5][2]
###       - sommet 7
##vertices[6, 0]=bodies_coords[0][6][0]
##vertices[6, 1]=bodies_coords[0][6][1]
##vertices[6, 2]=bodies_coords[0][6][2]
###       - sommet 8
##vertices[7, 0]=bodies_coords[0][7][0]
##vertices[7, 1]=bodies_coords[0][7][1]
##vertices[7, 2]=bodies_coords[0][7][2]
###    * connectivite des faces
##faces = numpy.zeros([12, 3], 'i')
##faces[ 0, 0]=1; faces[ 0, 1]=2; faces[ 0, 2]=3
##faces[ 1, 0]=2; faces[ 1, 1]=5; faces[ 1, 2]=3
##faces[ 2, 0]=1; faces[ 2, 1]=2; faces[ 2, 2]=6
##faces[ 3, 0]=1; faces[ 3, 1]=6; faces[ 3, 2]=4
##faces[ 4, 0]=2; faces[ 4, 1]=5; faces[ 4, 2]=8
##faces[ 5, 0]=2; faces[ 5, 1]=8; faces[ 5, 2]=6
##faces[ 6, 0]=5; faces[ 6, 1]=3; faces[ 6, 2]=7
##faces[ 7, 0]=5; faces[ 7, 1]=7; faces[ 7, 2]=8
##faces[ 8, 0]=1; faces[ 8, 1]=3; faces[ 8, 2]=7
##faces[ 9, 0]=1; faces[ 9, 1]=7; faces[ 9, 2]=4
##faces[10, 0]=4; faces[10, 1]=6; faces[10, 2]=7
##faces[11, 0]=6; faces[11, 1]=8; faces[11, 2]=7   
##
### creation d'un nouvel avatar rigide pour le bloc
##block = pre.rigidPolyhedron(model=mR3D, material=stone, generation_type='full',
##		       vertices=vertices, faces=faces, color='REDxx')
### ajout du bloc a l'ensemble des corps
##bodies.addAvatar(block)




i=0

while i< len(bodies_coords_1):

	vertices = numpy.zeros([8, 3], 'd')
	#       - sommet 1
	vertices[0, 0]=bodies_coords_1[i][0][0]
	vertices[0, 1]=bodies_coords_1[i][0][1]
	vertices[0, 2]=bodies_coords_1[i][0][2]
	#       - sommet 2
	vertices[1, 0]=bodies_coords_1[i][1][0]
	vertices[1, 1]=bodies_coords_1[i][1][1]
	vertices[1, 2]=bodies_coords_1[i][1][2]
	#       - sommet 3
	vertices[2, 0]=bodies_coords_1[i][2][0]
	vertices[2, 1]=bodies_coords_1[i][2][1]
	vertices[2, 2]=bodies_coords_1[i][2][2]
	#       - sommet 4
	vertices[3, 0]=bodies_coords_1[i][3][0]
	vertices[3, 1]=bodies_coords_1[i][3][1]
	vertices[3, 2]=bodies_coords_1[i][3][2]
	#       - sommet 5
	vertices[4, 0]=bodies_coords_1[i][4][0]
	vertices[4, 1]=bodies_coords_1[i][4][1]
	vertices[4, 2]=bodies_coords_1[i][4][2]
	#       - sommet 6
	vertices[5, 0]=bodies_coords_1[i][5][0]
	vertices[5, 1]=bodies_coords_1[i][5][1]
	vertices[5, 2]=bodies_coords_1[i][5][2]
	#       - sommet 7
	vertices[6, 0]=bodies_coords_1[i][6][0]
	vertices[6, 1]=bodies_coords_1[i][6][1]
	vertices[6, 2]=bodies_coords_1[i][6][2]
	#       - sommet 8
	vertices[7, 0]=bodies_coords_1[i][7][0]
	vertices[7, 1]=bodies_coords_1[i][7][1]
	vertices[7, 2]=bodies_coords_1[i][7][2]
	#    * connectivite des faces
	faces = numpy.zeros([12, 3], 'i')
	faces[ 0, 0]=1; faces[ 0, 1]=2; faces[ 0, 2]=3
	faces[ 1, 0]=2; faces[ 1, 1]=5; faces[ 1, 2]=3
	faces[ 2, 0]=1; faces[ 2, 1]=2; faces[ 2, 2]=6
	faces[ 3, 0]=1; faces[ 3, 1]=6; faces[ 3, 2]=4
	faces[ 4, 0]=2; faces[ 4, 1]=5; faces[ 4, 2]=8
	faces[ 5, 0]=2; faces[ 5, 1]=8; faces[ 5, 2]=6
	faces[ 6, 0]=5; faces[ 6, 1]=3; faces[ 6, 2]=7
	faces[ 7, 0]=5; faces[ 7, 1]=7; faces[ 7, 2]=8
	faces[ 8, 0]=1; faces[ 8, 1]=3; faces[ 8, 2]=7
	faces[ 9, 0]=1; faces[ 9, 1]=7; faces[ 9, 2]=4
	faces[10, 0]=4; faces[10, 1]=6; faces[10, 2]=7
	faces[11, 0]=6; faces[11, 1]=8; faces[11, 2]=7   

	# creation d'un nouvel avatar rigide pour le bloc
	block = pre.rigidPolyhedron(model=mR3D, material=stone, generation_type='full',
			       vertices=vertices, faces=faces, color='REDxx')
	# ajout du bloc a l'ensemble des corps
	bodies.addAvatar(block)	
	i=i+1
	




i=0

while i< len(bodies_coords_2):

	vertices = numpy.zeros([8, 3], 'd')
	#       - sommet 1
	vertices[0, 0]=bodies_coords_2[i][0][0]
	vertices[0, 1]=bodies_coords_2[i][0][1]
	vertices[0, 2]=bodies_coords_2[i][0][2]
	#       - sommet 2
	vertices[1, 0]=bodies_coords_2[i][1][0]
	vertices[1, 1]=bodies_coords_2[i][1][1]
	vertices[1, 2]=bodies_coords_2[i][1][2]
	#       - sommet 3
	vertices[2, 0]=bodies_coords_2[i][2][0]
	vertices[2, 1]=bodies_coords_2[i][2][1]
	vertices[2, 2]=bodies_coords_2[i][2][2]
	#       - sommet 4
	vertices[3, 0]=bodies_coords_2[i][3][0]
	vertices[3, 1]=bodies_coords_2[i][3][1]
	vertices[3, 2]=bodies_coords_2[i][3][2]
	#       - sommet 5
	vertices[4, 0]=bodies_coords_2[i][4][0]
	vertices[4, 1]=bodies_coords_2[i][4][1]
	vertices[4, 2]=bodies_coords_2[i][4][2]
	#       - sommet 6
	vertices[5, 0]=bodies_coords_2[i][5][0]
	vertices[5, 1]=bodies_coords_2[i][5][1]
	vertices[5, 2]=bodies_coords_2[i][5][2]
	#       - sommet 7
	vertices[6, 0]=bodies_coords_2[i][6][0]
	vertices[6, 1]=bodies_coords_2[i][6][1]
	vertices[6, 2]=bodies_coords_2[i][6][2]
	#       - sommet 8
	vertices[7, 0]=bodies_coords_2[i][7][0]
	vertices[7, 1]=bodies_coords_2[i][7][1]
	vertices[7, 2]=bodies_coords_2[i][7][2]
	#    * connectivite des faces
	faces = numpy.zeros([12, 3], 'i')
	faces[ 0, 0]=1; faces[ 0, 1]=2; faces[ 0, 2]=3
	faces[ 1, 0]=2; faces[ 1, 1]=5; faces[ 1, 2]=3
	faces[ 2, 0]=1; faces[ 2, 1]=2; faces[ 2, 2]=6
	faces[ 3, 0]=1; faces[ 3, 1]=6; faces[ 3, 2]=4
	faces[ 4, 0]=2; faces[ 4, 1]=5; faces[ 4, 2]=8
	faces[ 5, 0]=2; faces[ 5, 1]=8; faces[ 5, 2]=6
	faces[ 6, 0]=5; faces[ 6, 1]=3; faces[ 6, 2]=7
	faces[ 7, 0]=5; faces[ 7, 1]=7; faces[ 7, 2]=8
	faces[ 8, 0]=1; faces[ 8, 1]=3; faces[ 8, 2]=7
	faces[ 9, 0]=1; faces[ 9, 1]=7; faces[ 9, 2]=4
	faces[10, 0]=4; faces[10, 1]=6; faces[10, 2]=7
	faces[11, 0]=6; faces[11, 1]=8; faces[11, 2]=7   

	# creation d'un nouvel avatar rigide pour le bloc
	block = pre.rigidPolyhedron(model=mR3D, material=stone, generation_type='full',
			       vertices=vertices, faces=faces, color='REDxx')
	block.imposeDrivenDof(component=[1],dofty='vlocy',description='evolution',evolutionFile='vel_processed.dat')
	# ajout du bloc a l'ensemble des corps
	bodies.addAvatar(block)	
	i=i+1












### initialisation de l'angle de debut du prochain bloc
##theta = 0.
### pour chaque bloc
##for i in range(0, nb_blocs):
##   #    * coordonnees des sommets (repere global)
##   vertices = numpy.zeros([8, 3], 'd')
##   #       - sommet 1
##   vertices[0, 0]=r_int*math.cos(theta + theta_bloc)
##   vertices[0, 1]=-0.5*e_bloc
##   vertices[0, 2]=r_int*math.sin(theta + theta_bloc)
##   #       - sommet 2
##   vertices[1, 0]=r_int*math.cos(theta)
##   vertices[1, 1]=-0.5*e_bloc
##   vertices[1, 2]=r_int*math.sin(theta)
##   #       - sommet 3
##   vertices[2, 0]=r_int*math.cos(theta)
##   vertices[2, 1]= 0.5*e_bloc
##   vertices[2, 2]=r_int*math.sin(theta)
##   #       - sommet 4
##   vertices[3, 0]=r_int*math.cos(theta + theta_bloc)
##   vertices[3, 1]= 0.5*e_bloc
##   vertices[3, 2]=r_int*math.sin(theta + theta_bloc)
##   #       - sommet 5
##   vertices[4, 0]=r_ext*math.cos(theta + theta_bloc)
##   vertices[4, 1]=-0.5*e_bloc
##   vertices[4, 2]=r_ext*math.sin(theta + theta_bloc)
##   #       - sommet 6
##   vertices[5, 0]=r_ext*math.cos(theta)
##   vertices[5, 1]=-0.5*e_bloc
##   vertices[5, 2]=r_ext*math.sin(theta)
##   #       - sommet 7
##   vertices[6, 0]=r_ext*math.cos(theta)
##   vertices[6, 1]= 0.5*e_bloc
##   vertices[6, 2]=r_ext*math.sin(theta)
##   #       - sommet 8
##   vertices[7, 0]=r_ext*math.cos(theta + theta_bloc)
##   vertices[7, 1]= 0.5*e_bloc
##   vertices[7, 2]=r_ext*math.sin(theta + theta_bloc)
##   #    * connectivite des faces
##   faces = numpy.zeros([12, 3], 'i')
##   faces[ 0, 0]=1; faces[ 0, 1]=2; faces[ 0, 2]=3
##   faces[ 1, 0]=1; faces[ 1, 1]=3; faces[ 1, 2]=4
##   faces[ 2, 0]=1; faces[ 2, 1]=2; faces[ 2, 2]=6
##   faces[ 3, 0]=1; faces[ 3, 1]=6; faces[ 3, 2]=5
##   faces[ 4, 0]=2; faces[ 4, 1]=3; faces[ 4, 2]=7
##   faces[ 5, 0]=2; faces[ 5, 1]=7; faces[ 5, 2]=6
##   faces[ 6, 0]=1; faces[ 6, 1]=4; faces[ 6, 2]=8
##   faces[ 7, 0]=1; faces[ 7, 1]=8; faces[ 7, 2]=5
##   faces[ 8, 0]=3; faces[ 8, 1]=4; faces[ 8, 2]=8
##   faces[ 9, 0]=3; faces[ 9, 1]=8; faces[ 9, 2]=7
##   faces[10, 0]=5; faces[10, 1]=7; faces[10, 2]=8
##   faces[11, 0]=5; faces[11, 1]=6; faces[11, 2]=7   
##
##   # creation d'un nouvel avatar rigide pour le bloc
##   block = pre.rigidPolyhedron(model=mR3D, material=stone, generation_type='full',
##                               vertices=vertices, faces=faces, color='REDxx')
##   # ajout du bloc a l'ensemble des corps
##   bodies.addAvatar(block)
##   
##   # actualisation de l'angle pour la contruction du 
##   # prochain bloc
##   theta += theta_bloc + theta_joint
##
# creation d'un nouvel avatar rigide pour la fondation
floor = pre.rigidPlan(axe1=5, axe2=3, axe3=0.1, center=[0.125, 2.1875, -0.1],
                      model=mR3D, material=tdur, color='FLOOR')

# condition limites : fondation bloquee
floor.imposeDrivenDof(component=[ 2, 3, 4, 5, 6], dofty='vlocy')

floor.imposeDrivenDof(component=[1],dofty='vlocy',description='evolution',evolutionFile='vel_processed.dat')

# ajout de la fondation au conteneur de corps
bodies.addAvatar(floor)
##
# definition d'une loi de contact frottant, avec pre-gap
iqsmc=pre.tact_behav(name='iqsmc', law='IQS_MOHR_DS_CLB',cohn=0, coht=300000, dyfr=0.4, stfr=0.4)
# ajout de la loi dans le conteneur de lois
tacts.addBehav(iqsmc)
##
# definition d'une table de visibilite pour le
# contact polyedre-polyedre (i.e. entre blocs)
sv = pre.see_table(CorpsCandidat='RBDY3', candidat='POLYR', colorCandidat='REDxx',
                   CorpsAntagoniste='RBDY3', antagoniste='POLYR', colorAntagoniste='REDxx',
                   behav=iqsmc, alert=e_joint)
# ajout de la table de visibilite dans le conteneur
# de tables de visibilite
svs.addSeeTable(sv)
##
### definition d'une loi de contact frottant
##iqsc0=pre.tact_behav(name='iqsc0', law='IQS_CLB', fric=0.5)
### ajout de la loi dans le conteneur de lois
##tacts.addBehav(iqsc0)
##
# definition d'une table de visibilite pour le
# contact polyedre-plan (i.e. avec la fondation)
sv = pre.see_table(CorpsCandidat='RBDY3', candidat='POLYR', colorCandidat='REDxx',
                   CorpsAntagoniste='RBDY3', antagoniste='PLANx', colorAntagoniste='FLOOR',
                   behav=iqsmc, alert=e_joint)
# ajout de la table de visibilite dans le conteneur
# de tables de visibilite
svs.addSeeTable(sv)
##
try:
  pre.visuAvatars(bodies)
except:
  pass
##
post = pre.postpro_commands()
nlgs = pre.postpro_command(name='SOLVER INFORMATIONS', step=1)
post.addCommand(nlgs)

# ecriture des fichiers de donnees pour LMGC90
pre.writeDatbox(dim, mats, mods, bodies, tacts, svs, post=post)

