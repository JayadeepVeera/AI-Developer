from typing import TypedDict, List, Optional


class MCQ(TypedDict):
    question: str
    options: List[str]
    answer: str


class GeneratorOutput(TypedDict):
    explanation: str
    mcqs: List[MCQ]


class GeneratorAgent:
    """
    Generator Agent:
    - Input: grade (int), topic (str), optional feedback (list[str])
    - Output: GeneratorOutput
    """

    def generate(
        self,
        grade: int,
        topic: str,
        feedback: Optional[list[str]] = None
    ) -> GeneratorOutput:
        """
        Very simple implementation:
        - If topic is about 'angle', generate angles content.
        - Otherwise, generate a generic placeholder explanation + MCQs.
        """

        topic_lower = topic.lower()

        # Case 1: Types of angles (or similar)
        if "angle" in topic_lower:
            explanation = (
                "An angle is made when two straight lines meet at a point, "
                "and we can use angles to describe how much the lines turn. "
                "We can talk about different types of angles. "
                "A right angle is an angle that looks like the corner of a square. "
                "An acute angle is smaller than a right angle. "
                "An obtuse angle is bigger than a right angle."
            )


            # If feedback asks for simpler language, use shorter sentences
            if feedback:
                fb_text = " ".join(feedback).lower()
                if "too long" in fb_text or "too complex" in fb_text or "simpler" in fb_text:
                    explanation = (
                        "An angle is made when two lines meet. "
                        "A right angle is like the corner of a book. "
                        "An acute angle is smaller than a right angle. "
                        "An obtuse angle is bigger than a right angle."
                    )

            mcqs: List[MCQ] = [
                {
                    "question": "What is an angle?",
                    "options": [
                        "Two lines that never meet",
                        "A shape with three sides",
                        "Two lines that meet at a point",
                        "A number bigger than 100"
                    ],
                    "answer": "Two lines that meet at a point",
                },
                {
                    "question": "Which angle is like the corner of a square?",
                    "options": [
                        "Acute angle",
                        "Obtuse angle",
                        "Right angle",
                        "Straight angle"
                    ],
                    "answer": "Right angle",
                },
                {
                    "question": "Which angle is smaller than a right angle?",
                    "options": [
                        "Acute angle",
                        "Obtuse angle",
                        "Right angle",
                        "Straight angle"
                    ],
                    "answer": "Acute angle",
                },
                {
                    "question": "Which angle is bigger than a right angle?",
                    "options": [
                        "Acute angle",
                        "Obtuse angle",
                        "Right angle",
                        "Straight angle"
                    ],
                    "answer": "Obtuse angle",
                },
            ]

            return {
                "explanation": explanation,
                "mcqs": mcqs,
            }

        # Case 2: Any other topic (simple placeholder to keep structure)
        generic_explanation = (
            f"This is a short explanation about {topic}. "
            "Right now, this agent knows this topic in a simple way."
        )
        generic_mcqs: List[MCQ] = [
            {
                "question": f"What is this lesson mainly about?",
                "options": [
                    topic,
                    "Mathematics",
                    "Science",
                    "Sports"
                ],
                "answer": topic,
            }
        ]

        return {
            "explanation": generic_explanation,
            "mcqs": generic_mcqs,
        }
