import streamlit as st
from lib.ui import load_file_section, question_section

def main():
    st.set_page_config(page_title="Ask anything about database", page_icon="📊", layout="wide")
    st.title("DB Engineer")

    col1, col2 = st.columns([2, 3])

    with col1:
        df, context = load_file_section()

    with col2:
        if df is not None:
            question_section(df, context)

if __name__ == "__main__":
    main()
