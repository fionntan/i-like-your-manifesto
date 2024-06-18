import os

import utils


# init
# def read_pdf(file_path):
#     try:
#         with open(file_path, 'rb') as file:
#             reader = PyPDF2.PdfFileReader(file)
#             text = ""
#             for page_num in range(reader.numPages):
#                 page = reader.getPage(page_num)
#                 text += page.extract_text()
#         return text
#     except Exception as e:
#         print(f"Error reading {file_path}: {e}")
#         return None


def process_pdfs(config: dict):
    raw_pdfs_path = config['data_paths']['raw_pdfs']
    # processed_texts_path = config['data_paths']['processed_texts']
    pdf_files = config['pdf_files']
    project_root = utils.get_project_root()
    for title, filename in pdf_files.items():
        pdf_path = os.path.join(raw_pdfs_path, filename)
        print(f"{pdf_path}")
        print(os.path.exists(pdf_path))
        # print(f"Processing {title} from {pdf_path}")
        # text = read_pdf(pdf_path)
        # if text:
        #     processed_text_path = os.path.join(processed_texts_path, f"{title}.txt")
        #     with open(processed_text_path, 'w') as text_file:
        #         text_file.write(text)
        #     print(f"Saved processed text to {processed_text_path}")
        # else:
        #     print(f"Failed to process {title}")


if __name__ == "__main__":
    config = utils.load_config()
    process_pdfs(config)
