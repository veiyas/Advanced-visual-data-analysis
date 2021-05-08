import string
import copy
import nltk.data
from nltk.tokenize import PunktSentenceTokenizer


def remove_punctuation(sentence_list):
  return [sentence.translate(str.maketrans('','', string.punctuation)) 
          for sentence in sentence_list]

def make_lower(sentence_list):
  return [sentence.lower() for sentence in sentence_list]

def replace_words_with_numbers(texts):
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
  return dictionary
  

texts = []
for i in range(1,11):
  f = open(f'{i:02}.txt', 'r')
  texts.append(f.read())
  f.close()

texts = [text.replace('\n', ' ') for text in texts]

# Divide text into sentences
nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
texts = [tokenizer.tokenize(text) for text in texts]

texts = [remove_punctuation(sentences) for sentences in texts]
texts = [make_lower(sentences) for sentences in texts]

# Replacing the words with numbers and storing the words in a dictionary
texts_numbers = copy.deepcopy(texts)
dictionary = replace_words_with_numbers(texts_numbers)

# Compare the sequences
print('\n\nMatches found')
print('=============')
for idx1 in range(len(texts_numbers)-1):
  text1 = texts_numbers[idx1]
  for idx2 in range(idx1+1, len(texts_numbers)):
    text2 = texts_numbers[idx2]
  
    if text1 == text2:
      continue

    for i, sentence1 in enumerate(text1):
      # Skip short sentences---these are mostly just noise,
      # either so unoriginal that they are of no interest,
      # or incorrectly split by the sentence tokenization
      if len(sentence1.split()) <= 4:
        continue

      try:
        text2_find_sentence_idx = text2.index(sentence1)
        print(f'[between text {idx1+1} and {idx2+1}] {texts[idx1][i]}')
        # print(f'[Match between text {idx1+1} and {idx2+1}] {texts[idx1][i]}  ===  {texts[idx2][text2_find_sentence_idx]}')
        # print(f'\t= {texts[idx2][text2_find_sentence_idx]}')
      except:
        pass

