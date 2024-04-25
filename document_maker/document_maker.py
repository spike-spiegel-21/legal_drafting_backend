# from docx import Document
# import os
from open_ai.openai_api import OpenAI

#document_path = os.path.join('.', 'legal_notice_template.docx')
#path_of_template = './legal_notice_template.docx'
#dev-> TODO: What if any point is incomplete?
class DocumentMaker:
    #initialize path
    def __init__(self, path):
        #self.path = path
        self.document = Document(path)
        #change after database allotment
        self.new_path = 'legal_notice.docx'
    
    #save function
    def save(self):
        self.document.save(self.new_path)


    def replace_common(self, search_text, replace_text):
        for paragraph in self.document.paragraphs:
            for run in paragraph.runs:

                if search_text in run.text:
                    if search_text == "defect_des":
                        run.text = OpenAI().get_response(replace_text)
                        break
                    if search_text == "name_of_company":
                        run.text = replace_text.upper()
                        break
                    run.text = replace_text
        self.save()


