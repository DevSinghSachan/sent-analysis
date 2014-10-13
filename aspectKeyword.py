import pandas as pd
# This code takes aspect information from excel file as input and writes the
# aspect tags with keywords to a text file.

# For details on the format of excel file, please see the example of
# "seed_aspects.xlsx".

# Details of the input excel file above which contains aspect information.
# We also need to specifiy the sheet information of the excel file
INPUT_FILE = "seed_aspects.xlsx"
SHEET_NO_EXL = 0

# Input the aspect col and keywords col numbers here
ASPECT_COL = 0
KEYWORD_COL1 = 1
KEYWORD_COL2 = 2

# name of output text file in which the aspect words will be separated
# by a "|" operator
OUTPUT_DIR = "aspect_output"
OUTPUT_FILE = OUTPUT_DIR + "/" + "aspect_tags.txt"


if __name__ == "__main__":

    # Opening the excel file
    # We use read_excel function of pandas library to read the xlsx file.
    # For more details on the options please refer to -
    # http://pandas.pydata.org/pandas-docs/stable/
    # generated/pandas.io.excel.read_excel.html

    sheet1 = pd.read_excel(INPUT_FILE, SHEET_NO_EXL,
                           index_col=None, na_values=['NA'])
    array_temp = sheet1.values

    # Opening the output file for writing the keywords
    fp = open(OUTPUT_FILE, "wb")

    # Iterating through the rows of array_temp matrix
    rownum = 0
    for row2 in array_temp:
        col = 0
        for cell in row2:

            # Taking the aspect information
            if col == ASPECT_COL:
                aspect = unicode(row2[col]).encode("utf-8")

            # Taking the keywords information from the two columns
            # specified above
            if col == KEYWORD_COL1:
                keywords1 = []
                kw_list1 = unicode(row2[col]).encode("utf-8").lower().split(";")
                for word in kw_list1:
                    keywords1.append(word.strip())

            if col == KEYWORD_COL2:
                keywords2 = []
                kw_list2 = unicode(row2[col]).encode("utf-8").lower().split(";")
                for word in kw_list2:
                    keywords2.append(word.strip())

            col += 1

        if (keywords1 != []) or (keywords2 != []):
            # writing the aspect and keywords to output txt file
            print >> fp, aspect, "\t",

            # removing duplicates among keywords
            keywords3 = set(keywords1 + keywords2)

            print >> fp, "|".join(keywords3)

    fp.close()
