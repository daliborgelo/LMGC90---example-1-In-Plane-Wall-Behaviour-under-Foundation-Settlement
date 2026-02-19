# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 14:08:15 2025

@author: dalib
"""

import ezdxf

import os
import math

import numpy

import sys
sys.path.append("/home/dgelo/lmgc90_user_2024/build")

from pylmgc90 import pre

if not os.path.isdir('./DATBOX'):
  os.mkdir('./DATBOX')

# on se place en 2D
dim = 2

# creation des conteneurs
bodies = pre.avatars()
mats   = pre.materials()
mods   = pre.models()
svs    = pre.see_tables()
tacts  = pre.tact_behavs()

# creations de deux materiaux
brick = pre.material(name='BRICK',materialType='RIGID',density=205.)
earth = pre.material(name='EARTH',materialType='RIGID',density=205.)
mats.addMaterial(brick, earth)

# on cree un modele de rigide
mod = pre.model(name='rigid', physics='MECAx', element='Rxx2D', dimension=dim)
mods.addModel(mod)





def extract_polyline_points(dxf_file):
    # Load the DXF document
    doc = ezdxf.readfile(dxf_file)
    
    # Get the modelspace
    msp = doc.modelspace()
    
    # List to store groups of polyline points
    polyline_groups = []
    
    # Iterate through all entities in modelspace
    for entity in msp:
        if entity.dxftype() == 'LWPOLYLINE':
            # Extract points from the polyline
            points = entity.get_points()
            polyline_groups.append(points)
    
    return polyline_groups

# Example usage
dxf_file = 'zid.dxf'
polyline_groups = extract_polyline_points(dxf_file)
#for i, group in enumerate(polyline_groups):
#    print(f"Polyline {i+1}: {group}")
    
#print (polyline_groups[1305])


##vertices=numpy.zeros([4, 2], 'd')
##vertices[0, 0]=polyline_groups[0][0][0]
##print (vertices[0, 0])
##vertices[0, 1]=polyline_groups[0][0][1]
##print (vertices[0, 1])
##vertices[1, 0]=polyline_groups[0][1][0]
##print (vertices[1, 0])
##vertices[1, 1]=polyline_groups[0][1][1]
##print (vertices[1, 1])
##vertices[2, 0]=polyline_groups[0][2][0]
##print (vertices[2, 0])
##vertices[2, 1]=polyline_groups[0][2][1]
##print (vertices[2, 1])
##vertices[3, 0]=polyline_groups[0][3][0]
##print (vertices[3, 0])
##vertices[3, 1]=polyline_groups[0][3][1]
##print (vertices[3, 1])



for i in range(0,len(polyline_groups)):

    vertices=numpy.zeros([4, 2], 'd')
    vertices[0, 0]=polyline_groups[i][0][0]
    vertices[0, 1]=polyline_groups[i][0][1]
    vertices[1, 0]=polyline_groups[i][1][0]
    vertices[1, 1]=polyline_groups[i][1][1]
    vertices[2, 0]=polyline_groups[i][2][0]
    vertices[2, 1]=polyline_groups[i][2][1]
    vertices[3, 0]=polyline_groups[i][3][0]
    vertices[3, 1]=polyline_groups[i][3][1]



    block = pre.rigidPolygon(model=mod, material=brick, center=numpy.array([0., 0.]), color='REDxx', generation_type='full',vertices=vertices)

    bodies.addAvatar(block)




down_m = pre.rigidJonc(model=mod, material=earth, center=numpy.array([3., -0.25]),color='GREEN', axe1=1.0, axe2=0.25)
bodies.addAvatar(down_m)

down_m.imposeDrivenDof(component=[1, 2, 3], dofty='vlocy')


down_l = pre.rigidJonc(model=mod, material=earth, center=numpy.array([1., -0.25]),color='GREEN', axe1=1.0, axe2=0.25)
bodies.addAvatar(down_l)

down_l.imposeDrivenDof(component=[1, 2, 3], dofty='vlocy')


down_r = pre.rigidJonc(model=mod, material=earth, center=numpy.array([5., -0.25]),color='GREEN', axe1=1.0, axe2=0.25)
bodies.addAvatar(down_r)

down_r.imposeDrivenDof(component=[1, 3], dofty='vlocy')
down_r.imposeDrivenDof(component=2, dofty='vlocy',description='predefined',ct=-0.025, amp=0.0, omega=0.0, phi=0.0, rampi=1.0, ramp=0.0)

# gestion des interactions :
#   * declaration des lois
lplpl = pre.tact_behav(name='iqsc0',law='IQS_CLB_g0',fric=0.4)
tacts+= lplpl


#   * declaration des tables de visibilite
svplpl = pre.see_table(CorpsCandidat='RBDY2', candidat='POLYG', colorCandidat='REDxx',
                       CorpsAntagoniste='RBDY2', antagoniste='POLYG', colorAntagoniste='REDxx',
                       behav='iqsc0', alert=0.03)
svs+=svplpl
svpljc = pre.see_table(CorpsCandidat='RBDY2', candidat='POLYG', colorCandidat='REDxx',
                       CorpsAntagoniste='RBDY2', antagoniste='JONCx', colorAntagoniste='GREEN',
                       behav='iqsc0', alert=0.03)
svs+= svpljc


post = pre.postpro_commands()
nlgs = pre.postpro_command(name='SOLVER INFORMATIONS', step=1)
post.addCommand(nlgs)

# ecriture des fichiers
pre.writeDatbox(dim, mats, mods, bodies, tacts, svs, post=post)



##pre.visuAvatars(bodies)



   
