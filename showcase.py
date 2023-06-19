import streamlit as st
import pandas

st.set_page_config(layout="wide")
# def style():
#     css = """
#     <link rel="preconnect" href="https://fonts.gstatic.com">
#         <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap" rel="stylesheet">
#     <style>
#     @font-face {
#         font-family: 'My Font';
#         font-style: normal;
#         src: url(assets/fonts/myfont.tff) format('truetype');;
#     }
#     .sidebar-text{
#         font-family: 'Roboto', sans-serif;
#     }
#     .standard-text{
#         font-family: 'My Font';
#     }
#     </style>
#     """
#     st.markdown(css,unsafe_allow_html=True)
# style()

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Nguyen Xuan Phong")
    content = """Hi. My name is Nguyen Xuan Phong. 
    Currently I am a 2nd year student of Posts & Telecommunications Institue of Techcology. 
    I am on my way to learning to become a back-end developer. 
    And the first language I learned was Python.
"""
    st.info(content)
content2 = """<strong>Here are some of my small projects. Hope it can be of help to you<strong>"""
st.write(content2, unsafe_allow_html=True)

df = pandas.read_csv("data.csv", sep=";")
col3, empty_colum, col4 = st.columns([1.5, 0.5, 1.5])
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source code](row['url'])")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source code](row['url'])")

