## Enterprise RAG Assistant ##

Um assistente inteligente de recuperação de documentos (RAG) desenvolvido em Python, projetado para responder a perguntas corporativas com base estritamente em dados internos, eliminando alucinações da IA.

---

  ##  Arquitetura do Sistema

```mermaid
graph TD
    A[Documentos PDF/TXT] -->|Ingestão & Embedding| B[(Base Vetorial ChromaDB)]
    C[Pergunta do Utilizador] -->|Busca Semântica| B
    B -->|Contexto Relevante| D[LLM / OpenAI]
    C -->|Prompt + Contexto| D
    D -->|Resposta Precisa| E[Interface / Resposta Final]
