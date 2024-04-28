from docx import Document
from open_ai.openai_api import OpenAI
import sys
class DocumentMaker:
    def __init__(self, path):
        self.document = Document(path)
        self.new_path = 'legal_notice_new.docx'
    
    def save(self):
        self.document.save(self.new_path)

    def replace_common(self, search_text, replace_text):
        for paragraph in self.document.paragraphs:
            for run in paragraph.runs:

                if search_text in run.text:
                    if search_text == "defect_des":
                        # run.text = OpenAI().get_response(replace_text)
                        run.text = "gg"
                        break
                    if search_text == "name_of_company":
                        # run.text = replace_text.upper()
                        run.text = "gg"
                        break
                    run.text = replace_text
        self.save()


