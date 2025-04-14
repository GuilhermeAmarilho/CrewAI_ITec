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
# tem que alterar pois mudei a forma de criação do crew
CrewAI_ITec/
│ ── app/ 
│ │ └── agents/
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

## Documentando o que fiz
- Engenharia de prompt - Elementos de uma boa query:
    - Instrução:
        - uma tarefa ou instrução específica que você deseja que o modelo execute
    - Contexto:
        - pode envolver informações externas ou contexto adicional que pode direcionar o modelo para melhores respostas
    - Dados de entrada:
        - é a entrada ou pergunta para a qual estamos interessados em encontrar uma resposta
    - Indicador de saída:
        - indica o tipo ou formato da saída.
    - Conteúdo aprendido desse [site](https://www.promptingguide.ai/pt).
- CrewAI
    - Primeiro, eu criei um projeto manualmente, mas estava sempre usando a LLM da OpenAI, mesmo com o .env configurado para Gemini. Com isso, dei um passo para tras e fui passo a passo seguindo a documentação.
    - QuickStart
        - Baixando UV
            > powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        - Instalando o CrewAI
            > uv tool install crewai
        - Criando a estrutura do projeto
            > crewai create crew <nome>
        - Vai ser necessário informar a LLM e a API_KEY
    - Conteúdo aprendido nesses sites:
        - [Instalação do CrewAI](https://docs.crewai.com/installation)
        - [Primeiros passos](https://docs.crewai.com/quickstart)
        - [Usando o arquivo .yaml para as tasks](https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended)
        - [Usando o arquivo .yaml para os agentes](https://docs.crewai.com/concepts/agents#yaml-configuration-recommended)
    - <Desabafo> - Caso alguem esteja lendo essa parte. Programação é um negócio daora né? O programa não rodava e puxava o LLM da OpenAi mesmo eu configurando para gemini. deixei o final de semana parado, e voltei segunda, refiz o código, e tcharam, funcionou! 
    - (づ￣ 3￣)づ