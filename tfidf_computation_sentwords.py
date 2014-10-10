import sys, os, shutil
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
##from dataclean import *
##from textcleaning import *
import pandas as pd
##from tfidf import *
from nltk import word_tokenize 
from nltk.stem import WordNetLemmatizer

REVIEW_DIR = "review_text"
REVIEW_FILE = REVIEW_DIR + "/" + "product_user_review.txt"

OUTPUT_FILE = "tfidf_sklearn_user_bi.txt"

class LemmaTokenizer(object):
     def __init__(self):
         self.wnl = WordNetLemmatizer()
     def __call__(self, doc):
         return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]

 
if __name__ == "__main__":

    ## Changing the sheet number to take read the training data 
    fp = open(REVIEW_FILE, "rb")

    mydoclist1 = []
    myfilelist = []

    for line in fp:
        
        row2 = line.split("~")
        ##print row2        
	labels = []
	col = 0
	for cell in row2:
	    ## This is for FILE-ID information 
	    if col==1:
		filename = unicode(row2[col])
		print "Reading from excel file, fileid = ", filename
				   
	    ## This is for COMMENT information
	    if col==10:
                text = row2[col] 
                ##print text
 
                text2 = ""
                for temp in text.split("\t"):
                  if len(temp.strip()) > 3:
                    text2 += temp.strip() + " "    

		comment = text2
	    col += 1
 
	if (comment!=None):
	    myfilelist.append(filename)
	    mydoclist1.append(comment)
       
    print 'the total number of documnts are', len(mydoclist1)
    
    ## Normalizing the document for removal of stopwords, etc
    ## mydoclist = textcleaning( mydoclist1 )
    mydoclist = mydoclist1     
    ##tfreq( mydoclist )

    count_vectorizer = CountVectorizer( lowercase="True", max_features=6000, ngram_range=(2, 2))
    tf_matrix = count_vectorizer.fit_transform(mydoclist)

    tfidf = TfidfTransformer(norm="l1")
    tfidf.fit(tf_matrix)         
    
    tf_sum = np.sum(tf_matrix.todense(), axis=0)
    tf_sum1 = np.array(tf_sum)

    idf_values = tfidf.idf_

    with open( OUTPUT_FILE, "wb") as fp:
      print >> fp, "word", "\t", "tf_score", "\t", "idf_score"
      for num in zip(count_vectorizer.get_feature_names(), list(tf_sum1[0]), list(idf_values)):
	print >> fp, num[0].encode('utf-8'), "\t", num[1], "\t", num[2], "\t", num[1]*num[2]
