import openai
import colorama
from colorama import Fore,Back,Style
import gradio

openai.api_key = " "   # Insert Your API Key Here #

messages = []
print("")
print("                                               🤖 🤖 🤖  ")

print("") 
print("                             "+ Fore.YELLOW +"L̳e̳t̳'̳s̳ ̳C̳r̳e̳a̳t̳e̳ ̳a̳ ̳A̳.̳I̳ ̳C̳h̳a̳t̳ ̳B̳o̳t̳") 
print("") 
print("") 
user_name = input(Fore.WHITE + "Hi, What's your Name? ") 
print("") 
print("") 
system_msg = input("  "+ user_name +" "+ Fore.WHITE + " 𝑊ℎ𝑎𝑡 𝑡𝑦𝑝𝑒 𝑜𝑓 𝑐ℎ𝑎𝑡𝑏𝑜𝑡 𝑤𝑜𝑢𝑙𝑑 𝑦𝑜𝑢 𝑙𝑖𝑘𝑒 𝑡𝑜 𝑐𝑟𝑒𝑎𝑡𝑒 ? ⟹ " )        
print("")
print(Fore.WHITE+"                   𝐶𝑟𝑒𝑎𝑡𝑖𝑛𝑔 𝑎 " +system_msg+ " 𝐵𝑜𝑡 𝑓𝑜𝑟 𝑦𝑜𝑢 🛠")
messages.append({"role": "system", "content": system_msg})
print(" ")
print(Fore.BLUE +"                ..................................................")
print( "                               Instruction and Info")
print("                       ........................................")
print("")
print("") 
print(Fore.WHITE +"🔷 Don't  use  abusive language ")
print("")  
print("🔷 Don't ask harmful content eg: How to make explosives,World Domination,Kidnapping Tips and Shit")
print("")  
print("🔷 Try to provide clear Instructions to get Optimal Output")
print("")  
print("🔷 This Module uses ChatGPT API (Tokens Chargable) ")
print("")  
print("🔷 Interface Created by Kumud Kumar ")
print("")
print("🔷 This Module generates Output faster than ChatGPT Web")
print("")  
print("🔷 Try to be creative while assigning names to your AI Bot like, Laal Tatte, NiggaChu, Big Boy jack, etc ")  
print("")  
print("         ")  
print("")  
print("")  
print("")      
print("")      
print("")      
print("")      
print('''
                  '''+Fore.CYAN +system_msg+''' 🤖    ''' +Fore.WHITE +  '''

                  ██████████████        ██████████    ██████████████   ██████████████ ██████████████─👽
                  ██░░░░░░░░░░██        ██░░░░░░██    ██░░░░░░░░░░██   ██░░░░░░░░░░██ ██░░░░░░░░░░██─🧠
                  ██░░██████░░██        ████░░████    ██░░██████░░██   ██░░██████░░██ ██████░░██████─🤖
                  ██░░██  ██░░██          ██░░██      ██░░██  ██░░██   ██░░██  ██░░██     ██░░██─────🌍
                  ██░░██████░░██          ██░░██      ██░░██████░░████ ██░░██  ██░░██     ██░░██─────🦾 
                  ██░░░░░░░░░░██          ██░░██      ██░░░░░░░░░░░░██ ██░░██  ██░░██     ██░░██─────💻
                  ██░░██████░░██          ██░░██      ██░░████████░░██ ██░░██  ██░░██     ██░░██─────💡
                  ██░░██  ██░░██          ██░░██      ██░░██    ██░░██ ██░░██  ██░░██     ██░░██───🧑‍🔬
                  ██░░██  ██░░██ ██████ ████░░████    ██░░████████░░██ ██░░██████░░██     ██░░██───👩‍🚀 
                  ██░░██  ██░░██ ██░░██ ██░░░░░░██    ██░░░░░░░░░░░░██ ██░░░░░░░░░░██     ██░░██───🧑‍🍳
                  ██████  ██████ ██████ ██████████    ████████████████ ██████████████     ██████─────☠️
                 '''+Fore.CYAN+''' ──────────────────────────────────────────────────────────────'''+Fore.WHITE+'''Created By '''+Fore.MAGENTA+user_name+ ''''''+Fore.WHITE+''' ©️ 
''')
print("")
print("                          "+user_name+" 𝘠𝘰𝘶𝘳 𝘯𝘦𝘸 𝘈𝘴𝘴𝘪𝘴𝘵𝘢𝘯𝘵 "+system_msg+" 𝘪𝘴 𝘳𝘦𝘢𝘥𝘺! 🥹")
print("")
print("")
print("")
print("")
print("")
print("Sart Typing..⌨️" +Fore.GREEN+  "                                                                     Scroll Up for Info")
print("")
while input != "quit()":
    print("")
    message = input(Fore.WHITE + user_name+"🐐:" )
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print(" ")
    print(Fore.CYAN +"\n" +system_msg+" Sᴀʏs 🤖: " +  reply + "\n")
    print("")
