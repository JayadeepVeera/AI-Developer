from typing import TypedDict, List, Literal
from generator_agent import GeneratorOutput


class ReviewerOutput(TypedDict):
    status: Literal["pass", "fail"]
    feedback: List[str]


class ReviewerAgent:
    """
    Reviewer Agent:
    - Input: GeneratorOutput + grade
    - Output: ReviewerOutput
    """

    def review(self, content: GeneratorOutput, grade: int) -> ReviewerOutput:
        feedback: List[str] = []

        explanation = content["explanation"]
        mcqs = content["mcqs"]

        # 1. Age appropriateness: check sentence length (very simple rule)
        sentences = [s.strip() for s in explanation.split(".") if s.strip()]
        for idx, sentence in enumerate(sentences, start=1):
            word_count = len(sentence.split())
            if grade <= 4 and word_count > 18:

            
                feedback.append(
                    f"Sentence {idx} is too long for Grade {grade} (has {word_count} words)."
                )

        # 2. Conceptual correctness (very basic checks for 'angles')
        explanation_lower = explanation.lower()
        if "angle" not in explanation_lower:
            feedback.append("The explanation should clearly say what an angle is.")

        # Simple checks: right, acute, obtuse should be mentioned
        for term in ["right angle", "acute angle", "obtuse angle"]:
            if term not in explanation_lower:
                feedback.append(f"The explanation should mention '{term}' for this topic.")

        # 3. MCQ checks: each question should have 4 options and a valid answer
        for i, mcq in enumerate(mcqs, start=1):
            if len(mcq["options"]) != 4:
                feedback.append(f"Question {i} should have exactly 4 options.")
            if mcq["answer"] not in mcq["options"]:
                feedback.append(
                    f"Question {i} has an answer that is not in the options."
                )

        status: Literal["pass", "fail"] = "pass" if not feedback else "fail"

        return {
            "status": status,
            "feedback": feedback,
        }
