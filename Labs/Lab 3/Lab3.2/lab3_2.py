import string
import copy

texts = []
for i in range(1,11):
  f = open(f'{i:02}.txt', 'r')
  texts.append(f.read())
  f.close()

# print(len(texts))

texts = [text.lower() for text in texts]
texts = [text.translate(str.maketrans('','', string.punctuation)) for text in texts]
texts = [text.splitlines() for text in texts]
texts = [[sentence for sentence in text if sentence] for text in texts]
# TODO KOM PÅ ATT JAG NU DELAR PÅ RADER ISTÄLLET FÖR MENINGAR

# # Store the words as elements in an array for each of the texts
# texts_words = [text.split() for text in texts]

# Replacing the words with numbers and storing the words in a dictionary
texts_numbers = copy.deepcopy(texts);
dictionary = {}
dict_counter = 0
for text in texts_numbers:
  for i in range(len(text)):
    sentence = text[i]
    word_indices = []
    for curr_word in sentence.split():
      if curr_word in dictionary:
        word_indices.append(str(dictionary[curr_word]))
      else:
        dictionary[curr_word] = dict_counter
        word_indices.append(str(dict_counter))
        dict_counter += 1
    text[i] = ' '.join(word_indices)


# Compare the sequences
for idx1, text1 in enumerate(texts_numbers):
  for idx2, text2 in enumerate(texts_numbers):
    # print(f'\t{idx1} {idx2}')
    if text1 == text2:
      continue
    i = 0
    for sentence1 in text1:
      i += 1
      if sentence1 in text2:
        # print(i)
        print(texts[idx1][i])
    #   for sentence2 in text2:

        






#__________________________
# texts = [text.lower() for text in texts]
# texts = [text.translate(str.maketrans('','', string.punctuation)) for text in texts]
# texts = [text.replace('\n', ' ') for text in texts]

# # Store the words as elements in an array for each of the texts
# texts_words = [text.split() for text in texts]

# # Replacing the words with numbers and storing the words in a dictionary
# dictionary = {}
# dict_counter = 0;
# for words in texts_words:
#   for i in range(len(words)):
#     curr_word = words[i]
#     if curr_word in dictionary:
#       words[i] = dictionary[curr_word]
#     else:
#       dictionary[curr_word] = dict_counter
#       words[i] = dict_counter
#       dict_counter += 1

# # Compare the sequences
# # I'm really not sure how to do this efficiently

# # for text1 in texts_words:
# #   for text2 in texts_words:
# #     for text1_word in text1:
# #       for text2_word in text2:
        

# # Eg kanske man skulle dela upp i meningar?


# print(texts_words[0])
# print(len(texts_words[0]))