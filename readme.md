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

## 1. – Estruturar o projeto.
- Ir atualizando conforme update
- [ ] Versão final do projeto

## 1.1. - Atual estrutura do projeto
- app/
    - agents/
        - *search_agent.py*
        - *writer_agent.py*
    - tools/
        - *wikipedia_tool.py*
    - *main.py*
- api/
    - *api.py*
- .env
- requirements.txt
- readme.md
- LICENSE (vou usar a MIT do github)

### 2. Criar os agentes
- [ ] Estudar a documentação do CrewAI para aperfeiçoamento.
- [ ] Fazer pelo menos **2 agentes** com CrewAI: 
    - (ideias de agentes foram o search e write)
    - [ ] Um agente que **pesquisa** informações na Wikipedia.
    - [ ] Um agente que **escreve** o artigo com base nas informações.

### 3. Criar uma ferramenta personalizada
- [ ] Fazer uma **tool personalizada** que:
    - [ ] Acesse a API da Wikipedia.
    - [ ] Realizar o request.
    - [ ] Fazer o return dos dados para o agente.

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

## 📖 Fontes para Estudos

- [CrewAI Documentation](https://docs.crewai.com/introduction)
- [CrewAI Tools](https://docs.crewai.com/concepts/tools)
- [Curso da DeepLearning.AI sobre Sistemas Multiagente](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)

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