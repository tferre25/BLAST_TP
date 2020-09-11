def kmer_to_dict(dict_ferdi):
	dict_occurence = {}
	for clef in dict_ferdi:
		if clef == "1":
			for position_query, kmer_q in enumerate(dict_ferdi[clef]):
				query_list = [clef, position_query + 1]
				if kmer_q not in dict_occurence.keys():
					dict_occurence[kmer_q] = []
				dict_occurence[kmer_q].append(query_list)
		else:
			for position, kmer in enumerate(dict_ferdi[clef]):
				for kmer_query in dict_ferdi[1]:
					if kmer == kmer_query:
						match = [clef, position + 1]				
						if kmer not in dict_occurence.keys():
							dict_occurence[kmer] = []
						dict_occurence[kmer].append(match)
	return dict_occurence
	
	
	
#if __name__ == "__main__":

"""
	test = {}
	test["1"] = ["kfc", "stc", "opt", "ndp"]
	test["2"] = ["tgc", "kfc", "ndp", "jdo"]
	test["3"] = ["opd", "opt", "opm", "doz"]

	marchestp = kmer_to_dict(test)
	print(marchestp)
"""