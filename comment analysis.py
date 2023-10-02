import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.util import bigrams,trigrams,ngrams
#TAKING REVIEW FROM THE USER
sent=input("WRITE YOUR REVIEW-->")

#TOKENIZING THE SENTENCE
sent_token=word_tokenize(sent)

#REMOVING STOPWORD FROM THE SENTENCE
stop=stopwords.words("english")
n=len(sent_token)
negation=['not','no','neither','nor']
filter_sent=[]
for i in range(0,n):
    if (sent_token[i]  in negation or sent_token[i] not in stop):
        filter_sent.append(sent_token[i])

#CREATING BIGRAM OF SENTENCE
bigram=list(nltk.bigrams(filter_sent))

#CREATING LIST OF NEGATIVE AND POSITIVE WORD 
with open('positive.txt', 'r') as f:
    positive = []
    for line in f:
        positive.append(line.strip())
with open('negative.txt', 'r') as f:
    negative = []
    for line in f:
        negative.append(line.strip())
k=len(bigram)
flag=0
#ANALYSING IF THE SENTENCE IS NEGATIVE OR POSITIVE

if(len(filter_sent)==1):
       if(filter_sent[0] in positive):
           print("YOUR REVIEW IS POSITIVE")
           flag=1
       elif(filter_sent[0] in negative):
           print("YOUR REVIEW IS NEGATIVE")
           flag=1
else:
    for i in range(k):
       if (bigram[i][0] in negation and bigram[i][1] in positive) :
           print("YOUR REVIEW IS NEGATIVE")
           flag=1
       elif( bigram[i][0] not in negation and bigram[i][1] in positive):
           print("YOUR REVIEW IS POSITIVE")
           flag=1
       elif((bigram[i][0] not in negation and bigram[i][1] in negative) or (sent in negative)):
           print("YOUR REVIEW IS NEGATIVE")
           flag=1
       elif( bigram[i][0] in negation and bigram[i][1] in negative):
           print("YOUR REVIEW IS POSITIVE")
           flag=1
       elif(bigram[i][0] in positive):
           print("YOUR REVIEW IS POSITIVE")
           flag=1
       elif(bigram[i][0] in negative):
           print("YOUR REVIEW IS POSITIVE")
           flag=1

#IF MACHINE CANNOT DETECT THE SENTENCE IT WILL ASK HELP FROM THE USER AND WILL UPDATE ITS LIST
           
           
if flag==0:
    print("SORRY CAN'T DETECT...HELP ME!!")
    op=input("YOUR REVIEW IS POSITIVE OR NEGATIVE?")
    
    adj=input("WHICH ADJECTIVE YOU HAVE USED IN YOUR REVIEW?")
    
    for token in sent_token:
        pos=nltk.pos_tag(filter_sent)
        print(pos)
    if(pos[0][1]=='JJ'):
        if(len(sent_token)==1):
            if(op.lower()=='positive'):
                         with open('positive.txt', 'a') as my_file:
                             my_file.write('\n'+adj)
            if(op.lower()=='negative'):
                with open('negative.txt', 'a') as my_file:
                             my_file.write('\n'+adj)
                             
        else:
            for i in range(k):
                if( bigram[i][0] not in negation and op.lower()== 'positive'):
                    with open('positive.txt', 'a') as my_file:
                        my_file.write('\n'+adj)
                elif( bigram[i][0] in negation and op.lower()=='negative'):
                    with open('positive.txt', 'a') as my_file:
                        my_file.write('\n'+adj)
                elif (bigram[i][0] in negation and op.lower()=='positive'):
                    with open('negative.txt', 'a') as my_file:
                        my_file.write('\n'+adj)
                elif(bigram[i][0] not in negation and op.lower()=='negative'):
                     with open('negative.txt', 'a') as my_file:
                        my_file.write('\n'+adj)

    else:
        print("THIS IS NOT AN ADJECTIVE")   
    print("THANKYOU SOO MUCH FOR YOUR HELP!!")
            

                    
            
    
    
