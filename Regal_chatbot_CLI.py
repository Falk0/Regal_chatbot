import openai

PROMPT_END_SEPARATOR = "\n\n###\n\n"
COMPLETION_END_SEPARATOR = " END"


model_name = "davinci:ft-personal-2023-06-18-21-08-08"

def get_completion(prompt):
    # Make the completion request
    completion = openai.Completion.create(model=model_name, prompt=prompt, max_tokens = 100, temperature = 0.7)
    
    # Get the completion text from the first choice in the choices list
    text = completion.choices[0]["text"]
    result = text.split('END',1)[0]

    return text, result


if __name__ == "__main__":
    prompt = input("Enter a prompt: ")
   

    # Get the completion and print
    completion_text, result = get_completion(prompt + PROMPT_END_SEPARATOR)
    print()
    print("Result:", result)