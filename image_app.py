 my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(amount_of_time):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

def generate_text_from_image(url: str) -> str:
    image_to_text: Any = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    generated_text: str = image_to_text(url)[0]["generated_text"]
    print(f"IMAGE INPUT: {url}")
    print(f"GENERATED TEXT OUTPUT: {generated_text}")
    return generated_text

def generate_story_from_text(scenario: str) -> str:
    prompt_template: str = f"""
    You are a talented storyteller who can create a story from a simple narrative.
    Create a story using the following scenario; the story should be a maximum of 500 words long, Fun and creative way to make story interesting;
   
    CONTEXT: {scenario}
    STORY:
    """
    prompt: PromptTemplate = PromptTemplate(template=prompt_template, input_variables=["scenario"])
    llm: Any = ChatGroq(model_name="llama-3.2-11b-vision-preview", temperature=0.9)  # Using Groq's Llama model
    story_llm: Any = LLMChain(llm=llm, prompt=prompt, verbose=True)
    generated_story: str = story_llm.predict(scenario=scenario)
    print(f"TEXT INPUT: {scenario}")
    print(f"GENERATED STORY OUTPUT: {generated_story}")
