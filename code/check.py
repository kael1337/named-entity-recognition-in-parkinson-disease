import codecs
import nltk
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('./project/english.muc.7class.distsim.crf.ser.gz',
'/opt/libs/stanford-ner-2015-12-09/stanford-ner.jar')
with codecs.open('project/modify/SUMWOO.txt', encoding='utf-8') as rf:
    data = rf.read()
    sent=nltk.sent_tokenize(data)
    result = []
    for i in sent:
        a = st.tag(i.split())
        result.append(a)
print(result)