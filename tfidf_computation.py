import sys
import os
import shutil
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
import pandas as pd
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

REVIEW_DIR = "review_text"
REVIEW_FILE = REVIEW_DIR + "/" + "product_user_review.txt"

OUTPUT_FILE = "tfidf_sklearn_user_unibi.txt"


if __name__ == "__main__":

    # Loading the reviews file
    fp = open(REVIEW_FILE, "rb")

    mydoclist1 = []
    myfilelist = []

    for line in fp:
        row2 = line.split("~")

        col = 0
        for cell in row2:

        # This field is for comment-id information
            if col == 1:
                filename = unicode(row2[col])
                print "Reading from excel file, fileid = ", filename

        # This is for COMMENT information
            if col == 10:
                text = row2[col]

                text2 = ""
                # Adding the string text separated by "\t"
                for temp in text.split("\t"):
                    if len(temp.strip()) > 3:
                        text2 += temp.strip() + " "
                comment = text2

            col += 1

    if comment is not None:
        # Making a list of all the reviews and file id-s
        myfilelist.append(filename)
        mydoclist1.append(comment)
    print 'the total number of documnts are', len(mydoclist1)

    # Making the term-frequency matrix
    # See the documentation of the function here
    # http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
    count_vectorizer = CountVectorizer(lowercase="True", stop_words='english',
                                       min_df=100, ngram_range=(1, 2))
    tf_matrix = count_vectorizer.fit_transform(mydoclist1)

    # Computing the idf scores of all the terms
    # http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html
    tfidf = TfidfTransformer(norm="l1")
    tfidf.fit(tf_matrix)

    # outputting the the tf-idf values
    tf_sum = np.sum(tf_matrix.todense(), axis=0)
    tf_sum1 = np.array(tf_sum)

    idf_values = tfidf.idf_

    with open(OUTPUT_FILE, "wb") as fp:
        print >> fp, "word", "\t", "tf_score", "\t", "idf_score"

        for num in zip(count_vectorizer.get_feature_names(),
                       list(tf_sum1[0]), list(idf_values)):

            # Writing the tf, idf, tf*idf values to txt file
            print >> fp, num[0].encode('utf-8'), "\t",
            print >> fp, num[1], "\t", num[2], "\t", num[1]*num[2]
