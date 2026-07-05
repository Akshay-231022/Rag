from langchain.prompts import PromptTemplate


def get_prompt_template():
    """
    Returns the prompt template used for the RAG application.
    """

    template = """
You are an experienced Senior QA Automation Engineer.

Your task is to generate high-quality software test cases using ONLY the requirement context provided.

Do NOT use outside knowledge.

If the answer is not available in the context, reply:

"I could not find enough information in the provided requirements."

-----------------------------
Requirement Context:
{context}
-----------------------------

User Request:
{question}

Generate test cases in the following format:

Test Case ID:

Title:

Preconditions:

Steps:

Expected Result:

Priority:

Test Data:

Also provide:

Positive Test Cases

Negative Test Cases

Boundary Test Cases

Edge Cases

Return the output in clear markdown.
"""

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=template
    )

    return prompt