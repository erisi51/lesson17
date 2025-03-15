import streamlit as st

""""col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.header("Column 1")
    st.write("This is content of col1")

with col2:
        st.header("Column 2")
        st.write("This is content of col2")

with col3:
    st.header("Column 3")
    st.write("This is content of col3")

with col4:
    st.header("Column 4")
    st.write("This is content of col4")""""


with st.form("my form", clear_on_submit=True):
    name = st.text_input('Name')
    age = st.slider('Age', min_value=0 , max_value=100)
    email = st.text_input("Email")
    biography = st.text_area("Short bio")
    terms = st.checkbox("I agree to terms")
    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Email: {email}")
        st.write(f"Bio: {biography}")

        if terms:
            st.write("You agreed to terms")
        else:
            st.write("you did not agree to terms")

            tab1, tab2, tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

        with tab1:
            st.header("This is conent for tab1")
            st.write("This is text for tab1")

        with tab2:
            st.header("this is content for tab2")
            st.write("This is text for tab2")

        with tab3:
            st.header("this is content for tab3")
            st.write("This is text for tab3")

