from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from langchain.agents import create_pandas_dataframe_agent

from langchain.llms import OpenAI
import pandas as pd

import streamlit as st
import streamlit.components.v1 as components

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# +
# api=st.text_input('API KEY',"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", key='api')

# +
# api=st.text_input('API KEY',"", key='api')

# +

try:
    api=st.secrets["api_key_open"]
except:
    api=""
# api="s"
# -

import os
# os.environ["OPENAI_API_KEY"] = "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"

os.environ["OPENAI_API_KEY"] = api

Model="gpt-3.5-turbo"





# +
# llm = OpenAI(temperature=0, verbose=True)

# +
# df = pd.read_pickle('df_compras_2023_Q1_23052023.pkl')

# +
# agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df[["description","awardsvalue","date","award_naname"]].dropna(), verbose=True)

# +
# st.title("Bot de Consultas para Proceso de Compras Públicas")

# +
# st.subheader("Botservatorio")

# +
# st.markdown("Consulta utilizando INTELIGENCIA ARTIFICIAL datos sobre los procesos de compras públicas")

# +
# import streamlit as st

# title = st.text_input("",value='', key="input")

# respuesta=agent.run(title)

# st.write( respuesta)
# -

df = pd.read_pickle('data_today_SIE.pkl')

# +
# df

# +


# # Storing the chat
# if 'generated' not in st.session_state:
#     st.session_state['generated'] = []

# if 'past' not in st.session_state:
#     st.session_state['past'] = []

# +
# if 'something' not in st.session_state:
#     st.session_state.something = ''

# def submit():
#     st.session_state.something = st.session_state.widget
#     st.session_state.widget = ''

# st.text_input('Something', key='widget', on_change=submit)

# st.write(f'Last submission: {st.session_state.something}')

# +
# st.caption('Ejemplos de Consultas que le Puedes Hacer al BotServatorio')

# +
# code_1 = '''Total de Procesos por  Fecha de Publicación  en mayo'''
# st.code(code_1)
# code_2 = '''Las  3  Entidades Contratantes Con Presupuesto Referencial Total(sin iva)   mayores a 10000'''
# st.code(code_2)
# code_3 = ''' Cuales son las 3 Provinciaa/Cantones que mas Procesos tienen'''
# st.code(code_3)
# code_4 = '''Cual es el Porcentaje de Procesos que estan en Estado del Proceso  igual a  Desierta'''
# st.code(code_4)
# -

# We will get the user's input by calling the get_text function
def get_text():
    # input_text = st.text_input("You: ","Hello, how are you?", key="input")
    input_text=st.text_input('', key='widget')
    # st.write(f'Last submission: {st.session_state.something}')
    
    # input_text=st.session_state.something
    
    promp=f"Responde Exageradamente Formal a la sigueinte pregunta , y si la pregunta te pide un listado siempre en formato Markdown :{input_text}"
    return promp


user_input = get_text()
# user_input = "NUmero de columnas"

# +
# st.spinner(text="En progreso")

# +
# st.success(output,icon='✅')
# +

try:
    if st.button('Analizar'):
        with st.spinner(f'Analizando procesos para obtener respuesta...'):
            llm = OpenAI(model_name=Model, temperature=0.9, verbose=True)
            agent = create_pandas_dataframe_agent(OpenAI(temperature=0.8), df, verbose=True)
            output = agent.run(user_input)
            if 'stopped' in output:
                st.success("Woops! Eso nos está tomando más tiempo que el esperado: por favor vuelve a intentar",icon='✅')
            else:
                st.success(output,icon='✅')
    else:
        pass
except:
    st.error('Favor escribe tu pregunta de forma más específica e intenta nuevamente', icon="🚨")
