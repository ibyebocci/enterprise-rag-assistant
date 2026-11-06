

```bash
git clone [https://github.com/SEU-UTILIZADOR/enterprise-rag-assistant.git](https://github.com/SEU-UTILIZADOR/enterprise-rag-assistant.git)
cd enterprise-rag-assistant
pip install -r requirements.txt
$env:OPENAI_API_KEY="sua-chave-aqui"
python src/ingest.py
python src/query.py
