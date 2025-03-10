import streamlit as st

st.title("Mon application Streamlit")
st.write("Ceci est une application simple avec Streamlit.")

# Ajouter un champ de saisie
user_input = st.text_input("Entrez quelque chose :")
st.write(f"Vous avez entré : {user_input}")

# Ajouter un bouton
if st.button("Cliquez-moi"):
    st.write("Bouton cliqué !")

