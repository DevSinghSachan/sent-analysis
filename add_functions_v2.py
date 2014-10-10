import os, re

def KeywordSearch( class_words, RESULTS_FILE, FILES_DIR_TEXT, rownum):

        for i,infile in enumerate(sorted(os.listdir(FILES_DIR_TEXT))):
                #print >> outfile, rownum, '\t',
                ##print "rownum :: ", rownum
                if infile == txt_file:
                  print >> outfile, rownum, "\t",
                  FILE_PATH = FILES_DIR_TEXT + infile
                  with open(FILE_PATH,'rb') as txtfile:
                        foo = txtfile.read()

                        for j,key in enumerate( sorted(class_words.keys() )):
                                list1 = class_words[key]
                                total = 0
                                str1 = ""  
                                for word in list1:
                                        match = re.findall( "\\b"+word+"\\b", foo.lower())
                                        if (match):
                                          if len( str1.split(";") ) < 11:
                                            str1 += word + ";"
                                        total += len(match)

                                ##print >> outfile, str(total),'\t',
                                ##if ( len( str1.split(";")) > 5 ):
                                print >> outfile, str1,
                                print >> outfile, '\t',
                  print >> outfile,'\n',

