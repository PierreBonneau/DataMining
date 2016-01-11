import re
from Bio import SeqIO

def parse_RE(myfile):
	content= myfile.read()
	lines= content.split("\n")
	dictkeys =  {}
	for i in lines:
		match = re.match("<.*?>", i)
		if match != None:
			key = match.group(0)
			if key not in dictkeys:
				dictkeys[key] = 1
				print key
			else:
				dictkeys[key] = dictkeys[key]+1
	return dictkeys

# def parse_Bio():
# 	for record in SeqIO.parse(f, ''):
# 		print record.dir()


if __name__ == '__main__':
	
	proteome = "/net/stockage/BioInformatique2014/Lebonrepertoire/uniprot_riz.xml"
	myfile=open(proteome)
	of = open("outputfile.txt", "w")
	dictkeys = parse_RE(myfile)
	for k in dictkeys.keys():
		of.write(k)
		of.write("\n")
	of.flush()
	of.close()
	myfile.flush()
	myfile.close()
