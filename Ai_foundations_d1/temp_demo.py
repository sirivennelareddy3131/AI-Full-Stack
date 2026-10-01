from ollama import chat
for temp in [0,0.7,1.5]:
    print(f"Temp :{temp}")
    for run in range(3):
        response=chat(
            model="llama3.2",
            messages=[
                {
                    "role":"user",
                    "content":"give me a  name for my wine shop."
                }
            ],
            options={"temperature":temp}
        )
        print(f"Run{run+1}:{response.message.content}")
        print()