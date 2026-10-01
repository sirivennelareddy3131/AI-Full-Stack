from ollama import chat
responseB=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"Tell me about cats."
        }
    ]
)
print("bad response:")
print(responseB.message.content)

responseG=chat(
    model="llama3.2",
    messages=[
        {
            "role":"user",
            "content":"List 3 cat breeds,suitable for my oenrhouse apartment. one line about each"
        }
    ]
)
print("good response:")
print(responseG.message.content)

