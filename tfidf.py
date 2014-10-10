## code for tf-idf in python

import csv, operator, math
import string #allows for format()
import numpy as np  
import pickle
###########################################################################################################
## function to compute the term-frequency(tf) and inverse-document-frequency(idf) from a corpus of comments
###########################################################################################################

def tfreq(doclist):
    vocab = {}
    vocab_idf = {}
    NUM_DOCS = len(doclist)     
    idf_count = {}
    doc_count = {}   

    ## Code for calculating the frequency of all the terms in the corpus and storing them in dict called vocab{}
    for doc in doclist:
        for word in doc.split():
            if word.strip() in vocab:
                vocab[word.strip()] += 1                
            else:
                vocab[word.strip()] = 1
    
    ## Code for making the inverted index for all the terms in vocabulary and storing them in dict called vocab_idf{}
    for i, doc in enumerate(doclist):
        for word in doc.split():
            if word.strip() in vocab_idf:
                vocab_idf[word.strip()].append(i)
            else:
                vocab_idf[word.strip()] = [i]
    
    ## Code for computing the idf value of the terms from the inverted index
     # first converting vocab_idf to set and then making it to list
     # dict doc_count contains the count of a word appearing in that number of documents
    for word in vocab_idf.keys():
        vocab_idf[word] =  list(set(vocab_idf[word]))
        doc_count[word] = len( vocab_idf[word] )        
        idf_count[word] = np.log( float(NUM_DOCS)/float(1 + doc_count[word]) )
             
    ## Saving the idf value of words into a pickle file
    with open('idf_values.pickle', 'wb') as pfile:
        pickle.dump(idf_count, pfile)
           
    ## Sorting the dict{} which contains the term frequency information in decreasing order
    sorted_x = sorted(vocab.iteritems(), key=operator.itemgetter(1))
    sorted_x.reverse()  # it arranges the list in decreasing order of count values
  

    ## Saving the tf and idf scores in a txt file 
    with open('tf_idf.txt','w') as txtfile:
        print >> txtfile, 'word\t\t','tfcount\t', 'doc-count\t', 'idf-count'
        for word,tfcount in sorted_x:
            for word2 in idf_count.keys():
                if word2==word:
                    print >> txtfile, word, '\t\t', tfcount,'\t', doc_count[word],'\t', idf_count[word2]     
    
    '''
    ## Computing the values of idf of words from Rebecca Weiss Code (Stanford)                   
    vocab_idf = {}
    for word in vocab.keys():
        idf_value =  idf(word,doclist)
        vocab_idf[word] = (vocab[word],idf_value)
    '''   

    ## Sorting the list vocab_idf in decreasing order of the tf_values 
    #sorted_y = sorted(vocab_idf.iteritems(), key=operator.itemgetter(1))
    #sorted_y.reverse()  # it arranges the list in decreasing order of count values

    return sorted_x              
   
    #return sorted_y



###################################################################################################################################

###################################################################################################################################

def numDocsContaining(word, doclist):
    doccount = 0
    for doc in doclist:
        if freq(word, doc) > 0:
            doccount +=1
    return doccount 


def idf(word, doclist):
    n_samples = len(doclist)
    df = numDocsContaining(word, doclist)
    return  np.log(float(n_samples) / float(1+df))

def build_idf_matrix(idf_vector):
    idf_mat = np.zeros((len(idf_vector), len(idf_vector)))
    np.fill_diagonal(idf_mat, idf_vector)
    return idf_mat
 
def l2_normalizer(vec):
    denom = np.sum([el**2 for el in vec])
    return [(el / math.sqrt(denom)) for el in vec]
 
def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def tf(term, document):
  return freq(term, document)

def freq(term, document):
  return document.split().count(term)
        
def termfreq(mydoclist):
    vocabulary = build_lexicon(mydoclist)
    doc_term_matrix = []

    print len(list(vocabulary))
    for i,doc in enumerate(mydoclist):
        '''
        tf_vector = [tf(word, doc) for word in vocabulary]
        tf_vector_string = ', '.join(format(freq, 'd') for freq in tf_vector)
        # print 'The tf vector for Document %d is [%s]' % ((mydoclist.index(doc)+1), tf_vector_string)
        doc_term_matrix.append(tf_vector)
        '''
        ## A different way of doing term-freq for all docs

        print 'term freq for doc number is   ', i
        tf_doc = {}
        tf_vector = list() 
        for word in doc.split():
            if word.strip() in tf_doc:
                tf_doc[word.strip()] += 1                
            else:
                tf_doc[word.strip()] = 1
       
        for word in vocabulary:
            if word in tf_doc.keys():
                tf_vector.append(tf_doc[word]) 
            else:
                tf_vector.append(0)

        doc_term_matrix.append(tf_vector)             
        # here's a test: why did I wrap mydoclist.index(doc)+1 in parens?  it returns an int...
        # try it!  type(mydoclist.index(doc) + 1)
  
    ''' 
    ## Loading the idf values from the pickle file which was saved earlier
    idf_count = dict()
    #with open('idf_values.pickle', 'rb') as pfile:
    #    idf_count = pickle.load(pfile)

    vocab_idf = dict()
    doc_count = dict()
    ## Calculating the value of the idf part again in these documents  
    for i, doc in enumerate(mydoclist):
        for word in doc.split():
            if word.strip() in vocab_idf:
                vocab_idf[word.strip()].append(i)
            else:
                vocab_idf[word.strip()] = [i]
    
    ## Code for computing the idf value of the terms from the inverted index
     # first converting vocab_idf to set and then making it to list
     # dict doc_count contains the count of a word appearing in that number of documents
    
    NUM_DOCS = len(mydoclist)
    for word in vocab_idf.keys():
        vocab_idf[word] =  list(set(vocab_idf[word]))
        doc_count[word] = len( vocab_idf[word] )        
        idf_count[word] = np.log( float(NUM_DOCS)/float(1 + doc_count[word]) )

    
    my_idf_vector = list() 
    ## Making the idf vector from loaded idf values according to our vocabulary
    for word in vocabulary:
        my_idf_vector.append(idf_count[word])

    ## Making the square idf matrix from my_idf_vector
    my_idf_matrix = build_idf_matrix(my_idf_vector)

    doc_term_matrix_tfidf = []
    ## Performing tf-idf matrix multiplication
    for tf_vector in doc_term_matrix:
        doc_term_matrix_tfidf.append(np.dot(tf_vector, my_idf_matrix))

    ## Normalizing the vectors by taking the L2 norm
    doc_term_matrix_tfidf_l2 = []
    for tf_vector in doc_term_matrix_tfidf:
        doc_term_matrix_tfidf_l2.append(l2_normalizer(tf_vector))

    # print 'All combined, here is our master document term matrix: '
    # print doc_term_matrix
    '''


    
    doc_term_matrix_l2 = []
    for vec in doc_term_matrix:
        doc_term_matrix_l2.append(l2_normalizer(vec))
    

    #return (doc_term_matrix_tfidf_l2, list(vocabulary) )
    return (doc_term_matrix_l2, list(vocabulary))

