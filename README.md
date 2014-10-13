sent-analysis
=============
Here are some instructions to play with the code

Pre-requisites to run the code.

Please install the Anaconda library for python 2.7 from the link below. 
http://continuum.io/downloads

It includes various packages like scikit-learn etc which are required in our case.

1) The main part of the code is the aspect_search.py file. It takes aspects and keywords file as input 
   and outputs the names of keywords under aspects for review texts. It automatically takes example files
   for input. 
   To execute the code type "python aspect_search.py"

2) "tfidf_computation.py" outputs the count of term frequency (tf), inverse document frequency (idf) and tf*idf
    for the unique words in the corpus. To run the code type "python tfidf_computation.py"

3) "aspectKeyword.py" takes input from an excel file for the dictionary of sentiment words and outputs them in a 
   text file. Run the file by "python aspectKeyword.py"
  
