# Adote uma causa

`Adote uma causa` é uma plataforma com o objetivo de conectar doadores a projetos sociais.

![Tela principal](https://github.com/MarlonFL15/Adote-uma-Causa/blob/main/galeria/home.gif)

### Motivação

---

Esse projeto foi realizado com o intuito de colocar em prática meus conhecimentos em django. Comecei a estudar esse framework recentemente, e esse projeto surgiu como ideia para colocar o conhecimento adquirido em prática.

Funcionalidades do projeto:
+ Mostrar projetos sociais em destaque;
+ Permitir que o usuário filtre por projetos sociais de diversos temas;
+ Permitir que o usuário  acesse informações detalhadas de um determinado projeto;

### Sobre o desenvolvimento

---

* O projeto consumiu a API gratuita disponibilizada pela plataforma [globalgiving](https://www.globalgiving.org/);
* Para o front-end, foi utilizado um template gratuito, que pode ser baixado em : [https://htmlcodex.com/free-charity-website-template/](https://htmlcodex.com/free-charity-website-template/);

### Instalação e configuração

---

#### Dependências

* Python 3

Clone o projeto, entre no diretório e baixe todas as bibliotecas necessárias:
    
    $ git clone https://github.com/MarlonFL15/Adote-uma-Causa
    $ cd Adote-uma-Causa
    $ pip install -r requirements.txt
    
    
Após ter baixado o projeto, a única configuração necessária é configurar a `api_key`. Para criar a sua, você precisa acessar a plataforma da [globalgiving](https://www.globalgiving.org/), se cadastrar e gerar a sua chave de API. Após criar, você precisa acessar `/app_adote_uma_causa/request.py`, dentro do diretório de projeto, e alterar a seguinte linha, colocando a sua chave:

`API_KEY = 'your_key'`

Após isso, apenas execute o servidor de desenvolvimento:

    $ python manage.py runserver

Após isso, o servidor começará a rodar na porta 8000, e a página inicial do projeto está em [8000/home]()

### Conclusões finais

---

Com o desenvolvimento desse projeto, consegui aplicar em prática alguns assuntos que venho estudando sobre django. Mesmo não trabalhando com banco de dados, esse projeto foi bom para me adaptar ao processo de configuração e estruturação de um projeto em django. Além disso, também foi interessante aprender a consumir API externas.


### Galeria de imagens

---

Caso você queira ver mais imagens de como ficou a solução final, você pode acessar este link para uma pasta no google drive:
https://drive.google.com/drive/folders/1cAepEolSLHYvO_VruXLlABLVNk5Co7Fd?usp=sharing



