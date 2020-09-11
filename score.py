

def score(fichier):
	print(fichier)
	dict1 = {}
	for key in fichier.keys():
		dict1[key] = max(fichier[key])
	return dict1
'''
if __name__ == '__main__':
	
	# programme principal
	dico = {"0/1" : [7,-3,10], "0/2": [2,-4,16]}
	S = score(dico)
	print(S)

'''