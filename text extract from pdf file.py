# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:29:33 2023

@author: User
"""

# extract the full text in a pdf file to a txt 

import PyPDF2

# Open the PDF file in read-binary mode
with open('ex06.pdf', 'rb') as pdf_file:  
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Create an empty string to store the extracted text
    text = ''

    # Loop through each page in the PDF file
    for page_num in range(len(pdf_reader.pages)):
        # Get the page object
        page = pdf_reader.pages[page_num]

        # Extract the text from the page
        page_text = page.extract_text()
        # Add the page text to the overall text string
        text += page_text

# Save the extracted text to a text file
with open('output.txt', 'w',encoding='UTF-8') as txt_file: #  to restore 'cp950' problem which is caused from "unicode text convert to cp950", add encoding='UTF-8' which change the encoding type to UTF-8
    txt_file.write(text)
