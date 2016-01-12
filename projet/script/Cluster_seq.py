import os
from Bio import Phylo

table_seq = open("./../tables/sequence2.csv", "r")
fichout = open("./../tables/sequences.fasta", "w")
data = table_seq.readlines()
del data[0]

print "taille", len(data)
test = 0
mot = ""
donnees =[]
for i in data :
    print "i", i
    i = i.split(";")
    fichout.write(">"+i[0]+i[3]+"\n")

fichout.close()
table_seq.close()

from Bio.Align.Applications import ClustalwCommandline

clustalw_exe = r"/net/cremi/mlopez001006/Bureau/clustalw2"

clustalw_cline = ClustalwCommandline(clustalw_exe, infile="./../tables/sequences.fasta")

print clustalw_cline.matrix

print clustalw_cline()

assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
stdout, stderr = clustalw_cline()
tree = Phylo.read("sequences.dnd", "newick")
Phylo.draw_ascii(tree)
                
