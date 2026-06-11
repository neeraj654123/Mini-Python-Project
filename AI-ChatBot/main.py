from openai import OpenAI

key="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"
messages=[]
client =OpenAI(
    api_key=key
)

def completion(message):
    global messages
    messages.append(
        {
            "role" :"user",
            "content":message
        }
        )
    chat_completion=client.chat.completions.create(messages=messages,
                        model="gpt-4o")
    message={
        "role":"assistant",
        "content":chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis:{message['content']}")
if __name__ =="__main__":
    print("Hi I am Jarvis, how may i help you?")
    while True:
        user_question =input()
        print(f"User:{user_question}")
        completion(user_question)

