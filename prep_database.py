import argparse


def prep_data(querry, database):
	kmere_base={}
	tmpList = []
	#Lecture du fichier querry
	with open(querry, "r") as querry:
		lines = querry.readlines()
		seq=""
		for line in lines:
			if line.startswith(">"):
				continue
			else: 
				seq=seq+line.strip()
		for i in range(0, len(seq)):
			if i+3>len(seq):
				continue
			else : 
				tmpList.append(seq[i:i+3])
	
	kmere_base[1] = tmpList
	print("Querry :")
	print(kmere_base)
	x=1
	seq="" #Tmp str using to merge multiple line of a sigle sequence
	with open(database, "r") as fillin:
		lines = fillin.readlines()
		for line in lines:

			if line.startswith(">"):
				if seq!="":
					tmpList=[] #tempory list stocking kmere
					x+=1 #incrementing index of dict
					for i in range(0, len(seq)): #calculing kmere
						if i+3>len(seq):
							continue
						else : 
							tmpList.append(seq[i:i+3])
					kmere_base[x]=tmpList
				seq=""
				#print(x)
				continue
			else: 
				seq = seq+line.strip() #merge multiple line of the same sequence		
	print(kmere_base)
	return kmere_base


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("Querry_file", help = "Fasta querry file ", type=str)
	parser.add_argument("Database_file", help = "Fasta Database file ", type=str)
	args = parser.parse_args()

	if args.Database_file[-6:] != '.fasta' or args.Querry_file[-6:] != '.fasta': #Vérification de l'extension pdb
		print("Please select file with fasta extension")
	else: 
		database = prep_data(args.Querry_file , args.Database_file)
