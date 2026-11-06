git clone https://github.com/SEU-UTILIZADOR/enterprise-rag-assistant.git  # Baixa o repositório completo da nuvem do GitHub para o computador
cd enterprise-rag-assistant                                              # Entra na pasta do projeto recém-clonada
pip install -r requirements.txt                                          # Instala todas as bibliotecas necessárias listadas no ficheiro
$env:OPENAI_API_KEY="sua-chave-aqui"                                       # Define a chave de API da OpenAI no ambiente do terminal (PowerShell)
python src/ingest.py                                                     # Executa o script de ingestão para ler o documento e criar a base vetorial local
python src/query.py                                                      # Executa o script de consulta para fazer a pergunta à IA com base nos documentos
