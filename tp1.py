# Travail Pratique 1 - Alexandre Binette (p1206582)

### S'il vous plaît, regardez le courriel que j'ai envoyé concernant la remise du travail. Merci beaucoup!

import sys
import gzip
from collections import Counter

def read_file(fn):
    """Parses a (simplified) genotyping array annotation file (from Illumina).

    Args:
    fn (str): the name of the file (relative or absolute path).

    This function returns an iterable (one line at a time).

    """
    with gzip.open(fn, "rt") as f:
        for line in f:
            yield line.rstrip()

# Importe le fichier FASTA au sys.argv, attrape l'erreur de path et de fichier manquant

try:
    file = sys.argv[1]
except (IOError,IndexError):
    print ("Error : Fasta sequence file missing at argv[1], please specify filepath",file=sys.stderr)
    exit()


marq_count = 0
count_chrom = {}

for line in read_file(file):
    #for loop faisant passer toutes les lignes du fichier

    if line == 'Name,Chromosome,Position':
        # Permet à la ligne décrivant les colonnes de ne pas être comptée
        continue

    # Sépare les éléments des lignes par le nom, le chromosome et la position
    line_split = line.split(",")
    name = line_split[0]
    chromosome = line_split[1]
    position = line_split[2]

    # Conteur des marqueurs
    marq_count += 1

    if chromosome not in count_chrom:
        count_chrom[chromosome] = 0

    count_chrom[chromosome] += 1

    # Vérifie les propriétés du marqueur rs7139811 dans la séquence
    if name == "rs7139811":
        marq_rs7139811 = [name,chromosome,position]





#Imprime le nombre de marqueurs totaux (Question 1)
print("There are %d markers in total" % (marq_count))

#Imprime la valeur du chromosome avec le plus grand nombre de marqueurs (Question 2)
count = Counter(count_chrom.values()).most_common(1)[0]
print("The chromosome with the highest number of markers is chromosome %d with %d markers" % (count[1], count[0]))

#Imprime les propriétés du marqueur rs7139811 (Question 4)
print("%s is located at position %s on chromosome %s" % (marq_rs7139811[0],marq_rs7139811[1],marq_rs7139811[2]))
