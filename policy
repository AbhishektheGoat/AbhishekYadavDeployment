import streamlit as st

with open("sample.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="Download PDF",
    data=PDFbyte,
    file_name="sample.pdf",
    mime="application/pdf"
)
