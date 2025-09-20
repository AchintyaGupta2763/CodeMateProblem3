# Deep Researcher Agent (prototype)

## Setup
1. Create a Python venv and activate:
   python -m venv venv
   source venv/bin/activate   # on Windows: venv\Scripts\activate

2. Install dependencies:
   pip install -r requirements.txt

3. Set environment variables (optional):
   export MONGODB_URI="mongodb://localhost:27017"
   export DB_NAME="deep_researcher"

4. Run Streamlit:
   streamlit run streamlit_app.py

5. Upload PDF/TXT/DOCX files via the UI, then ask research queries.

## Notes
- Embeddings use `sentence-transformers/all-MiniLM-L6-v2`.
- Generation uses `google/flan-t5-small`. Swap in larger generation models in config for improved reasoning.
