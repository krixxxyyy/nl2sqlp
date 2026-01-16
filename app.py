import streamlit as st
from main import nl_to_sql

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="NL → SQL Generator",
    layout="centered"
)

st.title("Natural Language → SQL Generator")
st.caption("Rule-based NL→SQL with safe clarification handling")

# -----------------------------
# Session state
# -----------------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "awaiting_clarification" not in st.session_state:
    st.session_state.awaiting_clarification = False

if "clarification_prompt" not in st.session_state:
    st.session_state.clarification_prompt = ""

# -----------------------------
# Main NL input
# -----------------------------
query = st.text_input(
    "Enter a natural language query",
    placeholder="e.g. highest salary department",
    disabled=st.session_state.awaiting_clarification
)

# -----------------------------
# Submit main query
# -----------------------------
if st.button("Generate SQL", disabled=st.session_state.awaiting_clarification):
    if query.strip():
        response = nl_to_sql(query.strip())

        st.session_state.history.append({
            "user": query.strip(),
            "response": response
        })

        # Robust clarification detection
        if "(max/avg)" in response.lower():
            st.session_state.awaiting_clarification = True
            st.session_state.clarification_prompt = response
    else:
        st.warning("Please enter a query.")

# -----------------------------
# Clarification input (separate box)
# -----------------------------
if st.session_state.awaiting_clarification:
    st.markdown("### 🔍 Clarification Required")
    st.info(st.session_state.clarification_prompt)

    clarification = st.text_input(
        "Please clarify (max / avg)",
        key="clarification_input"
    )

    if st.button("Submit Clarification"):
        if clarification.strip():
            response = nl_to_sql(clarification.strip())

            st.session_state.history.append({
                "user": clarification.strip(),
                "response": response
            })

            # Reset clarification state
            st.session_state.awaiting_clarification = False
            st.session_state.clarification_prompt = ""
        else:
            st.warning("Please enter a clarification.")

# -----------------------------
# Display conversation history
# -----------------------------
if st.session_state.history:
    st.markdown("### Conversation")

    for item in st.session_state.history:
        st.markdown(f"**🧑 User:** {item['user']}")

        response = item["response"].strip().lower()

        # ---- System clarification ----
        if "(max/avg)" in response:
            st.markdown("**🤖 System (clarification):**")
            st.info(item["response"])

        # ---- SQL output ----
        else:
            formatted_sql = (
                item["response"]
                .replace("SELECT", "\nSELECT")
                .replace("FROM", "\nFROM")
                .replace("JOIN", "\nJOIN")
                .replace("WHERE", "\nWHERE")
                .replace("GROUP BY", "\nGROUP BY")
            ).strip()

            st.markdown("**🧠 Generated SQL:**")
            st.code(formatted_sql, language="sql")

        st.markdown("---")

# -----------------------------
# Footer
# -----------------------------
st.caption("v1.1-stable · Deterministic · No SQL execution")