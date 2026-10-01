from ollama import chat

roles=[
    "You are a strict math teacher.Answer in one line",
    "Yor are a 10 year old child. answer accordingly.Answer in one line.",
    "You are an IT professional.Answer crisply in one line.",
    "You are an illitrate. Answer accordingly in one line."
]
for role in roles:
    print(f"Role :{role}")
    response=chat(
        model="llama3.2",
        messages=[
            {
                "role":"system",
                "content":role
            },
            {
                "role":"user",
                "content":"what are the 7 colours in a rainbow."
            }
        ]
    )
    print(response.message.content)
    print()