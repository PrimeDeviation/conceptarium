import streamlit as st
from . import knowledge


def paint():
    modality = st.selectbox('modality', ['text', 'image'],
                            ['text', 'image'].index(st.session_state.get('navigator_modality', 'text')), help='Select the type of query you want to search with.')

    if modality == 'text':
        input = st.text_area('input', height=100,
                             help='Enter the actual contents of your query.')
    elif modality == 'image':
        input = st.file_uploader(
            'input', help='Enter the actual contents of your query.')

    if st.button('jump', help='Click to search for thoughts based on the specified query.'):
        st.session_state['authorized_thoughts'] = knowledge.load(
            modality, input)
        st.session_state['navigator_modality'] = modality
        st.session_state['navigator_input'] = input
