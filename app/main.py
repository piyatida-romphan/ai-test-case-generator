"""
main.py
-------
Streamlit entry point for the AI Test Case Generator.

Run with:
    streamlit run app/main.py
"""

import streamlit as st

from app.generators.test_case_generator import generate
from app.formatters.robot_formatter import to_robot_file_content

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="AI Test Case Generator",
    page_icon="🤖",
    layout="centered",
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.title("🤖 AI Test Case Generator")
st.caption("Paste a user story or requirement → get test cases + a Robot Framework template.")

st.divider()

# ---------------------------------------------------------------------------
# Sidebar — settings
# ---------------------------------------------------------------------------
PROVIDER_INFO = {
    "openai": {
        "label": "OpenAI",
        "key_var": "OPENAI_API_KEY",
        "model_var": "OPENAI_MODEL",
        "default_model": "gpt-4o-mini",
    },
    "anthropic": {
        "label": "Anthropic Claude",
        "key_var": "ANTHROPIC_API_KEY",
        "model_var": "ANTHROPIC_MODEL",
        "default_model": "claude-sonnet-4-6",
    },
    "gemini": {
        "label": "Google Gemini",
        "key_var": "GEMINI_API_KEY",
        "model_var": "GEMINI_MODEL",
        "default_model": "gemini-2.0-flash",
    },
}

with st.sidebar:
    st.header("⚙️ Settings")

    use_placeholder = st.toggle(
        "Use placeholder (no API key needed)",
        value=True,
        help="Returns sample output instantly — no API key required. Great for testing the UI.",
    )

    if not use_placeholder:
        provider = st.selectbox(
            "AI Provider",
            options=list(PROVIDER_INFO.keys()),
            format_func=lambda k: PROVIDER_INFO[k]["label"],
        )
        info = PROVIDER_INFO[provider]
        st.info(f"Set `{info['key_var']}` in your `.env` file.\nDefault model: `{info['default_model']}`")
    else:
        provider = "openai"

    st.divider()
    st.markdown("**Model defaults**")
    st.markdown("- Temperature: `0.3`")
    st.markdown("- Max tokens: `1500`")
    st.caption("Override via `.env` or `app/utils/config.py`.")

# ---------------------------------------------------------------------------
# Main form
# ---------------------------------------------------------------------------
user_story = st.text_area(
    label="📝 User Story / Requirement",
    placeholder="e.g. As a user, I want to transfer money between accounts so that I can manage my finances.",
    height=150,
)

generate_btn = st.button("✨ Generate Test Cases", type="primary", use_container_width=True)

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
if generate_btn:
    if not user_story.strip():
        st.warning("Please enter a user story before generating.")
    else:
        with st.spinner("Generating test cases..."):
            try:
                raw_output = generate(user_story, use_placeholder=use_placeholder, provider=provider)
                robot_output = to_robot_file_content(raw_output, story_title=user_story[:60])

            except EnvironmentError as e:
                st.error(f"Configuration error: {e}")
                st.stop()
            except Exception as e:
                st.error(f"Something went wrong: {e}")
                st.stop()

        st.success("Done! Review your test cases below.")
        st.divider()

        # Two tabs: plain test cases | Robot Framework template
        tab1, tab2 = st.tabs(["📋 Test Cases", "🤖 Robot Framework Template"])

        with tab1:
            st.text_area(
                label="Generated Test Cases",
                value=raw_output,
                height=400,
                label_visibility="collapsed",
            )
            st.download_button(
                label="⬇️ Download as .txt",
                data=raw_output,
                file_name="test_cases.txt",
                mime="text/plain",
            )

        with tab2:
            st.code(robot_output, language="robot")
            st.download_button(
                label="⬇️ Download as .robot",
                data=robot_output,
                file_name="test_cases.robot",
                mime="text/plain",
            )
