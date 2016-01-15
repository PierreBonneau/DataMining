 """
 Ce script devait permettre de réaliser des clusters selon les keywords de chaque protéine
 Il permet la génération de la matrice de distance par rapport aux listes de keywords
 """

def get_id_in_cluster(cluster_file):
	list_id_prot = []
	for line in cluster_file:
		line = line.rstrip('\n')
		words = line.split('; ')
		list_id_prot.append(words[0])
	return list_id_prot

def get_function_id(list_id_prot, proteins_file):
	header = proteins_file.readline()
	line = proteins_file.readline()
	id_function = []
	while line != '':
		line = line.rstrip('\n')
		words = line.split('; ')
		if words[0] in list_id_prot:
			trash = list_id_prot.remove(words[0])
			id_function.append(words[3])
		line = proteins_file.readline()
	return id_function

def gen_dict_id_kw(list_id_funct, functions_file):
	header = functions_file.readline()
	line = function_file.readline()
	kw_per_prot = {}
	categories = ["biological process", "molecular function", "cellular component"]
	while line != '':
		line = line.rstrip('\n')
		words = line.split('; ')
		if words[0] in list_id_function:
			trash = list_id_funct.remove(words[0])
			kw_per_prot[words[0]] = {}
			cat_of_kw = kw_per_prot[words[0]]
			cat_of_kw[categories[0]] = words[2].split(', ')
			cat_of_kw[categories[1]] = words[3].split(', ')
			cat_of_kw[categories[2]] = words[4].split(', ')
		line = proteins_file.readline()
	return kw_per_prot

# def split_keywords(str_kw):
# 	list_keywords = str_kw.split(', ')
# 	return list_keywords

def kmean(kw_per_prot, list_of_id):
	dist_per_prot = gen_distance_matrix(kw_per_prot, list_of_id)



def dist(prot1, prot2):
	distances = []
	for cat_of_kw in prot1.keys():
		different_kw = []
		p = 0
		m = 0
		for i in range(len(prot1[cat_of_kw])):
			if prot1[cat_of_kw][i] not in different_kw:
				different_kw.append(prot1[cat_of_kw][i])
		for j in range(len(prot2[cat_of_kw])):
			if prot2[cat_of_kw][j] not in different_kw:
				different_kw.append(prot2[cat_of_kw][j])
		p = len(different_kw)
		for kw  in range(len(prot1[cat_of_kw])):
			if prot1[cat_of_kw][kw] in prot2[cat_of_kw]:
				m = m + 1
		d = (p-m)/p
		distances.append(d)
	return distances

def average_dist(cluster, distance_matrix, list_of_id_funct):
	
	sum_ = [0, 0, 0]
	for i in range(prot):
		for d in range(len(distance_matrix[i][prot])):
			sum_[d] = sum_[d] + distance_matrix[i][prot][d]
	for j in range(prot, len(distance_matrix)+1):
		for e in range(len(distance_matrix[prot][j])):
			sum_[e] = sum_[e] + distance_matrix[prot][j]
	mean = [0, 0, 0]
	for s in range(len(sum_)):
		mean[s] = sum_[s]/len(distance_matrix)
	return mean



def gen_dist_matrix(kw_per_prot, list_of_id):
	distance_matrix = []
	for prot1 in range(len(list_of_id)):
		distance_matrix[list_of_id[prot1]] = []
		for prot2 in range(prot1,len(list_of_id)):
			d = dist(list_of_id[prot1], list_of_id[prot2])
			distance_matrix.append(d)
	return distance_matrix


if __name__ == '__main__':
	list_cluster_files = [, , ,]
	proteins = open("../tables/proteine.csv", r)
	functions = open("../tables/fonction.csv", r)
	for f in list_cluster_files:
		cluster = open(f, 'r')
		list_of_id_prot = get_id_in_cluster(cluster)
		list_of_id_funct = get_function_id(list_of_id_funct, proteins)
		kw_per_prot = gen_dict_id_kw(list_id_prot, functions)
		new_clusters = kmean(kw_per_prot, list_of_id_funct)
