import hug
from gensim.models.doc2vec import Doc2Vec
from gensim.utils import simple_preprocess


model = Doc2Vec.load('model/Doc2Vec(dbow+w,d200,n5,w8,mc2,s0.001,t8)')


@hug.get(examples='frase=Ao verme que primeiro roeu as frias carnes de meu cadáver')
@hug.local()
def topicos(frase: hug.types.text):
    """Informa os topicos de uma frase qualquer"""
    tokens = simple_preprocess(frase)
    inferred_vector = model.infer_vector(tokens)
    similars = model.docvecs.most_similar([inferred_vector], topn=10)

    return {
        'message': similars
    }
