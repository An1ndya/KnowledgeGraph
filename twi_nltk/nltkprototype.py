import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer


def count_word_freq_except_stopword():
    text = None
    with open('output/out.txt', 'r') as content_file:
        text = content_file.read()
    content_file.close()

    f = open('output/out2countwordfreq.txt', 'w')
    tokens = [t for t in text.split()]
    clean_tokens = tokens[:]
    sr = stopwords.words('english')
    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)
    freq = nltk.FreqDist(clean_tokens)
    for key, val in freq.items():
        # print(str(key) + ':' + str(val))
        f.write(str(key) + ':' + str(val)+'\n')
    f.close()
    freq.plot(20, cumulative=False)
    return


def tokenize_text():
    text = None
    with open('output/out.txt', 'r') as content_file:
        text = content_file.read()
    content_file.close()
    # mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
    # print(sent_tokenize(mytext))
    # print("######\n")
    f = open('output/out3tokenize.txt', 'w')
    myList = word_tokenize(text)
    for i in myList:
        f.write(i+'\n')
    f.close()
    # print(word_tokenize(text))
    return myList


def my_lemmatize(word, part_of_speech):  # word == "playing", pos = "v" , "n" , "a", "r"
    lemmatizer = WordNetLemmatizer()
    # print(lemmatizer.lemmatize('increases'))
    s = lemmatizer.lemmatize(word, pos=part_of_speech)
    print(s)
    return s
