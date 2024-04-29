import PyPDF2
import google.generativeai as genai

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to generate a summary from extracted text
def generate_summary(text):

    # Initialize the GenerativeAI model
    txt_model = genai.GenerativeModel('gemini-pro')
    # Give the prompt to the model and get the response
    response = txt_model.generate_content(f"generate summary for the text {text}")

    #print(response.text)
    summary = response.text
    return summary

# Example usage
if __name__ == "__main__":
    pdf_file_path = ".\\pdf\\example.pdf"  # Path to your PDF file
    text = extract_text_from_pdf(pdf_file_path)
    #print("Text:")
    #print(text)
    summary = generate_summary(text)
    print("\nSummary:")
    print(summary)
