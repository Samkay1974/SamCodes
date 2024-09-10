import streamlit as st
# import AshesiLeague as AL


if __name__ == "__main__":
    st.write("Hello Streamlit")
    st.success("App runs successfully. It's now upto you to be creative Developer🤭")
    
    st.sidebar.button("Home")
    st.sidebar.button("Teams")
    st.sidebar.button("Groups")
    


def page2():
    st.title("Second page")

def page1():
    st.title("First Page")

pg = st.navigation([
    st.Page(page1, title="First page", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
])
if page1:
    st.switch_page("Pages/Teams.py")