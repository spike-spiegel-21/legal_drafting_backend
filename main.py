import json
from typing import Union

from fastapi import FastAPI, Body, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from document_maker.document_maker import DocumentMaker
path_of_template = "legal_notice_template.docx"

def get_document_maker():
    return DocumentMaker(path_of_template)

app = FastAPI()

# Allow all origins, methods, and headers. Adjust these settings based on your needs.
origins = [
    "http://localhost",
    "http://localhost:3000",  # Add your React app's address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


#post route for fetching form data
@app.post("/process_json_data")
def process_json_data(json_data: dict = Body(...), document_maker: DocumentMaker = Depends(get_document_maker)):
    # Your processing logic goes here
    document_maker.replace_common("name_of_company",json_data.get("name_of_company"))
    document_maker.replace_common("name_of_entity",json_data.get("name_of_entity"))
    document_maker.replace_common("address_of_entity",json_data.get("address_of_entity"))
    document_maker.replace_common("date_of_rec",json_data.get("date_of_rec"))
    document_maker.replace_common("amount_of_rec",json_data.get("amount_of_rec"))
    document_maker.replace_common("defect_des",json_data.get("defect_des"))
    document_maker.replace_common("amount_to_get",json_data.get("amount_to_get"))
    document_maker.replace_common("contact_of_user",json_data.get("contact_of_user"))
    document_maker.replace_common("email_of_user",json_data.get("email_of_user"))

    
    return FileResponse('./legal_notice_new.docx', filename='legal_notice.docx')








