from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import io
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
async def get_answer(files: List[UploadFile] = File(...)):
    tables_list = []

    for file in files:
        if file.filename.endswith('.xls') or file.filename.endswith('.xlsx'):
            try:
                # Read the uploaded Excel file
                file_content = await file.read()  # Read the contents of the file
                
                if file_content is None:
                    raise HTTPException(status_code=400, detail=f"Failed to read file {file.filename}")
                
                excel_file = io.BytesIO(file_content)  # Convert to BytesIO for pandas to read
                
                # Process the Excel file and serialize tables
                tables = serialize_excel_tables(excel_file)
                tables_list.extend(tables)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Error processing file {file.filename}: {e}")
        elif file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail=f"CSV files are currently not supported: {file.filename}")
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported file type for file: {file.filename}")
    
    return {"tables": tables_list}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
