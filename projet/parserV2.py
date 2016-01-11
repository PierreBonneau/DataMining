from Bio import SeqIO

def parse_Bio(myfile):
	dictkeys =  {}
	done = False
	for record in SeqIO.parse(proteome,'uniprot-xml'):
		for key in dir(record):
			if key not in dictkeys:
				dictkeys[key] = 1
			else:
				dictkeys[key] = dictkeys[key]+1
	return dictkeys

def get_parameters(dictkeys):
	parameters = {}
	of = open("parameters.txt", "w")
	for key in dictkeys:
		of.write("TYPE")
		of.write(key)
		if parameter not in parameters:

	of = open("parameters_annotations.txt", "w")
	for i in parameters:
		of.write(i)
		of.write("\n")
	of.flush()
	of.close()
	done = True
	return done

if __name__ == '__main__':
	
	proteome = "uniprot_riz.xml"
	myfile=open(proteome)
	of = open("outputfile2.txt", "w")
	dictkeys = parse_Bio(myfile)
	for k in dictkeys.keys():
		of.write(k)
		of.write(" ")
		of.write(str(dictkeys[k]))
		of.write("\n")
	of.flush()
	of.close()
	myfile.flush()
	myfile.close()