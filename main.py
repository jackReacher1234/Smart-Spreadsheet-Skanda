from helper_functions import fetch_document, extract_text_from_pdf, serialize_excel_tables, extract_text_from_csv, clean_text, answer_question

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
