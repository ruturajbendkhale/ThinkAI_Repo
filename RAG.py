from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# Initialize the LLM with the OpenAI API key
llm = OpenAI(api_key="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")

# SimplificationAgent Class
class SimplificationAgent:
    def __init__(self, llm):
        self.llm = llm

    def simplify_question(self, question):
        prompt = PromptTemplate(
            input_variables=["question"],
            template="Simplify the following question for a user: {question}"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        return chain.run({"question": question})

# ReviewAgent Class
class ReviewAgent:
    def __init__(self, llm):
        self.llm = llm

    def review_response(self, response):
        prompt = PromptTemplate(
            input_variables=["response"],
            template="Check whether the response from te user contains the simple but direct to the point information or not, if not then ask the same question and explain how one can response better: {response}"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        review = chain.run({"response": response})
        return "concise and clear" in review.lower()

# Main execution logic
def main():
    # Database of form questions
    form_questions = [
        "How does the planned construction or modification of a building structure align with existing zoning regulations and environmental impact assessments, and what are the implications for both local infrastructure and community development??",
        "In what ways will the proposed alterations to the existing building impact its compliance with current safety standards and accessibility requirements, and what are the potential effects on the surrounding neighborhood’s aesthetic and functional characteristics??",
        "What are the procedural and environmental considerations involved in the planned demolition of the building, and how will the removal of the structure affect the local ecosystem and waste management processes??",
        # Add more questions as neededR
    ]

    # Instantiate the agents
    simplification_agent = SimplificationAgent(llm)
    review_agent = ReviewAgent(llm)

    responses = {}
    for question in form_questions:
        while True:
            simplified_question = simplification_agent.simplify_question(question)
            response = input(simplified_question)
            if review_agent.review_response(response):
                break
            else:
                print("The response was not concise or clear. Please provide a better answer.")

    filled_form = fill_form(responses)
    print("Filled Form:", filled_form)

# Form Filling Agent function (no need to encapsulate in a class)
def fill_form(responses):
    filled_form = {}
    for question, response in responses.items():
        filled_form[question] = response
    return filled_form

# Run the main function
if __name__ == "__main__":
    main()
