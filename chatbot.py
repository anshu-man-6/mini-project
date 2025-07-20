import random

hellow=["hii","is there anyone","can you here me","good day","hello","whats!up"]
bye=["bye","see you later","good day","i am leaving","have a good day"]
howare=["how are you","whats up","how you doing"]
name=["whats your name","do you have name please tell me","what should i call you","what is your name"]
dash=["what is your menu","what do you reccommend","show you menu","give me your menu"]
something=["tell me any thing","what are you doing","what can you do"]


print("**************************************************\n")

while True:
    a=input("user said-")

    if a.lower() in hellow: 
        bot=["Hello !","Hii","Hello and Welcome"]
        print('bot-'+random.choice(bot)+'\n')

    elif a.lower() in bye:
        bot=["bye ! see you soon","glad ! to say you bye","bye, Take care"] 
        print('bot-'+random.choice(bot)+'\n') 

    elif a.lower() in howare:
        bot=["I am fine","hey dude ! how may help you","HII ! how may i assest you"]
        print('bot-'+random.choice(bot)+'\n')

    elif a.lower() in name:
        bot=["hii , i am a chatbot","of course ! i am a chatbot","I am chatbot, what's your name?"]
        print('bot-'+random.choice(bot)+'\n')

    elif a.lower() in dash:
        bot=["I can answer you ","I can answer some of you","Wjjsbhhj"]
        print('bot-'+random.choice(bot)+'\n')
    
    elif a.lower() in something:
        bot=["i am talking to you right now|","ask me anything","i can answer your some basic question"]
        print('bot-'+random.choice(bot)+'\n')


    
    
     
