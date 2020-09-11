

def search_seq(dict_kmer, dict_seq):
	dict_score = {}
	for cles in dict_kmer.keys():
		line = dict_kmer[cles]
		#print(len(line))
		#print(line)
		for rang in range(0,len(line)-1):
			if line[rang][0] == 1:
				
				for second_range in range(rang+1,len(line)):
					

					if line[rang][0]!=line[second_range][0]:
						seq_first = line[rang]
						seq_second = line[second_range]
						list_fin = find_kmer(dict_seq, seq_first, seq_second)
						#print(list_fin)
						#print("diff")
						nom = str(list_fin[0])+"/"+str(list_fin[1])

						temp = []
						if (nom in dict_score):
							print("deja")
							print(nom)
							print(dict_score[nom])
							temp = list(dict_score[nom])
						else:
							print("apparition")
							print(nom)
							dict_score[nom] = []
						#temp = list(dict_score[nom])
						#dict_score[nom] = temp.append(list_fin[2])

						dict_score[nom] = temp.append(list_fin[2])
			else:
				break
	#print(dict_score)
	return(dict_score)


		

def find_kmer(dict_seq, seq_first, seq_second):
	pos1 = seq_first[1]
	pos2 = seq_second[1]
	pos1bis = seq_first[1]
	pos2bis = seq_second[1]

	qwery = dict_seq[seq_first[0]]
	compar = dict_seq[seq_second[0]]

	score = 3
	score_max = score

	y = 0
	for x in range(0,min(len(qwery), len(compar))):
		#print("FAIT")
		if x%2 == 0:
			y = -y-1
		else:
			y = -y+1


		if ((pos1+y < 1) or pos1+y > (len(qwery)-1) or (pos2+y < 1) or pos2+y > (len(compar)-1)):
			#print("stoppppppppp")
			break
		else:
			print(pos1+y, pos2+y)
			if qwery[pos1+y] == compar[pos2+y]:
				score += 1 
			else:
				score -= 1
			pos1 = pos1+y
			pos2 = pos2+y
		if score>score_max:
			score_max = score

		
	'''
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
	'''
	return(seq_first[0], seq_second[0], score_max)



if __name__ == '__main__':
	dict_kmer = {0 : ((1,4),(2,5),(7,9),(1,0)),
				 1 : ((3,6),(7,2)) }
	search_seq(dict_kmer, dict_kmer)