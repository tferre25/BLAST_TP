

def score(fichier):
	dict1 = {}
	for key in fichier:
		dict1[key] = max(fichier[key])
	return dict1


# programme principal
dico = {"0/1" : [7,-3,10], "0/2": [2,-4,16]}
S = score(dico)
print(S)

