import re

REVIEW_FILE_NAME = "product_expert_review.txt"
ASPECTS_OUTPUT_FILE = "review_aspects.txt"


if __name__ == "__main__":
 
 with open(REVIEW_FILE_NAME, "rb") as fp:
   for line in fp:
     print line.split("/t")
