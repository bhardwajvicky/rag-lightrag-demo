import os
import logging
from typing import Optional
from dataclasses import dataclass
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete

@dataclass
class RAGResponse:
    naive_result: str
    hybrid_result: str
    status: str
    error: Optional[str] = None

class RAGQueryManager:
    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.logger = logging.getLogger(__name__)
        self._setup_logging()
        
    def _setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def query(self, rag, question: str) -> RAGResponse:
        try:
            naive_result = rag.query(question, param=QueryParam(mode="naive"))
            hybrid_result = rag.query(question, param=QueryParam(mode="hybrid"))
            
            self._print_results(naive_result, hybrid_result)
            
            return RAGResponse(
                naive_result=naive_result,
                hybrid_result=hybrid_result,
                status="success"
            )
        except Exception as e:
            self.logger.error(f"Error during query: {str(e)}")
            return RAGResponse(
                naive_result="",
                hybrid_result="",
                status="error",
                error=str(e)
            )
    
    def _print_results(self, naive_result: str, hybrid_result: str):
        print("\n" + "="*50)
        print("NAIVE SEARCH RESULTS")
        print("="*50)
        print(naive_result)
        print("="*50)
        
        print("\n" + "="*50)
        print("HYBRID SEARCH RESULTS")
        print("="*50)
        print(hybrid_result)
        print("="*50 + "\n")

#########
# Uncomment the below two lines if running in a jupyter notebook to handle the async nature of rag.insert()
# import nest_asyncio
# nest_asyncio.apply()
#########

def main():
    while True:
        file_choice = input("Which file do you want to use for RAG \n 1. BAIN \n 2. APRA Data Regulation \n")
        if file_choice == "1":

            WORKING_DIR = "./bian_neo4jWorkDir"
            if not os.path.exists(WORKING_DIR):
                os.mkdir(WORKING_DIR)
            rag = LightRAG(
                working_dir=WORKING_DIR,
                llm_model_func=gpt_4o_mini_complete,  # Use gpt_4o_mini_complete LLM model
                graph_storage ="Neo4JStorage"
                # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
            )

            with open("./raw-docs/bian.md", "r", encoding="utf-8") as f:
                rag.insert(f.read())

        elif file_choice == "2":

            WORKING_DIR = "./cpg235_workdir"
            if not os.path.exists(WORKING_DIR):
                os.mkdir(WORKING_DIR)
            rag = LightRAG(
                working_dir=WORKING_DIR,
                llm_model_func=gpt_4o_mini_complete,  # Use gpt_4o_mini_complete LLM model
                # llm_model_func=gpt_4o_complete  # Optionally, use a stronger model
            )

            with open("./raw-docs/CPG235.md", "r", encoding="utf-8") as f:
                rag.insert(f.read())

        manager = RAGQueryManager(WORKING_DIR)
        
        # Ask question
        question = input("\n\n***What question do you want to ask the RAG? \n")
        response = manager.query(rag, question)
        
        while True:
            print("\nWhat would you like to do next?")
            print("1. Ask another question")
            print("2. Change RAG document")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == "1":
                break  # Break inner loop to ask new question
            elif choice == "2":
                # Logic to change RAG document would go here
                print("Changing RAG document...")
                break
            elif choice == "3":
                print("Thank you for using the RAG system. Goodbye!")
                return  # Exit the program
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Test cases
def test_rag_query_manager():
    """
    To run tests: python -m pytest lightrag-demo.py
    """
    manager = RAGQueryManager("./test_workdir")
    # Add test cases here
