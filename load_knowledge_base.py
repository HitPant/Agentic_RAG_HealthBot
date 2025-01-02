from phi.knowledge.pdf import PDFKnowledgeBase, PDFReader
from phi.vectordb.pgvector import PgVector, SearchType
from phi.embedder.mistral import MistralEmbedder
from phi.document.chunking.document import DocumentChunking


# embeddings = OpenAIEmbedder().get_embedding("Embed me")

# path to the directory containing your PDF files
pdf_directory_path = "health_assistant\pdf_data"

db_url="postgresql+psycopg://ai:ai@localhost:5532/ai"

# Initialize the PDFKnowledgeBase with the directory path
knowledge_base = PDFKnowledgeBase(
    path=pdf_directory_path,
    vector_db=PgVector(
        table_name="v2_health_insurace_data",
        db_url=db_url,
        search_type=SearchType.hybrid,
        embedder=MistralEmbedder()
    ),
    chunking_strategy=DocumentChunking(chunk_size=1024, overlap=20),
    reader=PDFReader(chunk=True),  # Optional: Configure the PDFReader as needed
)
# Load the knowledge base
# knowledge_base.load(upsert=True)

