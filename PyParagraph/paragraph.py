# import needed modules
import os
import re

# Module for reading CSV's
import csv

csvpath = "paragraph_1.csv"

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

     #  Initialize totals
    apprx_characters = 0
    apprx_words = 0
    apprx_sentences = 0
    avg_letter_count = 0
    avg_sentence_lenght = 0
    
    for row in csvreader:
      paragraph = row[0]

apprx_characters = len(paragraph)
sentences = re.split("(?<=[.!?]) +", paragraph)
apprx_sentences= (len(sentences))
words = re.split("(\w[\w']*\w|\w)", paragraph)
apprx_words = (len(words))
avg_letter_count= apprx_characters / apprx_words
avg_sentence_lenght = apprx_words / apprx_sentences

print ("Paragraph Analysis")
print ("------------------------------------------------")
print ("Approximate Word Count:   " + str(apprx_words))
print ("Approximate Sentence Count:  " + str(apprx_sentences))
print ("Approximate Letter Count:  " + str(avg_letter_count))
print ("Average Sentance Length:  " + str(avg_sentence_lenght))
 
