
import streamlit as st

import g4f

from g4f.Provider import (
    GptGo
)

st.title("Business Warehouse Bot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Welcome to the Business Warehouse Advise Chatbot!"}]

    st.write(
        '- This chatbot can offer advise on how to improve your business.'
    )

    st.write(
        '- Write `help` to see a list of commands'
    )

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():    
    st.session_state.messages.append({"role": "user", "content": prompt})

    if prompt == 'help':
        st.write(
            """
            - What are the latest trends in data warehousing?
            - Can you explain the benefits of cloud-based data warehouses?
            - I need advice on choosing a data warehouse for a small business.
            - What are the best practices for data warehouse management?
            - How can I improve data security in my data warehouse?
            - Tell me about the challenges in scaling data warehouses.
            - What tools are recommended for data analytics in large warehouses?
            - How does data warehousing support business intelligence?
            - What are the cost implications of data warehouse expansion?
            - I'm considering a migration to a new data warehouse, what should I consider?
            - What's the impact of big data on traditional data warehousing?
            - Can you help me understand data warehouse architecture?
            - How does data warehousing integrate with IoT devices?
            - What are some effective data warehousing strategies for e-commerce?
            - How can I ensure data quality in my data warehouse?
            """
        )
    else:
        st.chat_message("user").write(prompt)

        lastMessages = st.session_state.messages[-2:]

        if len(lastMessages) == 0:
            lastMessages = [{"role": "user", "content": " "}]

        # Set with provider
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.GptGo,
            messages=[
                {'role': 'system', 'content': 'You are a business advisor. Your job is to advise people on how to improve their business.'},
                {'role': 'system', 'content': 'You are talking to a small business owner who wants to improve their business.'},
            ] + lastMessages + [{"role": "user", "content": prompt}]
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": response})

        st.chat_message("assistant").write(response)
