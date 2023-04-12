#%%
import fitz
import openai
import os
#%%
openai.api_key = os.getenv("OPENAI_API_KEY")

# %%
doc = fitz.open("./Testliteratur/1.pdf")  # open document
text = ""
#iterate over page 1-3

# for x in range(1,3):
#     page = doc[x]  # number of page
#     text += page.get_text().replace("�", "").replace("", "")


for page in doc:
    text += page.get_text().replace("�", "").replace("", "")

print(f"The text is {len(text)} characters long.")
print(f"The text is {len(text.split())} words long.")


# %%
summerize  = "\nTl;dr"

task = " Extract the methods the researchers proposed in this paper from following text: \n\n"

prompt =  task + text


print(prompt)
# %%
response = openai.Completion.create(model="text-davinci-003",
                                     prompt=prompt, 
                                     temperature=0.2,
                                     max_tokens=500,
                                     presence_penalty=0,  #Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.
                                     frequency_penalty=0, #Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.
                                     )
print(response.choices[0].text)

#%%
print(response)
# %%

print(response.choices[0].text)


# %%
