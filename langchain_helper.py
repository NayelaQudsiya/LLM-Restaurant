from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os

# Set API key
os.environ['GROQ_API_KEY'] = "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"

# Load LLM
llm = ChatGroq(model_name="llama3-8b-8192", temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant name (no explanation)
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='Suggest a creative restaurant name for {cuisine} food. Return only the name.'
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu items (no explanation)
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template='Provide a list of menu items for {restaurant_name}. Return only the items as a comma-separated list, no explanations, no headings.'
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Combine into a sequence
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items'],
        verbose=False
    )

    return chain({'cuisine': cuisine})

    return response

# Example test
if __name__ == "__main__":
   
    result = generate_restaurant_name_and_items(cuisine_input.strip())
    print(result["restaurant_name"])
    print(result["menu_items"])