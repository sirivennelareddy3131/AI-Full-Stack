from ollama import chat
for temp in [0.7,1.5]:
    print(f"Temp :{temp}")
    for run in range(1):
        response=chat(
            model="llama3.2",
            messages=[
        
                    {"role":"system","content":"give low and high temperature response"},
                    {"role":"user","content":"Iam late to class"},
                    {"role":"system","content":"low temperature"},

                    {"role":"user","content":"Iam late to class"},
                    {"role":"system","content":"high temperature"},


            ],
            options={"temperature":temp}
        )
        print(f"Run{run+1}:{response.message.content}")
        print()