import openai
import __api
import os

openai.api_key = __api.api

onlyfiles = [f for f in os.listdir('/Users/coding/Documents/vs/FluentFriend/model/dataset/input')]

def chat(mess):
    model_engine = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=model_engine, 
        messages=[{"role": "user", "content": mess}], 
        max_tokens = 200, 
        stop=None, 
        temperature=0.5 
    )
    message = response.choices[0].message.content
    return message.strip()

def user_query(prompt):
    user_prompt = (f"{prompt}")
    result = chat(user_prompt)
    return result
    
def runner_2():
    try:
        for c in onlyfiles:
            cc = c.replace(".txt","")
            text = open('/Users/coding/Documents/vs/FluentFriend/model/dataset/input/'+c)
            text = text.readlines()
            pf = user_query(text)

            f = open('/Users/coding/Documents/vs/FluentFriend/model/dataset/output/'+cc+'_out.txt', "x")
            f = open('/Users/coding/Documents/vs/FluentFriend/model/dataset/output/'+cc+'_out.txt', "w")
            f.writelines(pf)
            f.close()
    except:
        pass
