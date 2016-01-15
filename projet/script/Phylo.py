#-*- coding: cp1252 -*-
import os
from Bio import Phylo
from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline

""" Prend en paramètre un fichier fasta et renvoi en sortie standard un arbre phylogénique
Nécessite l'utilisation de Clustalw qu'il faut installer en local"""

fich = "./results/sequences_cluster1.fasta" # Fichier input correspondant à un fichier fasta 

                
clustalw_exe = r"/net/cremi/login/Bureau/clustalw2" # lien vers le programme clustalw

clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fich)

assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
stdout, stderr = clustalw_cline()
tree = Phylo.read(fich+".dnd", "newick")
Phylo.draw_ascii(tree) 
