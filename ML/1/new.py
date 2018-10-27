import nltk
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import os
import codecs
from nltk import FreqDist
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from collections import Iterable

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r

comp_f=[]
rec_f=[]
sci_f=[]
talk_f=[]

files = list_files('/home/wishwa/COSC/ML/1/Data')
def categorize_files(files):
    for file in files:
        if "comp" in file:
            comp_f.append(file)
        elif "rec" in file:
            rec_f.append(file)
        elif "sci" in file:
            sci_f.append(file)
        elif "talk" in file:
            talk_f.append(file)
            

categorize_files(files)

comp_train,comp_test = train_test_split(comp_f, train_size=0.7,test_size=0.3, random_state=42)
rec_train, rec_test = train_test_split(rec_f, train_size=0.7,test_size=0.3, random_state=42)
sci_train, sci_test = train_test_split(sci_f, train_size=0.7,test_size=0.3, random_state=42)
talk_train,talk_test = train_test_split(talk_f, train_size=0.7,test_size=0.3, random_state=42)

def process_files(file):
    lt=[]
    wtxt = codecs.open(file,encoding='utf-8', errors='ignore').read()
    stopWords = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'[a-z,A-Z]{2,}')
    token=tokenizer.tokenize(wtxt)
    for w in token:
        w = w.translate(str.maketrans('','',string.punctuation))
        if w not in stopWords and w not in lt:
            lt.append(w.lower())
    return lt

compTrain=[]
recTrain=[]
sciTrain=[]
talkTrain=[]

for file in comp_train:
    compTrain.append(process_files(file))
for file in rec_train:
    recTrain.append(process_files(file))
for file in sci_train:
    sciTrain.append(process_files(file))
for file in talk_train:
    talkTrain.append(process_files(file))


compTest=[]
recTest=[]
sciTest=[]
talkTest=[]

for file in comp_test:
    compTest.append(process_files(file))
for file in rec_test:
    recTest.append(process_files(file))
for file in sci_test:
    sciTest.append(process_files(file))
for file in talk_test:
    talkTest.append(process_files(file))


def flatten(list):
    for i in list:
        for j in i:
            yield j

def flat_list(lst):
    lt=[]
    lt=flatten(lst)
    llt=list(lt)
    return llt


categoryList=['compTrain','recTrain','sciTrain','talkTrain','compTest','recTest','sciTest','talkTest']

l=flat_list(compTrain)
data=[]
for dt in l:
    if dt not in data:
        data.append(dt)
len(data)

def convert_to_csv_new(dataList):
    vectorizer = CountVectorizer()
    trans = vectorizer.fit_transform(l)
    features=vectorizer.get_feature_names()
    df = pd.DataFrame(trans.toarray(), columns = features)
    df.to_csv("file"+str(dataList)+".csv")
    #print(trans.toarray())

#for l in categoryList:
convert_to_csv_new(data)
#len(compTrain)



