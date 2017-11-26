#!/usr/bin/python3
import string
from collections import defaultdict
from collections import OrderedDict

# loop through all documents
list_of_documents = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt", "doc5.txt", "doc6.txt"]

# map to keep all the counts of words and sentences of those particular words.
word_count = {}
word_sentences = defaultdict(list)
word_documents = defaultdict(list)

for documents in list_of_documents:
    # get all the contents of a particular file
    with open(documents, 'r', encoding="utf8") as textFile:

            # holds the complete sentence.
            complete_sentence = ""
            # list of sentences
            stored_sentences = []

            # get a specific line of a specific file
            for line in text_file:
                # step one: get all the sentences and match to a particular word.

                # split sentence based on punctuations that ends a sentence.
                for sentence in line.lower().split('.') or line.lower().split('?') or line.lower().split(';'):
                    if sentence and not sentence.isspace():
                        stored_sentences.append(sentence)
                        complete_sentence = sentence

                        # remove all punctuations and make all the words lowercase
                        translator = line.maketrans('', '', string.punctuation)
                        line = line.translate(translator).lower()

                        # get individual word.
                        for word in line.split():
                            if word in word_count:
                                word_count[word] += 1
                            else:
                                word_count[word] = 1

                            if word in complete_sentence:
                                if not any(complete_sentence in s for s in word_sentences[word]):
                                    word_sentences[word].append(complete_sentence)
                                if not any(documents in s for s in word_documents[word]):
                                    word_documents[word].append(documents)

                        complete_sentence = ""



print('----------------------------------------------------------')
print('                      most common occurring words         ')
print('----------------------------------------------------------')
word_count = OrderedDict(sorted(word_count.items(), key=lambda t: t[1]))

word_count = list(word_count.items())
word_count.reverse()
for i in word_count[:5]:
    print(str(i[0]))
    print(str(word_sentences[str(i[0])]))
    print(str(word_documents[str(i[0])]))
    print('\n\n')
