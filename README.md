# Wikivec

Calcula os topicos de determinada frase a partir de artigos da Wikipedia.

As instruções abaixo são para um sistema Linux. O desenvolvimento foi realizado
em um PC com Ubuntu 16.04, processador i7, 16GB RAM.

## Instalar

O processo de instalação e uso foi simplificado através dos comandos Make. Primeiro,
precisamos criar um ambiente virtual com o seguinte comando:

> make create_environment

Agora basta ativar o ambiente com **source activate ptwiki2vec**

Em seguida, podemos baixar o dump mais recente da wikipedia com o comando data.
Este comando irá também instalar as dependências necessárias.

> make data

Agora, podemos treinar o modelo com o comando train:

> make train

Esta etapa durou 6h40min no PC que usei para treinar este modelo. Treinar na
nuvem com mais CPUs irá agilizar esse processo.

## Executar

Para carregar o modelo pre-treinado, e utilizá-lo como uma API REST:

> make serve

Isso vai habilitar a API na url **localhost:8000**

A API Rest pode ser consumida enviando uma requisição GET com a frase desejada
para:

> localhost:8000/topicos?frase=SUA FRASE

A API também pode fazer analogia de termos como no famoso exemplo de
**rei-homem+mulher=rainha**:

> localhost:8000/analogia?expressao=homem está para rei como mulher está para"

São necessários no mínimo 5GB de memória para a API funcionar.

## Explicação

Para maiores detalhes de como isto tudo funciona, consulte os notebooks.

## TO-DO

-   [X] tratar a pontuação da frase de input, pois não são aceitas na URL
-   [ ] parametrizar os comandos make
-   [ ] reduzir o uso de memória
-   [ ] aceitar múltiplos documentos na URL ou um arquivo CSV
