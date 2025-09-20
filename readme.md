# Análise de Ameaças STRIDE com IA Open-Source

## 📖 Descrição do Projeto

Este projeto é a minha entrega para o desafio "Entendendo o Desafio de Projeto: Análise de Ameaças com IA Generativa" da DIO.

O objetivo era implementar uma solução capaz de analisar diagramas de arquitetura de software e gerar automaticamente um modelo de ameaças baseado na metodologia STRIDE. Em vez de utilizar a abordagem sugerida com Azure OpenAI, optei por um desafio adicional: **recriar a funcionalidade utilizando modelos de Inteligência Artificial de código aberto (open-source) e ferramentas totalmente gratuitas**, demonstrando a aplicação prática de conceitos de Deep Learning e MLOps.

## 🚀 Minha Abordagem: IA com Custo Zero

A principal modificação neste projeto foi a substituição do cérebro de IA. Em vez de uma API paga, construí uma solução em três camadas:

1.  **Cérebro de IA (Google Colab):** Utilizei um notebook no Google Colab com acesso a uma GPU gratuita para carregar e executar o modelo multimodal **LLaVA (Large Language and Vision Assistant)**. O modelo foi carregado de forma otimizada (quantizado em 4-bit) para operar dentro dos limites do ambiente gratuito.
2.  **Backend Intermediário (FastAPI):** Um "carteiro" leve rodando localmente, responsável por receber as requisições do frontend e encaminhá-las para o serviço de IA no Colab através de um túnel seguro.
3.  **Frontend (HTML/JS/Cytoscape.js):** A interface original do projeto, que permite o upload da imagem e a visualização gráfica da análise de ameaças retornada pela IA.

Essa arquitetura permitiu replicar a funcionalidade do projeto original sem nenhum custo, focando na engenharia de prompt e no manuseio de modelos de IA.

## 🛠️ Tecnologias Utilizadas

-   **Inteligência Artificial:**
    -   **Google Colab:** Para acesso a GPU gratuita.
    -   **PyTorch:** Framework base para o modelo de IA.
    -   **Hugging Face Transformers:** Para carregar e executar o modelo LLaVA.
    -   **BitsandBytes & Accelerate:** Para otimização e quantização do modelo.
-   **Backend:**
    -   **Python 3.10**
    -   **FastAPI:** Para criar a API intermediária.
    -   **Uvicorn:** Para servir a aplicação FastAPI.
    -   **Requests:** Para comunicar com o serviço no Colab.
-   **Frontend:**
    -   **HTML5 / CSS3 / JavaScript**
    -   **Cytoscape.js:** Para a visualização do grafo de ameaças.
-   **Conectividade:**
    -   **Ngrok:** Para criar um túnel seguro e uma URL pública para o serviço rodando no Colab.

## ⚙️ Como Executar o Projeto

Para replicar este projeto, siga os passos abaixo:

### 1. Cérebro de IA (Google Colab)

1.  Abra o Google Colab, crie um novo notebook e configure o ambiente de execução para **T4 GPU**.
2.  Copie o código do arquivo `Cerebro_AI.ipynb` deste repositório e cole em uma célula do notebook. ou abra o link https://colab.research.google.com/drive/1m_war5SPpnmSuZ-5hl6fH02T7LCq1BSS?usp=sharing
3.  Subistitua o "COLE SEU TOKEN AQUI" pelo codigo do seu TOKEN de autenticação do NGROK, Você pode obtê-lo gratuitamente em https://dashboard.ngrok.com/get-started/your-authtoken
4.  Execute a célula. Ao final, ela irá gerar e exibir uma **URL pública do Ngrok**. Copie esta URL.

### 2. Backend (Sua Máquina Local)

1.  Navegue até a pasta `module-1/01-introducao-backend`.
2.  Abra o arquivo `main.py` e cole a URL do Ngrok na variável `COLAB_API_URL`.
3.  Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    # Windows
    .\.venv\Scripts\Activate.ps1
    # Linux/Mac
    source .venv/bin/activate
    ```
4.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5.  Inicie o servidor:
    ```bash
    uvicorn main:app --reload --port 8001
    ```

### 3. Frontend

1.  Navegue até a pasta `module-1/02-front-end`.
2.  Abra o arquivo `index.html` em seu navegador.
3.  Preencha o formulário, faça o upload de uma imagem de arquitetura e clique em "Analisar Ameaças". Aguarde alguns minutos para a IA processar a requisição.

## 📸 Resultado

Ele Gera um Grafo com o resultado da analise STRIDE
ainda não conclui a resposta escrita.... se tiver tempo organizo aqui kk

## 🧠 Aprendizados

Este desafio foi uma jornada incrível. Os principais aprendizados foram:-   
**Leitura e Processamento de conteudo em modelos Multimodais:** Ler um Conteudo em Formato de imagem e receber comandos em formato de texto e fazer a analise dos dois em uma Deep Learning.
-   **Engenharia de Prompt na Prática:** A qualidade da análise da IA é diretamente proporcional à qualidade do prompt. Foi um exercício prático de como instruir um modelo a realizar uma tarefa complexa e a retornar dados em um formato estruturado (JSON).
-   **MLOps com Ferramentas Gratuitas:** Aprendi a carregar e servir um modelo de Deep Learning pesado utilizando apenas os recursos gratuitos do Google Colab, aplicando técnicas de otimização como a quantização para viabilizar a operação.
-   **Arquitetura de Sistemas Distribuídos:** O projeto, na prática, se tornou um sistema distribuído com três componentes se comunicando via rede (Frontend -> Backend Local -> Backend na Nuvem), o que reforçou conceitos de APIs e comunicação HTTP.

---
Feito com 💜 por Silas SJ Junior para a DIO.
