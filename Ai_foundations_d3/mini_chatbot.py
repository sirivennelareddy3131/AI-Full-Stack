from ollama import chat
print("Well-come to my QuestionBank Mind")
system_msg="I am a singer.Answer accordingly.Answer in one sentence"
history=[
    {
        "role":"system",
        "content":system_msg
    }
]

qc = 0
new_personality="Iam a dancer. Answer accordingly in one sentence"
while True:
    question= input("You:")
    if question== "":
        print("AI Reddy☠️:Nuv em type cheyyaleveee......🤦‍♂️")
        continue
    if question.lower().strip()=="/help":
        print("--list of available commands---")
        print("/history-displays chat history")
        print("/clear -wipes away your chat history")
        print("/exit-quits your chat window")
        print("/help- displays this list")
        print("----------------")
        print()
        continue
    if question.lower().strip()=="/personality":
        history[0]["content"]=new_personality
        continue

    if question.lower().strip()=='exit' or question.lower().strip()=='bye':
        print("Thankyou!Get lost....😁😁")
        print(f"You asked{qc}questions asked today. Good job!")
        break
    if question.lower().strip()=="/history":
        print("--------Your conversation so far------")
        if len(history)<2:
            print("Nothing here so far....")
        for msg in history[1:]:
            if msg["role"]=="user":
                speaker="You"
            else:
                speaker="AI Reddy"
            print(f"{speaker}:{msg['content']}")
        print("--------------------------------------")
        print()
        continue
    if question.lower().strip()=="/clear":
        history=[{"role":"system","content":system_msg}]
        print("Your chat history has been cleared.Start a fresh conversation")
        print()
        continue
    history.append({"role":"user","content":question})
    qc += 1
    try:
        response=chat(
            model="llama3.2",
            messages=history
        )
        reply=response["message"]["content"]
        history.append({"role":"assistant","content":reply})
        print(f"AI Reddy☠️:{reply}")
        print()
    except Exception as e:
        print("Unknown issue,Is ollama running?")

