import codecs
import nltk
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('./project/model.gz',
'/opt/libs/stanford-ner-2015-12-09/stanford-ner.jar')
ST = StanfordNERTagger('./project/english.muc.7class.distsim.crf.ser.gz',
'/opt/libs/stanford-ner-2015-12-09/stanford-ner.jar')
with codecs.open('project/modify/Zhou et al., (2016) - Substantia nigra echohenicity correlated with clinical features of PD_annotated_fulltext.txt', encoding='utf-8') as rf:
    data = rf.read()
    sent=nltk.sent_tokenize(data)
    result = []
    record = []
    for i in sent:
        a = st.tag(i.split())
        b = ST.tag(i.split())
        c = len(record)
        for j in range(0, len(a)):
            if a[j][1] == 'TEST' and b[j][1] != 'O':
                record.append(a)
                record.append(b)
                break
        if len(record) != c:
            result.append(i)
print(result)
print(len(result))
print(record)