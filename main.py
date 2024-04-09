# Dataset based on #https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

import os
import logging
import chainlit as cl

import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-pro')


import db_utils
import gemini_utils

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info("Loading data...")
df = pd.read_csv("data/sales_data_sample.csv")
logging.info(f"Data Format: {df.shape}")

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None

@cl.on_chat_start
async def chat_st():

    logging.info("Converting to database...")
    database = db_utils.dataframe_to_database(df, "Sales")

    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    # cl.user_session.set('model',model)
    cl.user_session.set('chat_history',chat)
    cl.user_session.set('database',database)

@cl.on_message
async def main(msg:cl.Message):

    # model = cl.user_session.get('model')
    chat = cl.user_session.get('chat_history')
    database = cl.user_session.get('database')

    logging.info("Waiting for user input...")
    fixed_sql_prompt = gemini_utils.create_table_definition_prompt(df, "Sales")

    logging.info(f"Fixed SQL Prompt: {fixed_sql_prompt}")
    user_input = msg.content
    final_prompt = gemini_utils.combine_prompts(fixed_sql_prompt, user_input)

    logging.info(f"Final Prompt: {final_prompt}")
    logging.info("Sending to Gemini Pro...")
    response = chat.send_message(final_prompt)
    proposed_query_postprocessed = db_utils.handle_response(response)

    logging.info(f"Response obtained. Proposed sql query: {proposed_query_postprocessed}")
    result = db_utils.execute_query(database, proposed_query_postprocessed)
    final_response = gemini_utils.final_answer(user_input,result)

    logging.info(f"Result: {final_response}")

    await cl.Message(final_response).send()
# print(result)
