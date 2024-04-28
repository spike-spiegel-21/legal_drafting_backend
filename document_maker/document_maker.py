from docx import Document
from langchain_community.llms.fake import FakeListLLM

class DocumentMaker:
    def __init__(self, path):
        self.document = Document(path)
        self.new_path = 'legal_notice_new.docx'
    
    def save(self):
        self.document.save(self.new_path)

    def replace_common(self, search_text, replace_text):
        response_str = "fake_llm_res\n"+replace_text
        responses = [response_str]
        llm = FakeListLLM(responses = responses)
        
        for paragraph in self.document.paragraphs:
            for run in paragraph.runs:
                if search_text in run.text:
                    if search_text == "defect_des":
                        run.text = llm.invoke("gg")
                        break
                    if search_text == "name_of_company":
                        run.text = replace_text.upper()
                        break
                    run.text = replace_text
        self.save()


