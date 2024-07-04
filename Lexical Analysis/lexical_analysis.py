import spacy
nlp = spacy.load('en_core_web_sm') # Load the English Model
disallowed_character = {'_': '', '!': '', '(': '', ')': '', '/': '', '&': '', '%': '',
                        '$': '', '#': '', '@': '', '^': '', '*': '', '+': '', '-': '', '=': '',
                        '[': '', ']': '', '{': '', '}': '', ':': '', ';': '', ',': '', '?': '', '`': '',
                        '~': '', '|': '', '\n': '', '”': '', '“': '', ".": ''}
file=open("fairytale.txt","r",encoding='utf-8')
str= file.read()
doc = nlp(str)
file.close()
sentence_list= list(doc.sents)
for sentence in sentence_list:
    print ("sentence: ",sentence)
    split_sentence = sentence.text.split(' ')
    for word in split_sentence:
        for key, value in disallowed_character.items():
            if key in word:
                 i= split_sentence.index(word)
                 word=word.replace(key,value)
                 split_sentence = split_sentence[:i]+[word.replace(key,value)]+split_sentence[i+1:]
    print("words",split_sentence)