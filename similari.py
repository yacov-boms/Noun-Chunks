# Reading and concatenating the files
import os
import glob
os.chdir("C:/Users/Administrator/Downloads/IBM-20211028T072319Z-001/IBM")

extension = 'txt'
filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
with open('C:/Users/Administrator/SimilariFiles.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

# Main
# import packages
import spacy
nlp = spacy.load('en_core_web_lg') 
from collections import Counter

# Read the combined file
with open("C:/Users/Administrator/SimilariFiles.txt") as f:
    reviews = f.read()
    print(reviews)
# Construct Spacy Doc    
doc = nlp(reviews.lower())

# using chunk nouns - "chunks as a noun plus the words describing the noun"
chunk_list = list(doc.noun_chunks)
chunk_list = [chunk.text for chunk in list(doc.noun_chunks)]

# cleaning redundent prefixes
chunk_list_clean = []
for chunk in chunk_list:
    chunk_c = chunk
    if chunk[0:2] in ['a ','an']:
        chunk_c = chunk[2:]
    if chunk[0:3] == 'the':
        chunk_c = chunk[4:]
    chunk_list_clean.append(chunk_c)
    
# Most common noun tokens
noun_freq = Counter(chunk_list_clean)
common_nouns = noun_freq.most_common(20)
print(common_nouns)

# ('method', 69)
# ('machine learning model', 60)
# ('plurality', 57)
# ('machine learning', 55)
# ('invention', 51)
# ('system', 39)
# ('machine learning algorithm', 22)
# ('device', 21)
# ('data', 19)
# ('optimization', 18)
# ('parameters', 18)
# ('following steps', 17)
# ('hyperparameters', 17)
# ('set', 14)
# ('values', 13)
# ('methods', 13)
# ('training data', 12)
# ('performance', 12)
# ('present invention', 12)
# ('steps', 11)




