from langchain_core.prompts import PromptTemplate

template = """You are a powerful text-to-SQL model. Your job is to answer questions about a database. You are given a question and context regarding one or more tables. Dont add \n characters.
Do not include "SELECT short\_name, long\_name" this type of queries which have backslash in them.
You must output the SQL query that answers the question in a single line.

### Input:
`{question}`

### Context:
`{context}`

### Response:
"""

prompt = PromptTemplate.from_template(template=template)

def generate_prompt(context, question):
    input = {"context": context, "question": question}
    formatted_prompt = prompt.invoke(input=input).text
    return formatted_prompt
