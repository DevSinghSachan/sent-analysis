import pandas as pd

## This code takes excel files as input and writes the aspect tags with keywords to an output file


## This is the name of the input excel file which contains aspect information
INPUT_FILE = "seed_aspects.xlsx"
SHEET_NO_EXL = 0

## In this the aspect words will be separated by a "|"
OUTPUT_DIR = "aspect_output"
OUTPUT_FILE = OUTPUT_DIR + "/" + "aspect_tags.txt"


if __name__ == "__main__":

    sheet1 = pd.read_excel( INPUT_FILE, SHEET_NO_EXL, index_col=None, na_values=['NA'] )
    array_temp = sheet1.values

    fp = open(OUTPUT_FILE, "wb") 

    rownum = 0
    for row2 in array_temp:
	col = 0
	for cell in row2:

	    if col==0:
              dept = unicode(row2[col]).encode("utf-8")

            if col==1:
              keywords11 = [] 
              keywords1 = unicode(row2[col]).encode("utf-8").lower().split(";")
              for word in keywords1:
                keywords11.append( word.strip() )
              
            if col==2:
              keywords22 = []
              keywords2 = unicode(row2[col]).encode("utf-8").lower().split(";")
              for word in keywords2:
                keywords22.append( word.strip() )
        
            col += 1

        if ( keywords1 != [] ) or ( keywords2 != [] ):
          print >> fp, dept, "\t",
          keywords33 = set( keywords11 + keywords22 )
           
          print >> fp, "|".join(keywords33)

    fp.close()
