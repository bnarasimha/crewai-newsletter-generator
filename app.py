import streamlit as st
import os
import sys
from pathlib import Path
from datetime import datetime
import pandas as pd
import base64

# Add the root directory to Python path
root_dir = Path(__file__).parent
sys.path.append(str(root_dir))

from src.crew import CrewExperiment

def display_pdf(pdf_path):
    """Display PDF in Streamlit"""
    with open(pdf_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def process_topic(topic: str):
    inputs = {'topic': topic}
    with st.spinner('Generating newsletter...'):
        CrewExperiment().crew().kickoff(inputs=inputs)
    return "report.pdf"

# Streamlit UI
st.title("Newsletter Generator")

# Input section
with st.form("newsletter_form"):
    topic = st.text_input("Enter a topic", placeholder="e.g., Artificial Intelligence")
    submitted = st.form_submit_button("Generate Newsletter")

# Process form submission
if submitted and topic:
    pdf_file = process_topic(topic)
    if pdf_file:
        st.success("Newsletter generated successfully!")
        
        # Display PDF
        st.subheader("Generated Newsletter")
        display_pdf(pdf_file)
        
        # Download button
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="Download PDF",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )

# Display history
if not st.session_state.history.empty:
    st.subheader("Newsletter History")