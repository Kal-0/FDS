# Schoolyard Finds

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub Files](https://img.shields.io/github/directory-file-count/Kal-0/FDS)
![GitHub repo size](https://img.shields.io/github/repo-size/Kal-0/FDS)
![GitHub language count](https://img.shields.io/github/languages/count/Kal-0/FDS)
![Bitbucket open issues](https://img.shields.io/github/issues-raw/kal-0/FDS)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/Kal-0/FDS)
![Bitbucket Commits/Year](https://img.shields.io/github/commit-activity/y/kal-0/FDS)

<img src="https://github.com/Kal-0/DECOY/blob/main/FDS/syf_logogrande.png?raw=true?width=1524&height=450" alt="Logo do Projeto">

> Esse projeto é uma plataforma marketplace desenvolvida para a comunidade da CESAR School, com o objetivo de facilitar o comércio entre os membros da faculdade, onde os seus usuários poderão publicar produtos que desejam vender e comprar de outros usuários, com a possibilidade de negociação do item que desejado. Podendo ser acessado através desse <b> [LINK](http://schoolyardfinds1.us-east-1.elasticbeanstalk.com/).</b>



## 🔎 Funcionalidades Principais
- Gerenciamento de Produtos: Permite que usuários registrem, editem e excluam produtos do marketplace.
- Autenticação de Usuários: Sistema de login e registro seguro integrado ao Django, com proteção CSRF e armazenamento seguro de senhas.
- Pesquisa e Filtros: Implementação de filtros dinâmicos e funcionalidade de busca para facilitar a navegação entre os produtos disponíveis.
- Testes Automatizados: Testes end-to-end com Selenium, verificando a integridade das principais funcionalidades em múltiplos navegadores.
- CI/CD: Pipeline automatizado utilizando GitHub Actions, garantindo testes automatizados e deploy contínuo para o ambiente de produção na AWS.
- Integração com AWS: Deploy automatizado para AWS Elastic Beanstalk, garantindo alta disponibilidade e escalabilidade do sistema.


## 🚀 Técnologias Utilizadas 
Backend: 
- Python
- Django
  
Frontend:
- HTML
- CSS
- JavaScript
  
Banco de Dados:
- SQLite (desenvolvimento)
- AWS RDS (produção)
  
Testes:
- Selenium
  
CI/CD:
- GitHub Actions
  
Deploy:
- AWS Elastic Beanstalk

Jira:
- [Quadro Jira](https://decoy0.atlassian.net/jira/software/projects/SF/boards/3)<br></br>

Figma:
- [Quadro Figma](https://www.figma.com/file/2ip4H8uwjQ2fh1LfifG0ys/Prot%C3%B3tipo-Lo-Fi?node-id=0-1&t=4z1jTTTTcBTCKFU9-0)
- [Figma Flow](https://www.figma.com/proto/2ip4H8uwjQ2fh1LfifG0ys/Prot%C3%B3tipo-Lo-Fi?node-id=154-3&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=154%3A3)<br></br>

Google Drive:
- [Sketchs](https://drive.google.com/drive/folders/1fE_FwNUclmHxMSdsRN0t-QUT1UX3w3iC)
- [Storyboards](https://www.figma.com/file/2ip4H8uwjQ2fh1LfifG0ys/Prot%C3%B3tipo-Lo-Fi?type=design&node-id=200%3A19&t=aEKpXn9853zZryfc-1)
- [Screencasts](https://drive.google.com/drive/folders/11NuwNQj38WPsKoISbP0Ki22pt3MdIBnv?usp=drive_link)
- [Pair Programming](https://drive.google.com/drive/folders/1441ZlJdDW0m1_KSqb98R9jETa0zYaEn8)
- [Painel e Backlog](https://drive.google.com/drive/folders/1QGdTE9Tlg82WNDR6jwmWwqslcwNFJAvp?usp=sharing)
- [Diagrama de atividades](https://drive.google.com/drive/folders/1og0MFgwVGYnetjAFjTKkcNZ920Ulbf7N?usp=drive_link)


## 📁 Estrutura do Projeto
- `.ebextensions`: Configurações para AWS Elastic Beanstalk.
- `.github`: Workflows para CI/CD com GitHub Actions.
- `SchoolYardFinds`: Código fonte da aplicação Django.
- `Home`
  - `forms.py`: Arquivo contendo os formulários utilizados na aplicação, implementados com o Django Forms para validação e manipulação de dados de entrada.
  - `models.py`: Definição dos modelos de dados, representando as entidades do sistema e suas relações com o banco de dados.
  - `tests.py`: Conjunto de testes automatizados, implementados para verificar a funcionalidade e integridade dos componentes do sistema.
  - `urls.py`: Mapeamento das URLs da aplicação para as views correspondentes, definindo a estrutura de navegação do site.
  - `views.py`: Implementação das views da aplicação, contendo a lógica de apresentação e manipulação de dados para as páginas web.
- `static`: Arquivos estáticos (CSS, JS, imagens).
- `templates`: Templates HTML renderizados pelo Django.
- `manage.py`: Script de gerenciamento do Django.
- `requirements.txt`: Lista de dependências Python necessárias para o projeto.


## 💻 Pré-requisitos
- <b>Linguagem de Programação:</b> Python v2023.8.0, JavaScript, CSS, HTML.
- <b>Git:</b> Baixar o Git.
- <b>IDE:</b> Visual Studio Code 1.78.2 ou outras IDEs.
- <b>Extensions:</b> SQLite Viewer v0.2.5, HTML CSS Support v1.13.1, Live Server v5.7.9.
- <b>Sistema Operacional Compatível:</b> Windows, Mac e Linux.


## ☕ Como Usar
Para usar Schoolyard Find, siga estas etapas:

- Instalar a Aplicação no seu Computador:
```
1. O usuário deverá criar uma pasta em seu computador com um nome informativo da aplicação, como "Aplicação Schoolyard Finds".
2. O usuário então deverá apertar com o botão direito do mouse dentro da pasta e abrir o terminal da pasta.
3. Após isso, ele deverá inserir no terminal o comando "git clone https://github.com/Kal-0/FDS.git".
4. O usuário então abrirá o seu Visual Studio Code na versão certa e com as extensões baixadas, e apertará no botão "File".
5. Após isso, ele deverá navegar até "Open Folder", escolhendo a pasta que ele nomeou e aplicou o git clone.
6. O usuário deverá clicar com o botão direito do mouse em "FDS" e escolher a opção "Open in Integrated Terminal".
```
- Comandos para Instalação Libs Necessárias no Requirements.txt:
```
1. pip install -r requirements.txt
```
- Comandos para Utilização da Aplicação Local:
```
1. python manage.py makemigrations
1. python manage.py migrate
3. python manage.py runserver
```
- Comandos para Contribuição:
```
1. git pull
2. git add .
3. git status
4. git commit -m "Inserir Mensagem"
5. git push
```
- Abrir o Site do Schoolyard Finds:
```
1. Inserir no seu navegador o link "http://schoolyardfinds1.us-east-1.elasticbeanstalk.com/"
```

## 🎥 Screencast 
[![Screencast](https://raw.githubusercontent.com/Kal-0/DECOY/main/FDS/Captura%20de%20tela%202024-08-10%20153129.png)](https://drive.google.com/file/d/1k1roe2FEPbm4_4T-YNH_GLkOIF9QiQyX/view?usp=drive_link)


## 🤝 Colaboradores
Agradecemos às seguintes pessoas que contribuíram para este projeto:

Desenvolvedores:
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Kal-0">
        <img src="https://avatars.githubusercontent.com/u/106926790?s=400&u=d51d91a8d447afbb4a9d0be21d664b82d7091fc5&v=4" width="100px;" alt="Foto Kal"/><br>
        <sub>
          <b>Caio Cesar</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Fiend3333">
        <img src="https://avatars.githubusercontent.com/u/116087739?v=4" width="100px;" alt="Foto Diogo"/><br>
        <sub>
          <b>Diogo Henrique</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/EstelaLacerda">
        <img src="https://avatars.githubusercontent.com/u/117921412?v=4" width="100px;" alt="Foto Stora"/><br>
        <sub>
          <b>Estela Lacerda</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/MatheusGom">
        <img src="https://avatars.githubusercontent.com/u/117746778?v=4" width="100px;" alt="Foto Matheus Gomes"/><br>
        <sub>
          <b>Matheus Gomes</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/mell-brayner">
        <img src="https://avatars.githubusercontent.com/u/119381419?v=4" width="100px;" alt="Foto Mell Brayner"/><br>
        <sub>
          <b>Mell Brayner</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/SofiaValadares">
        <img src="https://avatars.githubusercontent.com/u/113111708?v=4" width="100px;" alt="Foto Sofia Valadares"/><br>
        <sub>
          <b>Sofia Valadares</b>
        </sub>
      </a>
    </td>
  </tr>
</table>


## 📝 Licença
Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE) para mais detalhes.

[⬆ Voltar ao topo](#)<br>
