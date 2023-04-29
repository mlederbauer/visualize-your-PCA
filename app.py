import streamlit as st
from tabs import theory, visualize, about

def main():
    st.set_page_config(page_title="Visualize Your CSA")

    st.sidebar.title("Navigation")
    menu = ["Theory", "Visualize Your PCA", "About"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Theory":
        theory.theory()
    elif choice == "Visualize Your PCA":
        visualize.visualize()
    else:
        about.about()

if __name__ == "__main__":
    main()

