import requests
from io import BytesIO
import fitz
import pandas as pd

from openai import OpenAI
from openai import AuthenticationError
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_document(source):
    if source.startswith('http://') or source.startswith('https://'):
        response = requests.get(source)
        response.raise_for_status()
        return BytesIO(response.content)
    elif os.path.exists(source):
        return source
    else:
        raise FileNotFoundError(f"No such file or URL: {source}")
    
def extract_text_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    return ' '.join(df.fillna('').astype(str).values.flatten())

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def serialize_excel_tables(excel_file):
    df = pd.read_excel(excel_file, header=None)
    tables = []
    current_table = []
    empty_row_count = 0
    
    # Iterate through each row
    for index, row in df.iterrows():
        # Check if the row is completely empty
        if row.isnull().all():
            empty_row_count += 1
        else:
            if empty_row_count == 1:
                # Single empty row indicates the end of a table
                if current_table:
                    tables.append(current_table)
                    current_table = []
            # Reset empty row counter
            empty_row_count = 0
            
            # Add the non-empty row to the current table
            current_table.append(row.astype(str).tolist())
    
    # Add the last table if it exists
    if current_table:
        tables.append(current_table)
    # Serialize each table to a string
    serialized_tables = []
    for table in tables:
        table_text = '\n'.join(['\t'.join(row) for row in table])
        serialized_tables.append(table_text)
    
    # Join all the tables into one single string
    result_text = '\n\n'.join(serialized_tables)
    
    return result_text

def clean_text(text):
    return ' '.join(text.split())

def get_openai_client(api_key):
    try:
        client = OpenAI(api_key=api_key)
        # Perform a minimal request to validate the API key
        client.models.list()
        return client
    
    except AuthenticationError as e:
        raise ValueError("Invalid OpenAI API key.") from e
    
    except Exception as e:
        raise

def answer_question(text, question):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai_client = get_openai_client(openai_api_key)

    completion = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
            {"role": "user", "content": question}
        ]
    )
    return completion.choices[0].message.content

def main():
    document_urls = input("Enter the document URLs separated by commas:\nExamples:\ntests/example_0.xlsx\nhttps://github.com/CapixAI/Smart-Spreadsheet/raw/main/tests/example_0.xlsx\n\n").split(',')
    user_question = input("\nEnter your question:\n")
    
    combined_text = ""

    for url in document_urls:
        url = url.strip()
        document = fetch_document(url)
        
        if url.endswith('.pdf'):
            text = extract_text_from_pdf(document)
        elif url.endswith('.xls') or url.endswith('.xlsx'):
            text = serialize_excel_tables(document)
        elif url.endswith('.csv'):
            text = extract_text_from_csv(document)
        else:
            raise ValueError(f"Unsupported file type for URL: {url}")
        
        combined_text += " " + text
    cleaned_text = clean_text(combined_text)
    answer = answer_question(cleaned_text, user_question)
    print("Answer:", answer)

if __name__ == "__main__":
    main()
