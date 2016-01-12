from parser_keywords import parser
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
	input_file = open('../tables/test.csv', 'r')
	cat = count_kw(dict_, input_file)
	output_file = open('../count_cat.csv', 'w')
	for key in cat:
		line = key + " : " + str(cat[key]) + "\n"
		output_file.write(line)

	keywlist.flush()
	keywlist.close()
	input_file.flush()
	input_file.close()
	output_file.flush()
	output_file.close()