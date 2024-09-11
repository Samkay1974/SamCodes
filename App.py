import streamlit as st
import pages
# import AshesiLeague as AL


if __name__ == "__main__":
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Ashesi Football Platform</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    st.sidebar.button("Home")
    st.sidebar.button("Teams")
    st.sidebar.button("Groups")

    pages = {
        "Your account": [
            st.Page("pages/home.py", title="Home"),
            st.Page("pages/teams.py", title="Teams"),
        ],
    }

    pg = st.navigation(pages)
    pg.run()


    