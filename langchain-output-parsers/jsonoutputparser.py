from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

# Biggest flaw of JSONOutputParser is that it will throw an error if the output is not valid JSON.
# This can happen if the model generates text that is not properly formatted as JSON, which can be a common occurrence.
# To enforce schema validation, we can use StructuredOutputParser instead, which allows us to define a schema for the expected output &
# validate the model's output against that schema. This can help ensure that the output is in the desired format and reduce the likelihood of errors.