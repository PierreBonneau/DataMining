import sys
from Bio import SeqIO
     
def gen_files(proteomes):
	#Creation des fichiers correspondants aux tables
	proteine = open('../tables/proteine.csv', 'w')
	proteine.write('id; id_interaction; id_seq; id_fonction; nom\n')
	interaction = open('../tables/interaction.csv', 'w')
	interaction.write('id_interact; sub-unit\n')
	sequence = open('../tables/sequence.csv', 'w')
	sequence.write('id_seq; longueur; masse; sequence\n')
	fonction = open('../tables/fonction.csv', 'w')
	fonction.write('id_fonction; catalytic activity\n')
	family = open('../tables/famille.csv', 'w')
	family.write('id; similarity\n')
	taxonomy = open('../tables/taxonomie.csv', 'w')
	taxonomy.write('nom; nom_du_gene; organisme; existence_proteine\n')

	#Parsage du fichier xml et ecriture dans les fichiers adequats
	id_prot = 0
	for p in range(len(proteomes)):
		proteome = open(proteomes[p], 'r')
		print proteomes[p]
		for record in SeqIO.parse(proteome, 'uniprot-xml'):
			nom = str(record.name)
			id_interact = "I"+str(id_prot)
			id_seq = "S"+str(id_prot)
			id_func = "FU"+str(id_prot)

			#Ecriture dans proteine.csv
			proteine.write(str(id_prot) +'; '+ id_interact +'; '+ id_seq +'; '+ id_func +'; '+ nom + '\n')

			#Ecriture dans interaction.csv
			if record.annotations.has_key('comment_subunit'):
				subunit = ''
				for su in range(len(record.annotations['comment_subunit'])):
					if su == len(record.annotations['comment_subunit'])-1:
						subunit = subunit + str(record.annotations['comment_subunit'][su])
					else:
						subunit = subunit + str(record.annotations['comment_subunit'][su]) + ", "
			else:
				subunit = 'None'
			interaction.write(id_interact +'; '+ subunit + '\n')

			#Ecriture dans sequence.csv
			masse = int(record.annotations['sequence_mass'])
			longueur = int(record.annotations['sequence_length'])
			#seq = str(record.format("fasta"))
			seq = str(record.seq)
			sequence.write(str(id_seq) +'; '+ str(longueur) +'; '+ str(masse) +'; '+ seq + '\n')

			#Ecriture dans fonction.csv
			if record.annotations.has_key('comment_catalyticactivity'):
				cat_act = ""
				for ca in range(len(record.annotations['comment_catalyticactivity'])):
					if ca == len(record.annotations['comment_catalyticactivity'])-1:
						cat_act = cat_act + str(record.annotations['comment_catalyticactivity'][ca])
					else :
						cat_act = cat_act + str(record.annotations['comment_catalyticactivity'][ca]) + ", "
			else:
				cat_act = "None"
			fonction.write(id_func +'; '+ cat_act + '\n')

			#Ecriture dans famille.csv
			if record.annotations.has_key('comment_similarity'):
				sim = ""
				for s in range(len(record.annotations['comment_similarity'])):
					if s == len(record.annotations['comment_similarity'])-1:
						sim = sim + str(record.annotations['comment_similarity'][s])
					else:
						sim = sim + str(record.annotations['comment_similarity'][s]) + ", "
			else:
				sim = "None"
			family.write(str(id_prot) +'; '+ sim + '\n')

			#Ecriture dans taxonomie.csv
			orga = str(record.annotations['organism'])
			exist = str(record.annotations['proteinExistence'])
			if record.annotations.has_key('gene_primary_name'):
				gene = ""
				for g in range(len(record.annotations['gene_primary_name'])):
					if g == len(record.annotations['gene_primary_name'])-1:
						gene = gene + str(record.annotations['gene_primary_name'][g])
					else:
						gene = gene + str(record.annotations['gene_primary_name'][g]) + ", "
			else:
				gene = 'None'
			taxonomy.write(nom +'; '+ gene +'; '+ orga +'; '+ exist + '\n')

			id_prot = id_prot + 1
		proteome.flush()
		proteome.close()
	proteine.flush()
	proteine.close()
	interaction.flush()
	interaction.close()
	sequence.flush()
	sequence.close()
	fonction.flush()
	fonction.close()
	family.flush()
	family.close()
	taxonomy.flush()
	taxonomy.close()

if __name__ == '__main__':
	proteomes = ["uniprot_riz.xml", "uniprot_tomate.xml"]
	# if len(sys.argv) == 0:
	# 	print "Donnez le(s) proteome(s) en arguments"
	# else:
	# 	for arg in sys.argv:
	# 		proteomes.append(str(arg))
	# 	gen_files(proteomes)
	gen_files(proteomes)
