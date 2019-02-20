#!/usr/bin/env python3
from gensim.corpora.wikicorpus import WikiCorpus
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import simple_preprocess
import multiprocessing
import errno
import os
import time

path = os.getcwd()
print("O diretório atual é %s" % path)
try:
    os.mkdir('models')
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    pass


print("Começando às " + time.strftime("%H:%M:%S") + ".")
print("Processando a wikipedia...")

wiki = WikiCorpus('data/ptwiki-latest-pages-articles.xml.bz2')

print("Pré-processamento concluído às " + time.strftime("%H:%M:%S") + ".")

class TaggedWikiDocument(object):
    def __init__(self, wiki):
        self.wiki = wiki
        self.wiki.metadata = True

    def __iter__(self):
        for content, (page_id, title) in self.wiki.get_texts():
            yield TaggedDocument([c for c in content], [title])


documents = TaggedWikiDocument(wiki)

cores = multiprocessing.cpu_count()

model = Doc2Vec(
                dm=0,
                dbow_words=1,
                vector_size=300,
                window=10,
                min_count=2,
                epochs=10,
                workers=cores)

print("Construindo o vocabulário...")

model.build_vocab(documents)

print("Treinamento iniciado às " + time.strftime("%H:%M:%S") + ".")

print("Treinando o modelo...")

model.train(documents, total_examples=model.corpus_count, epochs=model.iter)

model.delete_temporary_training_data(
                                    keep_doctags_vectors=True,
                                    keep_inference=True)

timestr = time.strftime("%Y%m%d-%H%M%S")
filepath = 'models/wiki-'+ timestr
model.save(filepath)

print("Tudo pronto! Treinamento finalizado às" + timestr + '!')

print("Execute o comando make serve.")
