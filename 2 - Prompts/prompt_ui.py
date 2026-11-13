from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-flash-latest"
)

st.header("Research Assistant")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)

user_input = st.text_input("Enter the prompt")


# @st.cache_resource
# def load_model():

#     llm = HuggingFaceEndpoint(
#         repo_id="ibm-granite/granite-4.2-3b",
#         task="text-generation",
#         max_new_tokens=100,
#         temperature=0.5
#     )

#     return ChatHuggingFace(llm=llm)


# model = load_model()


if st.button("Submit"):

    result = model.invoke(user_input)

    st.write(result.content)