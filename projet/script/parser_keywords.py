def parser(file):
	kw = ''
	cat = ''
	kw_category = {}
	for line in keywlist:
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


if __name__ == '__main__':
	input_file = "keywlist.txt"
	keywlist = open(input_file, "r")
	dict_ = parser(keywlist)
	kw_cat_file = open('kw_cat_file.txt', 'w')
	for key in dict_:
		line = key + " : " + dict_[key] + "\n"
		kw_cat_file.write(line)
	keywlist.flush()
	keywlist.close()
	kw_cat_file.flush()
	kw_cat_file.close()