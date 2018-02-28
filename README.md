#Wikivec

Calcula os topicos de determinada frase a partir de artigos da Wikipedia.

##Instalar

Para instalar execute o comando abaixo para instalar as dependencias

> pip3 install -r requirements.txt

Idealmente a partir de um ambiente virtual isolado.

> virtualenv -p python3 hugenv
> source hugenv/bin/activate

##Downloads

-[Modelo pré-treinado](https://drive.google.com/open?id=1PTNQTRtdiUdNbljG5fIRLxE8HhdQ6hhH)
-[Resultados preliminares aplicando nos projetos de lei da Câmara dos Deputados](https://drive.google.com/open?id=1bCafrrl8QqA_RsdKcNsw7zkHAMw6V7d6)

##Executar

Para executar o codigo e carregar o modelo pre-treinado a partir da linha
de comando:

> hug -f src/main.py

Isso vai habilitar a api na url **localhost:8000**

A API Rest pode ser consumida enviando uma requisição GET com a frase desejada
para:

> localhost:8000/topicos?frase=SUA FRASE

São necessários no mínimo 5GB de memória para a API funcionar.

##Explicação

Para maiores detalhes de como isto tudo funciona, consulte os notebooks.

##TO-DO

[ ] tratar a pontuação da frase de input, pois não são aceitas na URL
[ ] reduzir o uso de memória
[ ] aceitar múltiplos documentos na URL ou um arquivo CSV
