import streamlit as st
from pipeline import run_pipeline


def main():
    # Title and short description
    st.title("AI Assessment: Agent-Based, UI-Driven")

    st.write(
        "This app demonstrates a simple two-agent pipeline:\n"
        "- A Generator Agent that creates educational content.\n"
        "- A Reviewer Agent that evaluates the content and may trigger a refinement."
    )

    # Input section
    st.markdown("### Input")
    st.write("Enter the grade and topic, then click the button to run the agent pipeline.")

    grade = st.number_input("Grade", min_value=1, max_value=12, value=4, step=1)
    topic = st.text_input("Topic", value="Types of angles")

    # Pipeline trigger
    if st.button("Run Agent Pipeline"):
        with st.spinner("Running agents..."):
            generator_output, review_output, refined_output = run_pipeline(
                grade=int(grade),
                topic=topic,
            )

        # Generator output
        st.markdown("## Generator Output")
        st.subheader("Explanation")
        st.write(generator_output["explanation"])

        st.subheader("MCQs")
        for idx, mcq in enumerate(generator_output["mcqs"], start=1):
            st.markdown(f"**Q{idx}. {mcq['question']}**")
            for opt in mcq["options"]:
                st.write(f"- {opt}")
            st.write(f"**Answer:** {mcq['answer']}")
            st.write("---")

        # Reviewer feedback
        st.markdown("## Reviewer Feedback")
        st.write(
            "The reviewer checks age appropriateness, conceptual correctness, and clarity."
        )

        status = review_output["status"]
        if status == "pass":
            st.success("Status: PASS")
        else:
            st.error("Status: FAIL")

        if review_output["feedback"]:
            st.markdown("**Feedback:**")
            for fb in review_output["feedback"]:
                st.write(f"- {fb}")
        else:
            st.write("No feedback. Content looks good.")

        # Refined output
        st.markdown("## Refined Output (if any)")
        st.write(
            "If the reviewer fails the content, the generator refines it once using the feedback."
        )

        if refined_output is not None:
            st.info("Content was refined after feedback.")
            st.subheader("Refined Explanation")
            st.write(refined_output["explanation"])

            st.subheader("Refined MCQs")
            for idx, mcq in enumerate(refined_output["mcqs"], start=1):
                st.markdown(f"**Q{idx}. {mcq['question']}**")
                for opt in mcq["options"]:
                    st.write(f"- {opt}")
                st.write(f"**Answer:** {mcq['answer']}")
                st.write("---")
        else:
            st.write("No refinement needed (or refinement not triggered).")
    else:
        st.write("Click **Run Agent Pipeline** to generate and review content.")


if __name__ == "__main__":
    main()
