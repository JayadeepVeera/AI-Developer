from typing import Optional, Tuple
from generator_agent import GeneratorAgent, GeneratorOutput
from reviewer_agent import ReviewerAgent, ReviewerOutput


def run_pipeline(grade: int, topic: str) -> Tuple[GeneratorOutput, ReviewerOutput, Optional[GeneratorOutput]]:
    generator = GeneratorAgent()
    reviewer = ReviewerAgent()

    # First pass
    first_output = generator.generate(grade=grade, topic=topic, feedback=None)
    review = reviewer.review(first_output, grade=grade)

    refined_output: Optional[GeneratorOutput] = None

    # If fail, do ONE refinement pass
    if review["status"] == "fail":
        refined_output = generator.generate(
            grade=grade,
            topic=topic,
            feedback=review["feedback"]
        )

    return first_output, review, refined_output
