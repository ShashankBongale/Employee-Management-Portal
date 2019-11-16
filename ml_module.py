import pandas as pd
import numpy as np
import json
import re

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

from sklearn.linear_model import SGDClassifier

import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import StanfordNERTagger

import warnings
warnings.filterwarnings('ignore')


#text is a string ex) "This is a SE project". Returns string of only NN and NNP
def POS_remove(text):
    tokens = word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    st = ""
    for i in tagged:
        if i[1] == "NN" or i[1] == "NNP":
            st = st + " " + str(i[0])
    st = st.strip()    
    return st
  
#stop words removal, lower case, punctutations
def pre_process(text):
    text = POS_remove(text)  
    text=text.lower()
    text = re.sub(r'\d+', '', text)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in text:
        if char not in punctuations:
            no_punct = no_punct + char
    
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(no_punct)
    text = [i for i in tokens if not i in stop_words]
    #lemmatizer=WordNetLemmatizer()
    st = ""
    for word in text:
        #st = st + " " +lemmatizer.lemmatize(word)
        st = st + " " +word
    text = st.strip()
    st =""
    for ch in text:
        if(ch.isalpha() or ch == ' '):
            st = st + ch
    return st


