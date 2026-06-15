import streamlit as st
import os

pdf_path = os.path.join(os.path.dirname(__file__), "Policies.pdf")

with open(pdf_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="Download PDF",
    data=PDFbyte,
    file_name="Policies.pdf",
    mime="application/pdf"
)
