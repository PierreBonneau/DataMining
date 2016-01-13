# -*- coding: cp1252 -*-
import os
from Bio import Phylo
from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline

f1 = open('groupes.csv', 'r') # fichier de groupes générés par les keywords
f2 = open('uniprot_riz.xml', 'r')
f3 = open('uniprot_tomate.xml', 'r')

i = 1

groupes = {}
organism = ""

# implémenter la lecture du fichier

for key in groupes.keys() :
    fgroupe = open("sequences_groupe"+i+".fasta", 'w')
    for i in groupes[key] :
        #récupérer l'organisme (tomate ou riz)
        if organism == 'tomate' :
            for record in SeqIO.parse(f3, 'uniprot-xml') :
                if record.name == i :
                    fgroupe.write(">Solanum|"+str(record.name)+"\n"+str(record.seq)+"\n\n")
        if organism == 'riz' :
            for record in SeqIO.parse(f2, 'uniprot-xml') :
                if record.name == i :
                    fgroupe.write(">Oriza|"+str(record.name)+"\n"+str(record.seq)+"\n\n")
    i += 1
                
##clustalw_exe = r"/net/cremi/mlopez001006/Bureau/clustalw2"
##
##clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fich+".fasta")
##
###print clustalw_cline.matrix
##
##print clustalw_cline()
##
##assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
##stdout, stderr = clustalw_cline()
##tree = Phylo.read(fich+".dnd", "newick")
##Phylo.draw_ascii(tree)
