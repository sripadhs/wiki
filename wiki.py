import wikipedia
import streamlit as sl
sl.title('Pywiki')
inp=sl.text_input('Search:')
if sl.button('Search'):
    sl.header(wikipedia.summary(inp))
