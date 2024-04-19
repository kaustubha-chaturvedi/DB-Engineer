import streamlit as st
import pandas as pd
from pandasql import sqldf
from .utils import groq_infer
from .prompt import generate_prompt
from .config import MAX_ATTEMPTS

def load_file_section():
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, encoding="latin1")
        df.columns = df.columns.str.replace(r"[^a-zA-Z0-9_]", "", regex=True)
        st.write("Here's a preview of your uploaded file:")
        st.dataframe(df)

        context = pd.io.sql.get_schema(df.reset_index(), "df").replace('"', "")
        st.write("SQL Schema:")
        st.code(context)

        return df, context
    return None, None

def question_section(df, context):
    question = st.text_input("Write a question about the data", key="question")

    if st.button("Get Answer", key="get_answer"):
        if question:
            attempt = 0
            while attempt < MAX_ATTEMPTS:
                try:
                    formatted_prompt = generate_prompt(context, question)
                    response = groq_infer(formatted_prompt)
                    final = response.replace("`", "").replace("sql", "").strip()
                    st.text("Query performed")
                    st.code(final)
                    result = sqldf(final, locals())
                    st.write("Answer:")
                    st.dataframe(result)
                    break
                except Exception as e:
                    attempt += 1
                    st.error(f"Attempt {attempt}/{MAX_ATTEMPTS} failed. Retrying...")
                    if attempt == MAX_ATTEMPTS:
                        st.error("Unable to get the correct query, refresh app or try again later.")
                    continue
        else:
            st.warning("Please enter a question before clicking 'Get Answer'.")
