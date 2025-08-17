import streamlit as st
from helpers import state, lang

st.set_page_config(page_title="Intrinsic", layout="wide")

# Initialize session state and language
state.init_session_state()
lang_code = state.language_selector()
L = lang.get_labels()[lang_code]

# ---- Page Content ----
if lang_code == "Português (BR)":
    st.title("Intrinsic")

    st.write(
        "Uma ferramenta para construção de portfólios de ações com base na margem de segurança, voltada ao mercado brasileiro."
    )
