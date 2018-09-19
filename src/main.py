import hug
from gensim.models.doc2vec import Doc2Vec
from gensim.utils import simple_preprocess
import re

model = Doc2Vec.load('models/wiki-latest')


@hug.get('/topicos', examples='frase=Vingadores são um grupo de super-heróis')
@hug.local()
def topicos(frase: str):
    """Informa os topicos de uma frase qualquer"""
    tokens = simple_preprocess(frase)
    inferred_vector = model.infer_vector(tokens)
    similars = model.docvecs.most_similar([inferred_vector], topn=10)

    return {
        'topicos': similars
    }


@hug.get(examples="expressao=homem está para rei como mulher está para")
def analogia(expressao: str):
    """Calcula uma analogia entre termos"""

    entry = '{0}'.format(expressao)
    math_symbol = "\+"
    analogy_symbol = "está para"

    # Case 1: user wants to do word math: word1 - word2 + word3
    positive = []
    negative = []
    if math_symbol in entry:
        positive.append(re.split(" |\+|-", entry)[0])
        negative.append(re.search(r'\*\-\s*(\S+)', entry).group(1))
        positive.append(re.search(r'\*\+\s*(\S+)', entry).group(1))

    # Case 2: user wants to do analogies: word1 is to word2 as word3 is to
    elif analogy_symbol in entry:  # analogy expression is in the input
        split = entry.split(analogy_symbol)
        negative.append(split[0].strip())  # first word is negative
        positive = [word.strip() for word in split[1].split("como")]
    similar_words = model.most_similar_cosmul(positive=positive,
                                              negative=negative)
    most_similar_word = str(similar_words[0][0])
    return most_similar_word
