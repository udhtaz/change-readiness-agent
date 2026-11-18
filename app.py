"""Streamlit entry point for the change readiness agent."""

import streamlit as st


def main() -> None:
    """Render the Phase 1 application shell."""
    st.set_page_config(
        page_title="Change Readiness Agent",
        page_icon="✅",
        layout="centered",
    )

    st.title("Change Readiness Agent")
    st.caption("AI-assisted cloud change readiness · Phase 1 scaffold")
    st.write(
        "This project will assess synthetic change requests for approval evidence, "
        "deployment and rollback planning, testing, and monitoring readiness."
    )
    st.info("Assessment and model inference are intentionally not implemented yet.")


if __name__ == "__main__":
    main()
