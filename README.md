# NLP Exercise  
In order to implement keyword extraction including common phrases, I used Python with Spider on Anaconda and decided to apply Spacy's **Noun Chunk** feature.
I quote "Noun chunks are “base noun phrases” – flat phrases that have a noun as their head. You can think of noun chunks as a noun plus the words describing the noun".    
After concatenating the files into a one string, I could convert it into a Spacy doc file and apply noun chunks.
I applied minor prefix cleaning, summed the friquencies and ranked them using Counter function,
And Wualla we have a ranked list of major keywords.
