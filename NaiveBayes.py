
import labels
import numpy as np

class NaiveBayes :
  # Use these to compute P( Language )

  docLanguageCounts = {}
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
     if doc.language in languagecountmap:
         languagecountmap[doc.language] += 1
     else:
         languagecountmap[doc.language] = 1

   for key in languagecountmap:
        self.docLanguageCounts[key] = float(languagecountmap[key])/float(totaldoccount)


   for doc in corpus:
       for ngram in doc.text:
           if (doc.language,ngram) in self.languageWordCounts:
               self.languageWordCounts[(doc.language,ngram)] += 1
           else:
               self.languageWordCounts[(doc.language,ngram)] = 1

           if doc.language in self.wordCountsInOneLanguageMap:
               self.wordCountsInOneLanguageMap[doc.language] += 1
           else:
               self.wordCountsInOneLanguageMap[doc.language] = 1




  #Should compute P(word|language).Implement with add-lambda smoothing.
  def p_wordGivenLg(self,word,language,lamda):
     val = 0.0
     count = 0.0
     totalcount = 0.0
     totallanguages = len(self.docLanguageCounts)

     if(language,word) in self.languageWordCounts:
        count = self.languageWordCounts[(language, word)]

     totalcount =  self.wordCountsInOneLanguageMap[language]

     val = float(count+lamda)/float(totalcount+(lamda*totallanguages))

     return val



  #This function takes a document as a parameter, and returns the highest scoring language as a
  #Language object.
  def mostLikelyLanguage(self,doc,lamda):

    # Loop over the possible languages (they should accessible in docLanguageCounts.keys), and find
    # the language with the highest P( Document, Language ) score
    score = {}
    for lang in self.docLanguageCounts:
        score[lang] = np.log(self.docLanguageCounts[lang])
        for word in doc.text:
            val = self.p_wordGivenLg(word, lang, lamda)
            score[lang] += np.log(float(val))
    return max(score, key=score.get)
