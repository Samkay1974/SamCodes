import streamlit as st

st.title("This is the homepage")
page_temp= """
background = 
"""

container_temp = """
<div style=" 
padding:50x;
background-color: #000;
color: #fff;
opacity: .5;">
This box uses opacity
</div>
"""

st.markdown("""
<style>
[data-testid="column"] {
    box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 1px 3px 0px;
    border-radius: 15px;
    padding: 5% 5% 5% 10%;}
</style>"""
, unsafe_allow_html=True)