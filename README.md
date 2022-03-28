# Projeto Mercadinho CRUD

Este projeto tem por objetivo permitir a comunicação de um banco dados MySQL com o python através de um interface no terminal.

<p align="justify"> 
 
Para acessar o vídeo demonstrativo do projeto [CLIQUE AQUI](https://drive.google.com/drive/u/1/folders/1jNBcDQStzFz5haRzG4oiOJt6TK6Nped4).

</p>
 
## Próximos passos
 
<p align="justify">  
  Como é possível observar o projeto possui duas pastas com funções, Arquivo e Interface, na pasta arquivo são as funções lógicas da aplicação e na interface a parte textual. Entretanto, ainda não concluí a organização sendo possível, ainda, isolar alguns estruturas utilizadas em funções.
</p>

<p align="justify"> 
 Outro ponto importante é que a abordagem de edição de tabelas pelo usuário não ficou intuitiva, pois como existem chaves estrangeiras alguns dados não podem ser editados facilmente. Dessa forma, será mais efetivo introduzir uma sequência pré-estabelecida para o cadastro na tabela "lista_produtos", evitando erros e facilitando a vida do usuário.
</p>

<p align="justify"> 
 Facilitando-se o cadastro torna-se viável automatizar o processo de controle de estoque, onde a cada novo cadastro de compra feito pelo caixa será automaticamente atualizado o estoque e uma mesnsagem de aviso para um valor mínimo será adicionado.
</p>

<p align="justify"> 
 Por se tratar de um projeto de estudo o mesmo será utilizado para estudar Django. Desta forma, o foco principal será transformar esse projeto pré-eliminar em uma aplicação Web.
</p>

<p align="justify"> 
Descobri sobre a existência de um ORM (Object-relational mapping) chamado "Peewee" que facilita e encapsula os comandos SQL, dessa forma torna-se possível implementar o banco de dados via python e não por SQL, o que protege e facilita o desenvolvimento do CRUD. Irei utiliza-los nos próximos programas. Ps.: o Django possui seu próprio ORM então não se faz necessário lançar mão de outro.
</p>

Opiniões, dúvidas ou dicas? Fique a vontade para entrar em contato.
