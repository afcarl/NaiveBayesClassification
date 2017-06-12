#package lin567_p1

import labels
import numpy as np


class NaiveBayes :
  # Use these to compute P( Language )

  docLanguageCounts ={}
  docCount = 0

  #Use these to compute P( Word | Language )
  languageWordCounts = {}
  wordCountsInOneLanguageMap = {}

  #This should increment counts so you can compute P( Language ) and P( Word | Language )

  def train(self,corpus):

   totaldoccount = 0
   languagecountmap = {}

   #This loops over the set of documents, and provides variables for the document id as a String,
   # the document text as an Array[String], and the language as a Language
   for doc in corpus:
     totaldoccount +=1
     if doc in languagecountmap:
         languagecountmap[doc.language] += 1
     else:
         languagecountmap[doc.language] = 1

   for key in languagecountmap:
       self.docLanguageCounts[key] = float(languagecountmap[key])/float(totaldoccount)

   for doc in corpus:
       for word in doc.text:
           if word in self.languageWordCounts:
               self.languageWordCounts[(doc.language,word)] += 1
           else:
               self.languageWordCounts[(doc.language,word)]  = 1

           if doc.language in self.wordCountsInOneLanguageMap:
               self.wordCountsInOneLanguageMap[doc.language]+= 1
           else:
               self.wordCountsInOneLanguageMap[doc.language] = 1


  #Should compute P(word|language).Implement with add-lambda smoothing.
  def p_wordGivenLg(self,word,language,lamda):
    val = ((self.languageWordCounts[(word,language)]) + lamda)/((self.wordCountsInOneLanguageMap[language])+lamda*len(self.docLanguageCounts))
    return val

  #Should compute P(Language)
  #def p_Lg(self,language):
   # return self.docLanguageCounts[language]


  # Should compute P( Word, Language )= P( Language )\prod_{Word in Document}P( Word | Language )
  #def p_docAndLg(doc,language,lamda):
    #a = 0


  #This function takes a document as a parameter, and returns the highest scoring language as a
  #Language object.

  def mostLikelyLanguage(self,doc,lamda):

    # Loop over the possible languages (they should accessible in docLanguageCounts.keys), and find
    # the language with the highest P( Document, Language ) score
    maxscorelanguage = ""
    maxscore = 0
    for lang in self.docLanguageCounts:
        score = self.docLanguageCounts[lang]
        for word in doc.text:
            score *= self.p_wordGivenLg(self,word,lang,lamda)
        if score > maxscore:
           maxscore = score
           maxscorelanguage = lang

    return maxscorelanguage




