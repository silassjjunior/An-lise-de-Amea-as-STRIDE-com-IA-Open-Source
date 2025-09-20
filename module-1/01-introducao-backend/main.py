import requests
from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA APLICAÇÃO FASTAPI
# -----------------------------------------------------------------------------
app = FastAPI(
    title="STRIDE Threat Model Analyzer - Backend",
    description="API que serve como intermediário entre o frontend e o serviço de IA no Colab.",
    version="1.0.0"
)

# Configuração do CORS (Cross-Origin Resource Sharing)
# Permite que o frontend (rodando em outra porta/origem) se comunique com este backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, restrinja para o domínio do seu frontend.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# PASSO CRÍTICO: INSERIR A URL DO SEU CÉREBRO DE IA
# -----------------------------------------------------------------------------
# Cole aqui a URL pública gerada pelo seu notebook do Google Colab.
# Exemplo: "https://1a2b-34-56-78-90.ngrok.io/analyze"
COLAB_API_URL = "https://2e72c0b69a37.ngrok-free.app/analyze"

# -----------------------------------------------------------------------------
# ENDPOINT PRINCIPAL DA API
# -----------------------------------------------------------------------------
@app.post("/analyze", summary="Analyze Threat Model", tags=["Analysis"] )
async def analyze_threat_model(
    description: str = Form(...),
    image: UploadFile = File(...)
):
    """
    Recebe uma imagem e uma descrição do frontend, repassa para o serviço de IA
    no Colab e retorna a análise de ameaças.
    """
    if COLAB_API_URL == "COLE_A_SUA_URL_DO_NGROK_AQUI/analyze":
        raise HTTPException(
            status_code=500,
            detail="ERRO DE CONFIGURAÇÃO: A URL do Colab (COLAB_API_URL) não foi definida no código do backend."
        )

    # Prepara os dados para enviar ao Colab. O formato (files e data)
    # deve corresponder ao que a API Flask no Colab espera.
    files = {'image': (image.filename, await image.read(), image.content_type)}
    data = {'description': description}

    print(f"🚀 Encaminhando requisição para o Cérebro de IA em: {COLAB_API_URL}")

    try:
        # Faz a requisição para o nosso cérebro no Colab.
        response = requests.post(COLAB_API_URL, files=files, data=data, timeout=300) # Timeout de 5 minutos

        # Lança um erro HTTP se a resposta do Colab não for bem-sucedida (ex: 4xx, 5xx).
        response.raise_for_status()

        print("✅ Resposta recebida do Cérebro de IA. Retornando para o frontend.")
        # Retorna a resposta JSON do Colab diretamente para o frontend.
        return response.json()

    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="A requisição para o serviço de IA demorou muito (timeout).")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Erro ao conectar com o serviço de IA no Colab: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ocorreu um erro inesperado no backend: {e}")

@app.post("/suggest-improvements", summary="Get Improvement Suggestions", tags=["Analysis"])
async def suggest_improvements(analysis: dict):
    """
    Endpoint mockado para lidar com a chamada de sugestões do frontend.
    No futuro, isso poderia fazer outra chamada à IA.
    """
    print("✅ Requisição de sugestão de melhorias recebida (mock).")
    # Simplesmente retornamos uma resposta vazia ou uma mensagem padrão.
    return {"suggestions": ["Funcionalidade de sugestão ainda não implementada.", "Foco na análise STRIDE principal."]}


# Bloco para permitir a execução direta do script com 'python main.py'
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
