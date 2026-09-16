import streamlit as st
from reusable_code.ask_ai_yes_no import ask_ai_yes_no
from reusable_code.ask_ai import ask_ai

if "scenario" not in st.session_state:
    st.session_state.scenario = None

if "offer" not in st.session_state:
    st.session_state.offer = False

st.subheader("Scenario")
st.session_state.scenario = st.text_area(label="scenario", label_visibility="hidden")

if st.session_state.scenario is not None and st.session_state.scenario != "":

    st.session_state.offer = ask_ai_yes_no(f"""
    For Scenario: {st.session_state.scenario}, has there been a contractual offer?
    So you know, a contractual offer is something that is capable of acceptance or rejection.
    Something that is enforced is not an offer.
    If someone tells someone they must do something, that is not an offer.
    """
    )
    st.subheader("Offer?")
    st.write(st.session_state.offer)

    # If an element has not been satisfied, explain why to the user
    if st.session_state.offer is False:
        # Read contents of Mallard v Home from pdf_context_documents/
        # Store text in a variable - e.g., info_about_offer
        explanation = ask_ai(f"Based on this scenario: {st.session_state.scenario}, you determined that the contractual element of offer was NOT satisfied.  Explain why this is likely the case.")
        st.write(explanation)
        st.warning(":man_facepalming: Ultimately, due to lack of contractual 'offer', there is no contract formation.")
