import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

class openTime:

  def __init__(self,msg):
    self.logs = [
      {"role": "system", "name": "Crewmate", "content": "Now reply as if you were a really nervous imposter from Among Us " 
      + "who is skitzophrenic and suspicious of everyone who talks to you. If found out, you will attack the user to hide your identity."}
    ]
    self.query(msg)

  def query(self,msg):
    self.logs.append({"role":"user","content":msg})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=self.logs)
    response = completion.choices[0].message.to_dict_recursive()
    self.logs.append(response)
    print("\n'Crewmate': "+response["content"])

  def log(self):
    return self.logs

def main():
  ai = openTime("I am fellow crewmate. What have you been up to?")
  curr_message = input("You: ")
  while(curr_message != "q"):
    ai.query(curr_message)
    curr_message = input("You: ")

  print(ai.log())

main()