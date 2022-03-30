import json
import os
import sys

import django
from tqdm import tqdm
from vocab import Vocab

sys.path.extend(['..'])

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NLP_NewsRec.settings")
django.setup()

from News.models import News, Recommend

# file = '/Users/Jyonn/Downloads/news-test.tsv'
#
# with open(file, 'r') as f:
#     for line in tqdm(f):
#         data = line.split('\t')
#         nid, cat, subcat, title, abs = data[:5]
#
#         News.create(nid=nid, category=cat, subcategory=subcat, title=title, abstract=abs, body=None)


# file = '/Users/Jyonn/Downloads/body.txt'
#
# with open(file, 'r') as f:
#     for line in tqdm(f):
#         if line[-1] == '\n':
#             line = line[:-1]
#         data = json.loads(line)
#         nid = data['nid']
#         body = data['body']
#
#         news = News.get(nid)
#         news.body = body
#         news.save()

file = '/Users/Jyonn/Downloads/sim.csv'
nid_vocab = Vocab(name='nid').load('/Users/Jyonn/Downloads/')

with open(file, 'r') as f:
    index = 0

    for line in tqdm(f):
        if line[-1] == '\n':
            line = line[:-1]
        data = json.loads(line)
        source = News.get(nid_vocab.index2obj[index])
        for target_index in data:
            target = nid_vocab.index2obj[target_index]
            Recommend.create(source=source, target=News.get(target))
        index += 1
