import json
import nltk
s1 = []
s2 = []
def art_filter(dictionary):
    for key, value in dictionary.iteritems():
        for i in value:
            for j in range(0, len(t1)):
                for k in t2[j]:
                    if k in i:
                        sentence =  "' %s ': the content of this sentence is related to '%s' test" % (i, t1[j])
                        s1.append(sentence)
                        s2.append(i)
                        break
print(s1)
f = open("project/Ahn et al., (2011) - The cortical neuroanatomy of neuropsychological deficits in MCI and AD_annotated_fulltext.txt", 'r')
text = f.read()
words =nltk.word_tokenize(text)
w = open('project/1.txt', 'w')
for i in words:
    w.write("%s\tO\n" % i)
f.close()
