#!/home/lucianosb/anaconda3/bin/python
from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess
import multiprocessing

wiki = WikiCorpus('data/ptwiki-latest-pages-articles.xml.bz2')


class TaggedWikiDocument(object):
    def __init__(self, wiki):
        self.wiki = wiki
        self.wiki.metadata = True

    def __iter__(self):
        for content, (page_id, title) in self.wiki.get_texts():
            yield TaggedDocument([c for c in content], [title])


documents = TaggedWikiDocument(wiki)

pre = Doc2Vec(min_count=0)
pre.scan_vocab(documents)

cores = multiprocessing.cpu_count()

model = Doc2Vec(
                dm=0,
                dbow_words=1,
                size=300,
                window=10,
                min_count=2,
                iter=10,
                workers=cores)

model.build_vocab(documents)

model.train(documents, total_examples=model.corpus_count, epochs=model.iter)

model.delete_temporary_training_data(
                                    keep_doctags_vectors=True,
                                    keep_inference=True)

model.save('models/wiki-latest')
