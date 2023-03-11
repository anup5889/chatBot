# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import openai
openai.api_key = open("api_key","r").read().strip("\n")

message_history =[]
def chat(inp, role='user'):
    message_history.append({"role":role,"content":inp})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message_history,
    )
    reply_content = completion.choices[0].message.content
    print(reply_content)
    message_history.append({"role" : "assistant","content" : reply_content})
    return reply_content

for i in range(2):
    user_input = input(">: ")
    print("User's input was",user_input)
    print()
    chat(user_input)
    print()

