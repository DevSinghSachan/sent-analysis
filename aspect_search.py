import re, os, shutil

RESULTS_DIR = "aspect_output"
RESULTS_FILE = RESULTS_DIR  + "/" + "aspect_results.txt"
KEYWORDS_FILE = RESULTS_DIR + "/" + "aspect_tags.txt"

REVIEW_DIR = "review_text"
REVIEW_FILE = REVIEW_DIR + "/" + "product_expert_review.txt"

## This is a function to search for aspect keywords in reviews

def KeywordSearch( class_words, review_id, text, RESULTS_FILE):
  with open( RESULTS_FILE, "ab") as outfile:
    print >> outfile, review_id, "\t", text, "\t",
    for j,key in enumerate( sorted(class_words.keys() )):
      list1 = class_words[key]
      total = 0
      str1 = ""
      for word in list1:
        match = re.findall( "\\b"+word+"\\b", text.lower())

        if (match):
          str1 += word + ";"
          total += len(match)

          print >> outfile, word + ";",
      print >> outfile, '\t',
    print >> outfile,'\n',


if __name__ == "__main__":

## Taking a text file as input in which every line has single aspect information 
## and first word of the line represents an aspect class. Entries of aspect class are tab separated

  class_words = {}
  with open(KEYWORDS_FILE,'rb') as infile:
    for line in infile:
      category = line.strip().split('\t')[0]
      words = line.strip().split('\t')[1].split("|")
      class_words[category] = []
      for word in words:
        class_words[category].append(word.strip().lower())
 
  ##print class_words
  ## Writing the keys in outfile
  with open(RESULTS_FILE,'wb') as outfile:
    print >> outfile, "fileid", "\t", "comment", "\t", '\t'.join( sorted( class_words.keys() )), '\n',
 
  ## Doing processing of the excel file
  fp = open(REVIEW_FILE, "rb")

  mydoclist = []
  fileid = []

  count = 0
  for line in fp:
      count += 1
      
      if 0 == (count % 10):
        print count   

      row2 = line.split("~")
      
      col=0
      for cell in row2:
        if col==1:
          fileid = unicode(row2[col])

        if col==3:
          text = row2[col].strip()
          for temp in text.split("\t"):
            if len(temp.strip()) > 3:   
              KeywordSearch( class_words, fileid, temp.strip(), RESULTS_FILE)

        col += 1

  print count
