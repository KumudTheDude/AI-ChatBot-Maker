import openai

openai.api_key = ""   ## Provide the Open AI API key between ""

messages = []
print("")
print("                                           A.I  ChatBot Maker     ️")
print("                                               🤖 🤖 🤖  ")
print("") 
print("") 
user_name = input("Hi, What's your Name? ") 
print("") 
print("") 
system_msg = input("   "+ user_name+ " 𝘗𝘪𝘤𝘬 𝘢 𝘕𝘢𝘮𝘦 𝘧𝘰𝘳 𝘠𝘰𝘶𝘳 𝘈.𝘐 𝘊𝘩𝘢𝘵 𝘉𝘰𝘵?: ")        
print("")
print("")
print("                   𝐶𝑟𝑒𝑎𝑡𝑖𝑛𝑔 𝑎 " +system_msg+ " 𝐵𝑜𝑡 𝑓𝑜𝑟 𝑦𝑜𝑢")
messages.append({"role": "system", "content": system_msg})
print("                ..................................................")
print("                               Instruction and Info")
print("")
print("")
print("1. Don't use abusive language ")
print("")  
print("2. Don't Try to ask harmful content eg: How to make explosives,World Domination,Kidnapping Tips and Shit")
print("")  
print("3. Try to provide clear Instructions to get Optimal Output")
print("")  
print("4. This Module uses ChatGPT API ")
print("")  
print("5. Interface Created by Kumud Kumar")
print("")
print("6. This Module generates Output faster than ChatGPT Web")
print("")  
print("7. Try to be creative while assigning names to your AI Bot like, Laal Tatte, NiggaChu, Big Boy jack, etc ")  
print("")  
print("")  
print("")  
print("")  
print("")  
print("")  
print("")    
print(''' 
               '''+system_msg+''' 🤖         

               ─██████████████────────██████████────██████████████───██████████████─██████████████─👽
               ─██░░░░░░░░░░██────────██░░░░░░██────██░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─😈
               ─██░░██████░░██────────████░░████────██░░██████░░██───██░░██████░░██─██████░░██████─🤖
               ─██░░██──██░░██──────────██░░██──────██░░██──██░░██───██░░██──██░░██─────██░░██─────☠️ 
               ─██░░██████░░██──────────██░░██──────██░░██████░░████─██░░██──██░░██─────██░░██─────🦾 
               ─██░░░░░░░░░░██──────────██░░██──────██░░░░░░░░░░░░██─██░░██──██░░██─────██░░██─────🧠
               ─██░░██████░░██──────────██░░██──────██░░████████░░██─██░░██──██░░██─────██░░██─────🎓
               ─██░░██──██░░██──────────██░░██──────██░░██────██░░██─██░░██──██░░██─────██░░██────🧑‍⚕️
               ─██░░██──██░░██─██████─████░░████────██░░████████░░██─██░░██████░░██─────██░░██────👨‍🏫
               ─██░░██──██░░██─██░░██─██░░░░░░██────██░░░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██────👩‍⚖️
               ─██████──██████─██████─██████████────████████████████─██████████████─────██████──────👀
               ────────────────────────────────────────────────────────────Created By '''+user_name+''' 
''')
print("                                                                   𝘠𝘰𝘶𝘳 𝘯𝘦𝘸 𝘈𝘴𝘴𝘪𝘴𝘵𝘢𝘯𝘵 𝘪𝘴 𝘳𝘦𝘢𝘥𝘺! ")
print("")
print("                                                                             𝖲𝖼𝗋𝗈𝗅𝗅 𝖴𝗉 𝖿𝗈𝗋 𝖨𝗇𝖿𝗈")
print("")
print("")
print("")
print("")
print("")
print("")
print("Start Typing..  ")
print("")
print("")
while input != "quit()":
    message = input(user_name+"🐐:" )
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print(" ")
    print("▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ")
    print("\n"+system_msg+" Sᴀʏs 🤖: " +  reply + "\n")
    print("▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ")
