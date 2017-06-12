

import labels

class IO :

  def extractNGrams(text,n):
    # pad the string with document boundary markers, and return an array of a sliding window over
    # the characters in the string
    textpad = ("#" * (n - 1) + text + "#" * (n - 1))
    leng = len(textpad)
    leng = leng - (n - 1)
    myarr = []
    for i in range(0, leng):
      strvab = ""
      for j in range(i, i + n):
        strvab += str(textpad[j])
      myarr.append(strvab)
    return myarr


  def readDocuments(self,corpusPath,n):
    file = open(corpusPath,"r")
    lines = file.readlines()
    docsset = []
    for line in lines:
       id,text,label = line.split("|")
       characterNGrams = self.extractNGrams(text,n)
       doc = labels.Document(id,characterNGrams,label)
       docsset.append(doc)
    file.close()
    return docsset






