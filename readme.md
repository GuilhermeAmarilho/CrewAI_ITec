# 🧠 Sistema Multiagente para Geração de Artigos com CrewAI

Este projeto tem como objetivo a criação de um sistema multiagente utilizando o framework CrewAI para gerar artigos de no mínimo 300 palavras, a partir de um tema específico, com base em informações obtidas da API da Wikipedia.

> ℹ️ Projeto desenvolvido como parte do **teste prático** para o processo seletivo do Instituto de Computação – ITEC/FURG, referente ao **Edital nº 026/2025**, destinado à vaga de **Iniciação Científica**.

---

## 🚀 Tecnologias Utilizadas

- Python
- [CrewAI](https://docs.crewai.com/)
- [CrewAI Tools](https://docs.crewai.com/concepts/tools)
- API da Wikipedia
- LLMs gratuitas (Groq, Gemini)
- FastAPI ou Flask
- Pydantic

---

## 📋 Tarefas do Projeto

## 1. - Estrutura do projeto
- Ir atualizando conforme update
- [ ] Versão final do projeto
```
CrewAI_ITec/
│ ── app/ 
│ │ └── agents/
│ │ │   # Modela a resposta do tool
│ │ │ └── __init__.py
│ │ │     # Modulariza a pasta para permitir import
│ │ │ └── api_search.py
│ │ │ └── api_write.py
│ │ └── tools/
│ │ |   # Gerencia e faz a comunicação com a API
│ │ │ └── __init__.py
│ │ │ └── api_wkp.py
│ │ └── __init__.py
│ │ └── main.py
│ ├── api/
│ │ # Interface usando Flask
| │ └── __init__.py
│ │ └── api.py
│ │     # Onde inicializa o flask e as rotas
│ │ └── routes.py
│ │     # Centraliza os Endpoints
│ │ └── controller.py
│ │     # Faz a conexão com o crew
│ └── main.py
│ └── .env 
│     # Armazena as variaveis de ambiente
│     # Normalmente fica oculto pelo gitgnore
│     # mas como o intuito é testar o código
│     # vai ficar livre
│ └── requirements.txt
│     # Lista de dependências
│ └── README.md
│ └── LICENSE 
```

### 2. Criar uma ferramenta personalizada
- [x] Fazer uma **tool personalizada** xque:
    - [x] Acesse a API da Wikipedia.
    - [x] Realizar o request.
    - [x] Fazer o return dos dados para o agente.

### 3. Criar os agentes
- [x] Estudar a documentação do CrewAI para aperfeiçoamento.
- [x] Fazer pelo menos **2 agentes** com CrewAI: 
    - (ideias de agentes foram o search e write)
    - [x] Um agente que **pesquisa** informações na Wikipedia.
    - [x] Um agente que **escreve** o artigo com base nas informações.

### 4. Gerar o artigo final
- [ ] O sistema precisa gerar um **artigo com no mínimo 300 palavras**.
- [ ] Usar o **Pydantic** para organizar os dados do artigo (ex: título, conteúdo, tema).

### 5. Criar uma API para rodar o sistema
- [ ] Fazer uma API com o **Flask**.
    - [ ] Criar um endpoint onde para mandar o tema e recebe o artigo pronto.
    - [ ] Pegar o artigo em JSON e transformar para artigo textual.

### 6. Organizar e documentar o projeto
- [ ] Separar bem os arquivos: agentes, tools, crew, API e outros.
- [ ] Deixar o código bem comentado para explicar como tudo funciona.
- [ ] Complementar o **README.md** com:
    - [ ] O que é o projeto.
    - [ ] Como rodar.
    - [ ] Como usar a API.
    - [ ] Publicar o repositório no GitHub
    - [ ] Manter o código aberto (público)

### 7. Concluir o projeto
- [ ] Subir o projeto em um repositório **público** e fazer a entrevista apresentando o projeto.

---

## 🧪 Como Rodar o Projeto

- Siga os passos abaixo para configurar e executar o projeto localmente:
1. **Crie uma Virtual Environment**
    - Para garantir que as dependências do projeto fiquem isoladas, crie uma virtualenv.
    > cd c:\

    > python -m venv CreAI_ITec
2. **Ative a Virtual Environment**
    - Ative a virtualenv criada:
    > c:\CrewAi_ITec\Scripts\activate
3. **Instale as Dependências**
   - Com a virtualenv ativa, instale os pacotes listados no arquivo `requirements.txt`:
   > pip install -r requirements.txt
4. **Execute o Projeto**
    - Por fim, rode o arquivo principal:
    > python app/main.py


---

## Trabalho "offtopic".
### Serve apenas para registrar o que fiz, no fim, irei apagar.
- [x] Como vou usar LLM neste projeto:
    - Exemplo de código que desenvolvi para relembrar
    ```
        from crewai import Agent
        from langchain_google_genai import ChatGoogleGenerativeAI

        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=<api>)

        pesquisador = Agent(
            role="Pesquisador da Wikipedia",
            goal="Pesquisar sobre o tema solicitado",
            backstory="É especialista em encontrar informações confiáveis e rápidas.",
            llm=llm,
            tools=[<tool>],
            verbose=True
        )
    ```
- [x] Configurar o Gemini e como utiliza-lo melhor.
- [x] O CrewAI não precisa de APY_KEY.
- [x] A API da wikipedia não precisa de Cadastro.
- [ ] Definir a engenharia de prompt adequada
    - Atualmente, pensei em:
    ```
        Introdução: "Você está criando um arigo informativo para web."
        Trabalho: "Escreva um artigo com, no minimo 300 palavras sobre o tema escolhido, usando linguagem simples de fácil entendimento."
        Formatação: "Formate o texto em parágrafos, começando por uma introdução clara, desenvolvimento com fatos e uma conclusão interessante."
        Fontes: "Utilize apenas os dados extraídos da Wikipedia. Não sendo permitido criar fatos que não foram falados lá."
        Estilo de escrita: "Use um tom informativo, amigável e envolvente. Evite palavras técnicas."
    ```