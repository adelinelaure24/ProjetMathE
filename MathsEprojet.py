import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Application Multi-Menus", layout="wide")

# Barre latérale pour le menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Choisissez une page :", ["Accueil", "À propos", "Contact"])

# Affichage du contenu selon le menu sélectionné
if menu == "Accueil":
    st.title("Bienvenue sur l'Accueil")
    st.write("Ceci est la page d'accueil de l'application.")
    st.image("https://source.unsplash.com/random/800x400", caption="Image aléatoire")

elif menu == "À propos":
    st.title("À propos")
    st.write("Cette application est développée avec Streamlit.")

elif menu == "Contact":
    st.title("Contact")
    st.write("Vous pouvez nous contacter à :")
    st.write("📧 Email : contact@example.com")
    st.write("📞 Téléphone : +33 1 23 45 67 89")

# Pour exécuter : `streamlit run votre_fichier.py`


