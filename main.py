import julien as jl
import prep_database as pd
import score as sc
import calcul_align as ca
import e_value as ev
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Querry_file", help = "Fasta Database file ", type=str)
parser.add_argument("Database_file", help = "Fasta Database file ", type=str)
args = parser.parse_args()

database_fd = pd.prep_data(args.Querry_file , args.Database_file)
print("ferdinand fini")
#print(database_fd)
database_jl = jl.kmer_to_dict(database_fd)
print("julien fini")
#print(database_jl)
database_ml = ca.search_seq(database_jl, database_fd)
print("mael raté")
sc.score(database_ml)
print("laetitia survivante")

