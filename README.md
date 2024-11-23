# RAG Query System

## Introduction

This project implements a document query system using LightRAG, a state-of-the-art Retrieval-Augmented Generation (RAG) framework. LightRAG represents a significant advancement in RAG systems, offering advantages over traditional approaches like GraphRAG while maintaining lower computational costs.

### What is LightRAG?

LightRAG is a lightweight yet powerful RAG framework that enhances retrieval quality through:

- **Dual-View Retrieval**: Combines both lexical and semantic search capabilities
- **Local Structure Modeling**: Captures document relationships with hierarchical structures
- **Global Knowledge Integration**: Leverages knowledge graphs for comprehensive understanding
- **Cost-Effective Performance**: Achieves comparable or better results than GraphRAG with reduced computational overhead

Indexing Flow
https://camo.githubusercontent.com/fa79bd2d317163583e8acdeb7c28b16d10652cfcd92c4bab85cc00954ffb1888/68747470733a2f2f6c6561726e6f70656e63762e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032342f31312f4c696768745241472d566563746f7244422d4a736f6e2d4b562d53746f72652d496e646578696e672d466c6f7763686172742d7363616c65642e6a7067![image](https://github.com/user-attachments/assets/df1ed771-9b10-4d91-805b-836277cfd824)

Retrieval & Querying Flow
https://camo.githubusercontent.com/32d67fdd28040d24756373fc674cae593b9961c2ef84fb8a0a8104f33735ab2a/68747470733a2f2f6c6561726e6f70656e63762e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032342f31312f4c696768745241472d5175657279696e672d466c6f7763686172742d4475616c2d4c6576656c2d52657472696576616c2d47656e65726174696f6e2d4b6e6f776c656467652d4772617068732d7363616c65642e6a7067![image](https://github.com/user-attachments/assets/41a6cdf3-8ac8-4a9e-b8ab-984545a78261)


[Learn more about LightRAG](https://github.com/HKUDS/LightRAG)

## Features

- Implementation of LightRAG's dual-view retrieval system:
  - Naive search for direct matching
  - Hybrid search combining semantic and lexical features
- Support for different document types

## Graph Storage Options

### Neo4j Approach
- Enterprise-grade graph database integration
- Scalable for large document collections
- Requires Neo4j installation:
- requirements.txt includes neo4j
- The graph of BIAN document from neo4j
![image](https://github.com/user-attachments/assets/6d3ebbe6-f222-4ce5-a442-1401e9c02218)

### NetworkX Approach
- Lightweight in-memory graph solution
- Suitable for smaller document sets
- No additional installation needed
- Default configuration:

## Prerequisites

- Python 3.8+
- Neo4j Database (required for BAIN document querying)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/MacOS
python -m venv .venv
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install -e .
```

4. Insall Docker Desktop or any other local container host, & run
```bash
docker run \
    --restart always \
    --publish=7474:7474 --publish=7687:7687 \
    neo4j:5.25.1
```

5. Set environment variables for OpenAI and Neo4j
```bash
export OPENAI_API_KEY="sk-..."
export NEO4J_URI="neo4j://localhost:7687"
export NEO4J_USERNAME="neo4j"
export NEO4J_PASSWORD="password"
```

## Document Preparation

Two separate RAG storages are prepared using:
1. BIAN document - https://bian.org/wp-content/uploads/2020/10/BIAN-Semantic-API-Pactitioner-Guide-V8.1-FINAL.pdf
2. ARPA - Managing Data Risk - https://www.apra.gov.au/sites/default/files/Prudential-Practice-Guide-CPG-235-Managing-Data-Risk_1.pdf

The system expects documents to be in the `raw-docs` folder. If you have PDF files, they need to be converted to markdown format using PyMuPDF4LLM. In the raw-docs you will find that .md files already exists.

```python
import fitz  # PyMuPDF
from PyMuPDF4LLM import extract_text_from_pdf

# Convert PDF to markdown
with fitz.open("raw-docs/your-document.pdf") as doc:
    markdown_text = extract_text_from_pdf(doc)
    
    with open("raw-docs/output.md", "w", encoding="utf-8") as f:
        f.write(markdown_text)
```

## Project Structure

```
.
├── raw-docs/
│   ├── bian.md
│   └── CPG235.md
├── lightrag-demo.py
├── .venv/
└── README.md
```

## Usage

1. Run the main script:
```bash
python lightrag-demo.py
```

2. Choose the document you want to query:
   - Option 1: BAIN documentation
   - Option 2: APRA Data Regulation

3. Enter your question when prompted

4. View both naive and hybrid search results:
   - Naive search provides direct matching results
   - Hybrid search combines semantic understanding with lexical matching for more comprehensive answers

5. Choose your next action:
   - Ask another question
   - Change document
   - Exit the program

## Testing

To run the test cases:
```bash
python -m pytest lightrag-demo.py
```

## Working Directories

The system creates working directories for each document type:
- `./bian_neo4jWorkDir`: For BAIN documentation
- `./cpg235_workdir`: For APRA Data Regulation

These directories store the necessary indexes and cached data for the RAG system.

## Notes

- The system uses `gpt_4o_mini_complete` as the default LLM model, but can be configured to use other models
- For BIAN documentation, Neo4j storage is specifically used for graph operations
- LightRAG's dual-view retrieval can be adjusted through QueryParam settings for different use cases

## Error Handling

The system includes comprehensive error handling and logging. All errors are:
- Logged with timestamps
- Returned in the RAGResponse object
- Displayed to the user with appropriate context

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
