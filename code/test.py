import codecs
import nltk
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('./project/model.gz',
'/opt/libs/stanford-ner-2015-12-09/stanford-ner.jar')
with codecs.open('./project/report/txt file/Zhou et al., (2006) - Neural substrates for forward and backward recitation of numbers._annotated_fulltext.txt', encoding='utf-8') as rf:
    data = rf.read()
    sent=nltk.sent_tokenize(data)
    result = []
    for i in sent:
        a = st.tag(i.split())
        for j in a:
            if j[1] == 'TEST':
                result.append(i)
                break
print(result)
print(len(result))