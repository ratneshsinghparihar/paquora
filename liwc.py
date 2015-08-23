import MySQLdb
execfile("trie.py")

# open database
liwc_db = MySQLdb.connect("localhost","nlp","nlppassword","nlp")
cursor = liwc_db.cursor()
DEBUG = False
def create_trie_data_structure():
	t = StringTrie();
	
	cursor.execute("SELECT * FROM LIWC")
	liwc_data_list = cursor.fetchall()
	# generating Trie data structure
	if DEBUG:
		print "Creating Data Structure"
	for entry in liwc_data_list:
		starString = False
		if entry[0].find('*') == -1:
			starString = False
		else:
			starString = True
		withoutStar = entry[0].replace("*","")
		if DEBUG:
			print withoutStar + " " + entry[0]
			print entry[1]
		if t.has_node(withoutStar):
			dummy_list = t[withoutStar]
			dummy_list.append(entry[1])
			t.setdefault(withoutStar,dummy_list)
		else:
			dummy_list = list()
			if starString:
				dummy_list.append("*")
			dummy_list.append(entry[1])
			t.setdefault(withoutStar,dummy_list)
		if DEBUG:
			print "Print the value just added : "
			print t[withoutStar]
	return t;

def main():
	liwc_trie = create_trie_data_structure()
	if DEBUG:
		print "Printing Trie Results"
		for key in liwc_trie.keys():
		 	print key
		print "Total Number of keys in Trie = " + str(len(liwc_trie.keys()))


if __name__ == '__main__':
	main()

liwc_db.close()
