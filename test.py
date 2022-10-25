import streamlit as st
import time

with st.spinner('Wait for it...'):
    time.sleep(5)

st.success('Done!')
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
