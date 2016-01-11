# -*- coding: cp1252 -*-

from Bio import SeqIO
tab={}
f = open('uniprot_riz.xml', 'r')
res=open("Resume2.txt",'w')
res2=open("Comptage2.txt",'w')
i = 0
for record in SeqIO.parse(f, 'uniprot-xml'):
        res.write("Protéine n°"+str(i)+"   "+str(record.name)+"\n")

        res.write("Features : \n"+str(record.features)+"\n")
        res.write("Description : \n"+str(record.description)+"\n")
        res.write("Annotations : \n"+str(record.annotations)+"\n")
        tt = False
        for annot in record.annotations :
                #print "annot : ", annot
                for cle in tab.keys() :
                       # print "clé : ", cle
                        if annot == cle :
                                tab[annot] += 1
                                tt = True
                                break
                        else :
                                tt = False
                if tt == False :
                        tab[annot]=1
        res.write("\n\n")
        i += 1

for j in tab.items() :
        res2.write(str(j)+"\n")
                
