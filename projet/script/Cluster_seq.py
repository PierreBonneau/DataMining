# -*- coding: cp1252 -*-
import os
from Bio import Phylo
from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline

#nb = 0
fich = "./fasta/sequences_groupe1"
groupes = {}
organism = ""

def extraction_grp(j):
    org = 0
    grp = {}
    f1 = open('./../tables/cluster'+str(j)+'.csv', 'r')
    data = f1.readlines()
    for lignes in data :
        lignes = lignes.split(";")
        if lignes[2] == "Oryza sativa subsp. japonica (Rice)\n" :
            org = 0 # 0 pour le riz
        elif lignes[2] == "Solanum lycopersicum (Tomato)\n" :
            org = 1 # 1 pour la tomate
        grp[lignes[0]] = org

    return grp
        
for j in range(0,6) :
	groupes = extraction_grp(j)
    	fgroupe = open("./fasta/sequences_groupe"+str(j)+".fasta", 'w')
    	for i in groupes.keys():
        	if groupes[i] == 1:
			f3 = open('uniprot_tomate.xml', 'r')
			for record in SeqIO.parse(f3, 'uniprot-xml') :
                		if record.name == i :
                    			fgroupe.write(">Solanum|"+str(record.name)+"\n"+str(record.seq)+"\n\n")
        		f3.close()
		elif groupes[i] == 0:
			f2 = open('uniprot_riz.xml', 'r')
			for record in SeqIO.parse(f2, 'uniprot-xml') :
				if record.name == i :
					fgroupe.write(">Oriza|"+str(record.name)+"\n"+str(record.seq)+"\n\n")
    			f2.close()
	#nb += 1
    	fgroupe.close()


"""                
clustalw_exe = r"/net/cremi/mlopez001006/Bureau/clustalw2"

clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fich+".fasta")

assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
stdout, stderr = clustalw_cline()
tree = Phylo.read(fich+".dnd", "newick")
Phylo.draw_ascii(tree) """
