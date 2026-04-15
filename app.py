import streamlit as st

REDIRECT_URL = "https://coach.archpal.org/"

st.set_page_config(
    page_title="Archpal Has Moved!",
    page_icon="🏠",
    layout="centered",
)

st.markdown(
    """
    <style>
        .block-container {
            max-width: 640px;
            padding-top: 5rem;
        }
        .title {
            text-align: center;
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            color: #1a1a2e;
        }
        .message {
            text-align: center;
            font-size: 1.15rem;
            line-height: 1.8;
            color: #4a4a68;
            margin-bottom: 2.5rem;
        }
        .btn-wrapper {
            display: flex;
            justify-content: center;
        }
        .btn-wrapper a {
            background-color: #4361ee;
            color: #ffffff !important;
            text-decoration: none;
            padding: 0.85rem 2.5rem;
            border-radius: 8px;
            font-size: 1.1rem;
            font-weight: 600;
            transition: background-color 0.2s ease;
        }
        .btn-wrapper a:hover {
            background-color: #3a56d4;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">Archpal Has Moved!</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="message">'
    "Archpal has migrated to a new website! All of your previous "
    "conversations and profile await you. Press the button below to redirect!"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="btn-wrapper">'
    f'<a href="{REDIRECT_URL}" target="_self">Go to Archpal →</a>'
    f"</div>",
    unsafe_allow_html=True,
)
