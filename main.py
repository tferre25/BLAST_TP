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

database = prep_data(args.Querry_file , args.Database_file)
