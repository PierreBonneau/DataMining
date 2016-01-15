import os
from Bio import Phylo
from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline

"""
Ce script permet de générer des fichiers fasta pour des clusters déjà définis
enregistrés dans des fichiers clusterX.csv
Retourne des fichiers sequences_clusterX.fasta
"""

for i in range(15):
	i_file_name = '../tables/cluster'+str(i)+'.csv'
	input_file = open(i_file_name, 'r')
	prot_per_organism = {}

	for line in input_file:
		line = line.rstrip('\n')
		words = line.split(';')

		if words[2] not in prot_per_organism.keys():
			prot_per_organism[words[2]] = []
			prot_per_organism[words[2]].append(words[0])
		else:
			prot_per_organism[words[2]].append(words[0])
	input_file.flush()
	input_file.close()
	o_file_name = 'sequences_cluster'+str(i)+'.fasta'
	result_file = open(o_file_name, 'w')
	for k in prot_per_organism.keys():
		if k == "Oryza sativa subsp. japonica (Rice)":
			riz_file = open('uniprot_riz.xml', 'r')
			for record in SeqIO.parse(riz_file, 'uniprot-xml'):
				if record.name in prot_per_organism[k]:
					result_file.write(">Oriza|"+str(record.name)+"\n"+str(record.seq)+"\n\n")
			riz_file.flush()
			riz_file.close()
		else:
			tom_file = open('uniprot_tomate.xml', 'r')
			for record in SeqIO.parse(tom_file, 'uniprot-xml'):
				if record.name in prot_per_organism[k]:
					result_file.write(">Solanum|"+str(record.name)+"\n"+str(record.seq)+"\n\n")
			tom_file.flush()
			tom_file.close()
	result_file.flush()
	result_file.close()