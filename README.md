# Adote uma causa

`Adote uma causa` é uma plataforma com o objetivo de conectar doadores a projetos sociais.

![Tela principal](https://github.com/MarlonFL15/Adote-uma-Causa/blob/main/galeria/home.gif)

### Motivação

---

Esse projeto foi realizado com o intuito de praticar meus conhecimentos em django. Comecei a estudar esse framework recentemente, e esse projeto surgiu como ideia para colocar o conhecimento adquirido em prática.

Objetivos do projeto:
+ Permitir que o usuário filtre por projetos sociais de diversos temas
+ Permitir que o usuário  acesse informações detalhadas de um determinado projeto
+ Mostrar projetos em destaque

### Instalação e configuração

---

#### Dependências

* Python 3 e Django instalados

Clone o projeto e entre no diretório
    
    $ git clone https://github.com/MarlonFL15/Adote-uma-Causa
    $ cd Adote-uma-Causa
    
Após ter baixado o projeto, a única configuração necessária é configurar a `api_key`. Para criar a sua, você precisa acessar a [globalgiving](https://www.globalgiving.org/), se cadastrar e criar a sua chave de API. Após criar, você precisa acessar `/app_adote_uma_causa/request.py`, dentro do diretório de projeto, e alterar a seguinte linha, colocando a sua chave:

`API_KEY = 'your_key'`

Após isso, apenas execute o servidor de desenvolvimento:

    $ python manage.py runserver

Após isso, o servidor começará a rodar na porta 8000, e a página inicial do projeto está em [8000/home]()

### Descrição técnica da solução

---

* A solução consumiu a API gratuita disponibilizada pelo [globalgiving](https://www.globalgiving.org/)
* Como a API retorna os dados em inglês, foi utilizado a biblioteca `googletrans` para traduzir as informações para português
* Para as páginas em HTML, foi utilizado um template gratuito, que pode ser baixado em : [https://htmlcodex.com/free-charity-website-template/](https://htmlcodex.com/free-charity-website-template/);

### Conclusões finais

---

Com a realização desse projeto, foi possível aplicar alguns conhecimentos que adquiri por meio de cursos, vídeos e blogs, tais como:

* Como estruturar um projeto em django;
* Como utilizar rotas com o django;
* Como funcionam as views;
* Como usar template tags;
* Como consumir API externas;
* Como customizar template tags;
* Como trabalhar com subtemplates;

### Galeria de imagens

---

<img src = "https://github.com/MarlonFL15/Adote-uma-Causa/blob/main/galeria/home.gif">
<p>
  Gif demonstrativo da página principal
</p>

<img src = "https://github.com/MarlonFL15/Adote-uma-Causa/blob/main/galeria/projetos.gif">
<p>
  Gif demonstrativo da página de Projetos e Visualização de projeto
</p>

<img src = "https://github.com/MarlonFL15/Adote-uma-Causa/blob/main/galeria/projetos.png">
<p>
  Imagem recortada da página de projetos
</p>

<img src = "https://github.com/MarlonFL15/Adote-uma-Causa/blob/main/galeria/single.png">
<p>
  Imagem recortada da página de visualizar projeto
</p>





