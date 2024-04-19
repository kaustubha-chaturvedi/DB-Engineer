# DB Engineer

This project implements an DB engineer which can perform SQL queries on a .csv file.
The DB engineer utilizes a GROQ APIs to interpret natural language questions and generate SQL queries.
I also have implemented a Mistral and Gemma API to interpret natural language questions and generate SQL queries, they are more accurate than GROQ API but I  intend to use them for future work, stay tuned.

## Features

- **Natural Language Interface**: Users can ask questions in natural language.
- **CSV Input**: The DB engineer accepts a .csv file as input.
- **SQL Query Generation**: The DB engineer generates SQL queries based on the input question.
- **Backend Options**: The DB engineer can use the Groq API in the backend.

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/kaustubha-chaturvedi/db-engineer.git
   ```

2. Install dependencies:

    ```sh
   pip  install -r requirements.txt
   ```

## Usage

1. Ensure your .csv file is formatted correctly.
2. Run the DB engineer:

   ```sh
   streamlit run main.py
   ```

## Demo Video

[![Demo Video](demo.webm)](demo.webm)
