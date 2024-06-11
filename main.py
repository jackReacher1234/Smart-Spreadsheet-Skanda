from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from helper_functions import fetch_document, extract_text_from_pdf, give_serialized_string, extract_text_from_csv, clean_text, answer_question, serialize_excel_tables

app = FastAPI()

class QuestionRequest(BaseModel):
    document_urls: str
    user_question: str

class SerializeTableRequest(BaseModel):
    document_urls: str

@app.post("/answer_question/")
async def get_answer(request: QuestionRequest):
    document_urls_list = request.document_urls.split(',')
    combined_text = ""

    for url in document_urls_list:
        url = url.strip()
        document = fetch_document(url)
        
        if url.endswith('.pdf'):
            text = extract_text_from_pdf(document)
        elif url.endswith('.xls') or url.endswith('.xlsx'):
            text = give_serialized_string(document)
        elif url.endswith('.csv'):
            text = extract_text_from_csv(document)
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported file type for URL: {url}")
        
        combined_text += " " + text

    cleaned_text = clean_text(combined_text)
    answer = answer_question(cleaned_text, request.user_question)
    return {"answer": answer}

@app.post("/give_tables/")
async def get_answer(request: SerializeTableRequest):
    document_urls_list = request.document_urls.split(',')

    for url in document_urls_list:
        url = url.strip()
        document = fetch_document(url)
        
        if url.endswith('.pdf'):
            tables = []
        elif url.endswith('.xls') or url.endswith('.xlsx'):
            tables = serialize_excel_tables(document)
        elif url.endswith('.csv'):
            tables = []
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported file type for URL: {url}")
        
    return {"tables": tables}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
