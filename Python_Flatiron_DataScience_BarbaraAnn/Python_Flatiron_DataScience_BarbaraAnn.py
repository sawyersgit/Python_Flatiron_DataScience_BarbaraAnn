lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"
list_of_lyrics = lyrics.split(' ')

len(list_of_lyrics)
print(list_of_lyrics)

unique_words = set(list_of_lyrics)
len(unique_words)


word_histogram = dict.fromkeys(unique_words, 0)
for word in list_of_lyrics:
    word_histogram[word] = word_histogram[word]+ 1

print(word_histogram)

