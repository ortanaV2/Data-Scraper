import json
import os
import pdfplumber
import re
from docx import Document

while True:
    directory = "./DATA"
    search_key = input("\nEnter keyword: ")

    #scrap directory-data
    data_cache = []
    for data_name in os.listdir(directory):
        dir = os.path.join(directory, data_name)

        #txt-data scrap
        if data_name.endswith(".txt"):
            with open(dir, "r", encoding="utf-8") as txt_datei:
                content = txt_datei.read()

        #pdf-data scrap
        elif data_name.endswith(".pdf"):
            text = []
            with pdfplumber.open(f"./DATA/{data_name}") as pdf:
                for page in pdf.pages:
                    text.append(page.extract_text())
            content = " ".join(text)
            raw = content.split()
            content = " ".join(raw)

        #docx-data scrap
        elif data_name.endswith(".docx"):
            doc = Document(f"./DATA/{data_name}")
            text = []
            for paragraph in doc.paragraphs:
                text.append(paragraph.text)
            content = " ".join(text)
            words = re.findall(r"\S+", content)
            content = " ".join(words)

        else:
            content = None
        #save scrap-data
        data_cache.append([
            data_name,
            content
        ])

    matches = []
    for datapoint in data_cache:
        name = datapoint[0] #file_name
        content = datapoint[1] #file_content
        
        key_content = None
        if content is not None:
            key_content = content.split()
        
        #search keyword in file_name
        if search_key in name:
            matches.append(f"Filename: {name}")
        
        #search keyword in file_content
        if key_content is not None:
            word_count = 0
            for word in key_content:
                word_count+=1
                if search_key in word:
                    matches.append(f'Word({word_count}): "{search_key}" found in {name}')
    
    #output result
    if len(matches) > 0:
        print("\nMatches:\n"+"_"*35)
        for findings in matches:
            print(findings)
    else:
        print("\nNo matches found.")