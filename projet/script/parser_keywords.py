#Ce script permet de traiter les information du fichier keywlist.txt d'UniProt (sans son entete)
# Il permet d'associer chaque keywords à sa catégorie facilement
def parser(file_):
	kw = ''
	cat = ''
	kw_category = {}
	for line in file_:
		line = line.rstrip('.\n')
		if line == '//':
			continue
		words = line.split('   ')
		if words[0] == 'ID':
			kw = words[1]
		elif words[0] == 'CA':
			cat = words[1]
			kw_category[kw] = cat
	return kw_category
#Retourne le compte de mots-clé par catégories dans un dictionnaire
def count_kw(dict_, file_):
	entete = file_.readline()
	line = file_.readline()
	cat = {}
	while line != "":
		line = line.rstrip("\n")
		fields = line.split('; ')
		kw_list = fields[1].split(', ')
		for kw in kw_list:
			if dict_[kw] not in cat:
				cat[dict_[kw]] = 1
			else:
				cat[dict_[kw]] = cat[dict_[kw]] + 1
		line = file_.readline()
	return cat

if __name__ == '__main__':
	input_file = "../keywlist.txt"
	keywlist = open(input_file, "r")
	dict_ = parser(keywlist)
	kw_cat_file = open('../kw_cat_file.txt', 'w')
	for key in dict_:
		line = key + " : " + dict_[key] + "\n"
		kw_cat_file.write(line)
	keywlist.flush()
	keywlist.close()
	kw_cat_file.flush()
	kw_cat_file.close()