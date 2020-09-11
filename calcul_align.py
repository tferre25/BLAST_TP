

def search_seq(dict_kmer, dict_seq):
	dict_score = {}
	for cles in dict_kmer.keys():
		line = dict_kmer[cles]
		for rang in range(0,len(line)-1):
			if line[rang][0] != 1:
				return
			for second_rang in range(rang+1,len(line)-1):
				if line[rang][0]!=line[rang+1][0]:
					seq_first = line[rang]
					seq_second = line[rang+1]
					list_fin = find_kmer(dict_seq, seq_first, seq_second)
					print("diff")
					nom = string(list_fin[0])+"/"+string(list_fin[1])
					dict_score[nom] = dict_score[nom].append(list_fin[2])

	return(dict_score)


		#print(len(line))

def find_kmer(dict_seq, seq_first, seq_second):
	pos1 = seq_first[1]
	pos2 = seq_second[1]
	pos1bis = seq_first[1]
	pos2bis = seq_second[1]

	qwery = dict_seq[seq_first[0]]
	compar = dict_seq[seq_second[0]]

	score = 3
	score_max = score

	while (score > 2 | pos1bis > 1 | pos1 < len(qwery)-1 
	| pos2bis > 1 | pos2 < len(compar)-1):
		if qwery[pos1+1] == compar[pos2+1]:
			score += 1 
		else:
			score -= 1
		if qwery[pos1bis-1] == compar[pos2bis-1]:
			score += 1 
		else:
			score -= 1

		if score>score_max:
			score_max = score
		pos1 +=1
		pos2 +=1
		pos1bis -= 1
		pos2bis -= 1

	return(qwery, compar, score_max)



if __name__ == '__main__':
	dict_kmer = {0 : ((1,4),(2,5),(7,9),(1,0)),
				 1 : ((3,6),(7,2)) }
	search_seq(dict_kmer, dict_kmer)