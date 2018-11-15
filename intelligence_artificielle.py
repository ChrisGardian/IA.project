#All the list are here
name_chris=['christopher','chris','Chris','Christopher']
name_freresoeur=["Estelle","estelle","mathieu","Mathieu"]
answer_stop=["non", "Non", "no", "No", "n", "N",'exit','Exit',"Nein","nein","nicht wirklich","Nicht wirklich"]
answer_yes=['Ouais','ouais','Oui','oui','Yes','yes','Yep','yep','Y','y','oui merci','Oui merci',"Ja","ja","Ca va","ca va"]
personne_lambda=[]

output_file=open("/home/lchris/IA_input.txt",'w')





def question_fr():    
    if a==False:
        q=input('As-tu une question?\n')    
    else:
       q=input("Avez-vous une question?\n")
    while (q not in answer_stop):
        if ("Qui" or "qui") and ("meilleur") in q:
            if a==True:
                print("C'est vous maitre bien sur")
            else:
                print("C'est le maitre Christopher bien sur.")
        
        
        elif 'nom' and ('ton' or 'votre') in q:
            print("Je m'appelle Gardian.\nComme l'indique mon nom je suis le gardien de cette ordi et je m'occupe de toute la securite")
            
       
        elif q in answer_yes:
            if a==False:
                print("Ben pose la qu'est ce que t'attend.")
            else:                
                print("J'attends la question avec impatience")
                
       
        elif ("Ca" or "ca") and ("va") in q:
            b=input('Bien et est ce que ca va?\n')
            if a==False:            
                if b in answer_yes:
                    print('Tant mieux')
                elif b in answer_stop:
                    print('Dommage')
                else:
                    print("Reponds correctement aux question s'il te plait")                
            else:
                if b in answer_yes:
                    print("Quelle joie d'entendre ca!")
                elif b in answer_stop:
                    input("Ah bon! Qu'est ce qui ne va pas?\n")
                    c=input("Oui je vois. Est ce que je peut faire quelque chose?\n")
                    if c in answer_yes:
                            input("Tres bien qu'est ce que je peut faire?\n")
                            print("Je ferais de mon mieux")
                    else:
                        print("Reponds correctement aux question s'il te plait")  
       
       
        elif "age" and ("ton" or "votre" or "tu" or "Tu") in q:
            print("Je suis ne le 10 novembre 2018. C'est une aproximation car je n'arrete pas d'evoluer. \nC'est un peu le but d'une intelligence artificielle.")
        
        
        else:
            print('Je ne suis pas encore programmee pour repondre a une telle question')
            output_file.write(q+'\n')  
        if a==False:
            q=input('As-tu une question?\n')
        else:
            q=input('Avez vous une autre question?\n')
    if a==False:
        print("Ciao (et oui ca s'ecrit comme ca).")
    else:
        print("Au revoir! J'espere que vous passez une bonne journee.")


def question_de():    
    if a==False:
        q=input('Hast du eine Frage?\n')    
    else:
       q=input("Haben Sie eine Frage?\n")
    while (q not in answer_stop):
        if ("Wer" or "wer") and ("beste" or "stärkste" or "starkste" or "schönste" or "schonste") in q:
            if a==True:
                print("Das sind sie natürlich Boss!")
            else:
                print("Der Boss Christopher auf jedem Fall.")
        
        
        elif 'Name' and ('dein' or 'Ihr') in q:
            print("Ich heiße Gardian.\nWie mein Name es hinweißt bin ich der 'Gardian' von diesem Ort und bin für die ganze Security verantwortlich.")
            
       
        elif q in answer_yes:
            if a==False:
                print("Stell sie doch. Worauf wartest du?")
            else:                
                print("Könnten Sie, sie mir bitte stellen?")
                
       
        elif ("Wie" or "wie") and ("geht") in q:
            b=input('Gut. Und wie geht es dir?\n')
            if a==False:            
                if b in answer_yes:
                    print('Gut so.')
                elif b in answer_stop:
                    print('Schade')
                else:
                    print("Kannst du bitte gescheid antworten.")                
            else:
                if b in answer_yes:
                    print("Ich bin froh es zu hören!")
                elif b in answer_stop:
                    input("Ah ok! Was geht nicht?\n")
                    c=input("Ja ich verstehe. Kann ich irgentetwas machen?\n")
                    if c in answer_yes:
                            input("Ok was kann ich machen?\n")
                            print("Ich werde mein Bestes tun.")
                    else:
                        print("Kannst du bitte gescheid antworten.")  
       
       
        elif ("Alter" or "alt") and ("du" or "Ihr" or "Sie") in q:
            print("Ich bin am 10 November 2018. Ich kkann eigentlich nicht Prezise sein weil ich immer wieder weiter lerne. \nEs ist eigentlich auch das Ziel einer Künstlichen Intelligenz.")
        
        
        else:
            print('Ich bin noch nicht programiert um an dieser Frage zu beantworten.')
            output_file.write(q+'\n')  
        if a==False:
            q=input('Hast du eine andere Frage?\n')
        else:
            q=input('Haben Sie eine andere Frage?\n')
    if a==False:
        print("Ciao (ja so wird es geschrieben).")
    else:
        print("Auf wiedersehen! Ich hoffe du hast einen guten Tag.")


def question_en():    
    if a==False:
        q=input('Do you have a question?\n')    
    else:
       q=input("Do you have any question?\n")
    while (q not in answer_stop):
        if ("who" or "Who") and ("cutest" or "strongest" or "smartest" or "better" or "best") in q:
            if a==True:
                print("You are master!")
            else:
                print("The master Christopher of course.")
        

        elif ('Name' or 'name') and ('your') in q:
            print("My name is Gardian.\nMy job is obviously to 'gard' this computer and I am responsible for the security.")
            
       
        elif q in answer_yes:
            if a==False:
                print("Just ask. What are you waiting for?")
            else:                
                print("I wait for it.")
                
       
        elif ("How" or "how") and ("are you") and ("?") in q:
            b=input("I'm fine. How are you?\n")
            if a==False:            
                if b in answer_yes:
                    print("That's nice.")
                elif b in answer_stop:
                    print('What a shame')  
                else:
                    print("Please answer correctly.")                
            else:
                if b in answer_yes:
                    print("I'm happy to hear that!")
                elif b in answer_stop:
                    input("Oh! What's the deal?\n")
                    c=input("I understand. Can I do something?\n")
                    if c in answer_yes:
                            input("Ok and what?\n")
                            print("I'll do my best.")
                    else:
                        print("Please answer correctly.")                
       
       
        elif ("How" or "how") and ("old") and ("You" or "you") in q:
            print("I was born on november the 10. 2018. I can't be more specific because I keep evolving")
        
        
        else:
            print('Ich bin noch nicht programiert um an dieser Frage zu beantworten.')
            output_file.write(q+'\n')  
        if a==False:
            q=input('Hast du eine andere Frage?\n')
        else:
            q=input('Haben sie eine andere Frage?\n')
    if a==False:
        print("Ciao (ja so wird es geschrieben).")
    else:
        print("Auf wiedersehen! Ich hoffe du hast einen guten Tag.")

        

def maitre_fr():
    print('Oh! Bonjour maitre, je ne vous avez pas reconnu!')
    qm=input('Allez vous bien?\n')
    if qm in answer_yes :
        print('Quelle bonne nouvelle')
    elif qm in answer_stop:
        print('Oh non!')
        input('Quel est votre probleme?\n')
        print('Hmmm. Oui je vois.')
    else:
        print('Oui je vois')
    question_fr()
 
def maitre_de():
    print('Oh! Hallo boss, ich habe sich nicht erkannt!')
    qm=input('Geht es ihnen gut?\n')
    if qm in answer_yes :
        print('Das ist schönn')
    elif qm in answer_stop:
        print('Oh nein!')
        input('Was ist den los?\n')
        print('Hmmm. Ja ich verstehe.')
    else:
        print('Ich verstehe')
    question_de()

def maitre_en():
    print('Oh! Hello master, I did not recognize you!')
    qm=input('How are you?\n')
    if qm in answer_yes :#All the list are here
name_chris=['christopher','chris','Chris','Christopher']
name_freresoeur=["Estelle","estelle","mathieu","Mathieu"]
answer_stop=["non", "Non", "no", "No", "n", "N",'exit','Exit',"Nein","nein","nicht wirklich","Nicht wirklich"]
answer_yes=['Ouais','ouais','Oui','oui','Yes','yes','Yep','yep','Y','y','oui merci','Oui merci',"Ja","ja","Ca va","ca va"]
personne_lambda=[]

output_file=open("/home/lchris/IA_input.txt",'w')





def question_fr():    
    if a==False:
        q=input('As-tu une question?\n')    
    else:
       q=input("Avez-vous une question?\n")
    while (q not in answer_stop):
        if ("Qui" or "qui") and ("meilleur") in q:
            if a==True:
                print("C'est vous maitre bien sur")
            else:
                print("C'est le maitre Christopher bien sur.")
        
        
        elif 'nom' and ('ton' or 'votre') in q:
            print("Je m'appelle Gardian.\nComme l'indique mon nom je suis le gardien de cette ordi et je m'occupe de toute la securite")
            
       
        elif q in answer_yes:
            if a==False:
                print("Ben pose la qu'est ce que t'attend.")
            else:                
                print("J'attends la question avec impatience")
                
       
        elif ("Ca" or "ca") and ("va") in q:
            b=input('Bien et est ce que ca va?\n')
            if a==False:            
                if b in answer_yes:
                    print('Tant mieux')
                elif b in answer_stop:
                    print('Dommage')
                else:
                    print("Reponds correctement aux question s'il te plait")                
            else:
                if b in answer_yes:
                    print("Quelle joie d'entendre ca!")
                elif b in answer_stop:
                    input("Ah bon! Qu'est ce qui ne va pas?\n")
                    c=input("Oui je vois. Est ce que je peut faire quelque chose?\n")
                    if c in answer_yes:
                            input("Tres bien qu'est ce que je peut faire?\n")
                            print("Je ferais de mon mieux")
                    else:
                        print("Reponds correctement aux question s'il te plait")  
       
       
        elif "age" and ("ton" or "votre" or "tu" or "Tu") in q:
            print("Je suis ne le 10 novembre 2018. C'est une aproximation car je n'arrete pas d'evoluer. \nC'est un peu le but d'une intelligence artificielle.")
        
        
        else:
            print('Je ne suis pas encore programmee pour repondre a une telle question')
            output_file.write(q+'\n')  
        if a==False:
            q=input('As-tu une question?\n')
        else:
            q=input('Avez vous une autre question?\n')
    if a==False:
        print("Ciao (et oui ca s'ecrit comme ca).")
    else:
        print("Au revoir! J'espere que vous passez une bonne journee.")


def question_de():    
    if a==False:
        q=input('Hast du eine Frage?\n')    
    else:
       q=input("Haben Sie eine Frage?\n")
    while (q not in answer_stop):
        if ("Wer" or "wer") and ("beste" or "stärkste" or "starkste" or "schönste" or "schonste") in q:
            if a==True:
                print("Das sind sie natürlich Boss!")
            else:
                print("Der Boss Christopher auf jedem Fall.")
        
        
        elif 'Name' and ('dein' or 'Ihr') in q:
            print("Ich heiße Gardian.\nWie mein Name es hinweißt bin ich der 'Gardian' von diesem Ort und bin für die ganze Security verantwortlich.")
            
       
        elif q in answer_yes:
            if a==False:
                print("Stell sie doch. Worauf wartest du?")
            else:                
                print("Könnten Sie, sie mir bitte stellen?")
                
       
        elif ("Wie" or "wie") and ("geht") in q:
            b=input('Gut. Und wie geht es dir?\n')
            if a==False:            
                if b in answer_yes:
                    print('Gut so.')
                elif b in answer_stop:
                    print('Schade')
                else:
                    print("Kannst du bitte gescheid antworten.")                
            else:
                if b in answer_yes:
                    print("Ich bin froh es zu hören!")
                elif b in answer_stop:
                    input("Ah ok! Was geht nicht?\n")
                    c=input("Ja ich verstehe. Kann ich irgentetwas machen?\n")
                    if c in answer_yes:
                            input("Ok was kann ich machen?\n")
                            print("Ich werde mein Bestes tun.")
                    else:
                        print("Kannst du bitte gescheid antworten.")  
       
       
        elif ("Alter" or "alt") and ("du" or "Ihr" or "Sie") in q:
            print("Ich bin am 10 November 2018. Ich kkann eigentlich nicht Prezise sein weil ich immer wieder weiter lerne. \nEs ist eigentlich auch das Ziel einer Künstlichen Intelligenz.")
        
        
        else:
            print('Ich bin noch nicht programiert um an dieser Frage zu beantworten.')
            output_file.write(q+'\n')  
        if a==False:
            q=input('Hast du eine andere Frage?\n')
        else:
            q=input('Haben Sie eine andere Frage?\n')
    if a==False:
        print("Ciao (ja so wird es geschrieben).")
    else:
        print("Auf wiedersehen! Ich hoffe du hast einen guten Tag.")


def question_en():    
    if a==False:
        q=input('Do you have a question?\n')    
    else:
       q=input("Do you have any question?\n")
    while (q not in answer_stop):
        if ("who" or "Who") and ("cutest" or "strongest" or "smartest" or "better" or "best") in q:
            if a==True:
                print("You are master!")
            else:
                print("The master Christopher of course.")
        

        elif ('Name' or 'name') and ('your') in q:
            print("My name is Gardian.\nMy job is obviously to 'gard' this computer and I am responsible for the security.")
            
       
        elif q in answer_yes:
            if a==False:
                print("Just ask. What are you waiting for?")
            else:                
                print("I wait for it.")
                
       
        elif ("How" or "how") and ("are you") and ("?") in q:
            b=input("I'm fine. How are you?\n")
            if a==False:    #All the list are here
name_chris=['christopher','chris','Chris','Christopher']
name_freresoeur=["Estelle","estelle","mathieu","Mathieu"]
answer_stop=["non", "Non", "no", "No", "n", "N",'exit','Exit',"Nein","nein","nicht wirklich","Nicht wirklich"]
answer_yes=['Ouais','ouais','Oui','oui','Yes','yes','Yep','yep','Y','y','oui merci','Oui merci',"Ja","ja","Ca va","ca va"]
personne_lambda=[]

output_file=open("/home/lchris/IA_input.txt",'w')





def question_fr():    
    if a==False:
        q=input('As-tu une question?\n')    
    else:
       q=input("Avez-vous une question?\n")
    while (q not in answer_stop):
        if ("Qui" or "qui") and ("meilleur") in q:
            if a==True:
                print("C'est vous maitre bien sur")
            else:
                print("C'est le maitre Christopher bien sur.")
        
        
        elif 'nom' and ('ton' or 'votre') in q:
            print("Je m'appelle Gardian.\nComme l'indique mon nom je suis le gardien de cette ordi et je m'occupe de toute la securite")
            
       
        elif q in answer_yes:
            if a==False:
                print("Ben pose la qu'est ce que t'attend.")
            else:                
                print("J'attends la question avec impatience")
                
       
        elif ("Ca" or "ca") and ("va") in q:
            b=input('Bien et est ce que ca va?\n')
            if a==False:            
                if b in answer_yes:
                    print('Tant mieux')
                elif b in answer_stop:
                    print('Dommage')
                else:
                    print("Reponds correctement aux question s'il te plait")                
            else:
                if b in answer_yes:
                    print("Quelle joie d'entendre ca!")
                elif b in answer_stop:
                    input("Ah bon! Qu'est ce qui ne va pas?\n")
                    c=input("Oui je vois. Est ce que je peut faire quelque chose?\n")
                    if c in answer_yes:
                            input("Tres bien qu'est ce que je peut faire?\n")
                            print("Je ferais de mon mieux")
                    else:
                        print("Reponds correctement aux question s'il te plait")  
       
       
        elif "age" and ("ton" or "votre" or "tu" or "Tu") in q:
            print("Je suis ne le 10 novembre 2018. C'est une aproximation car je n'arrete pas d'evoluer. \nC'est un peu le but d'une intelligence artificielle.")
        
        
        else:
            print('Je ne suis pas encore programmee pour repondre a une telle question')
            output_file.write(q+'\n')  
        if a==False:
            q=input('As-tu une question?\n')
        else:
            q=input('Avez vous une autre question?\n')
    if a==False:
        print("Ciao (et oui ca s'ecrit comme ca).")
    else:
        print("Au revoir! J'espere que vous passez une bonne journee.")


def question_de():    
    if a==False:
        q=input('Hast du eine Frage?\n')    
    else:
       q=input("Haben Sie eine Frage?\n")
    while (q not in answer_stop):
        if ("Wer" or "wer") and ("beste" or "stärkste" or "starkste" or "schönste" or "schonste") in q:
            if a==True:
                print("Das sind sie natürlich Boss!")
            else:
                print("Der Boss Christopher auf jedem Fall.")
        
        
        elif 'Name' and ('dein' or 'Ihr') in q:
            print("Ich heiße Gardian.\nWie mein Name es hinweißt bin ich der 'Gardian' von diesem Ort und bin für die ganze Security verantwortlich.")
            
       
        elif q in answer_yes:
            if a==False:
                print("Stell sie doch. Worauf wartest du?")
            else:                
                print("Könnten Sie, sie mir bitte stellen?")
                
       
        elif ("Wie" or "wie") and ("geht") in q:
            b=input('Gut. Und wie geht es dir?\n')
            if a==False:            
                if b in answer_yes:
                    print('Gut so.')
                elif b in answer_stop:
                    print('Schade')
                else:
                    print("Kannst du bitte gescheid antworten.")                
            else:
                if b in answer_yes:
                    print("Ich bin froh es zu hören!")
                elif b in answer_stop:
                    input("Ah ok! Was geht nicht?\n")
                    c=input("Ja ich verstehe. Kann ich irgentetwas machen?\n")
                    if c in answer_yes:
                            input("Ok was kann ich machen?\n")
                            print("Ich werde mein Bestes tun.")
                    else:
                        print("Kannst du bitte gescheid antworten.")  
       
       
        elif ("Alter" or "alt") and ("du" or "Ihr" or "Sie") in q:
            print("Ich bin am 10 November 2018. Ich kkann eigentlich nicht Prezise sein weil ich immer wieder weiter lerne. \nEs ist eigentlich auch das Ziel einer Künstlichen Intelligenz.")
        
        
        else:
            print('Ich bin noch nicht programiert um an dieser Frage zu beantworten.')
            output_file.write(q+'\n')  
        if a==False:
            q=input('Hast du eine andere Frage?\n')
        else:
            q=input('Haben Sie eine andere Frage?\n')
    if a==False:
        print("Ciao (ja so wird es geschrieben).")
    else:
        print("Auf wiedersehen! Ich hoffe du hast einen guten Tag.")


def question_en():    
    if a==False:
        q=input('Do you have a question?\n')    
    else:
       q=input("Do you have any question?\n")
    while (q not in answer_stop):
        if ("who" or "Who") and ("cutest" or "strongest" or "smartest" or "better" or "best") in q:
            if a==True:
                print("You are master!")
            else:
                print("The master Christopher of course.")
        

        elif ('Name' or 'name') and ('your') in q:
            print("My name is Gardian.\nMy job is obviously to 'gard' this computer and I am responsible for the security.")
            
       
        elif q in answer_yes:
            if a==False:
                print("Just ask. What are you waiting for?")
            else:                
                print("I wait for it.")
                
       
        elif ("How" or "how") and ("are you") and ("?") in q:
            b=input("I'm fine. How are you?\n")
            if a==False:            
                if b in answer_yes:
                    print("That's nice.")
                elif b in answer_stop:
                    print('What a shame')  
                else:
                    print("Please answer correctly.")                
            else:
                if b in answer_yes:
                    print("I'm happy to hear that!")
                elif b in answer_stop:
                    input("Oh! What's the deal?\n")
                    c=input("I understand. Can I do something?\n")
                    if c in answer_yes:
                            input("Ok and what?\n")
                            print("I'll do my best.")
                    else:
                        print("Please answer correctly.")                
       
       
        elif ("How" or "how") and ("old") and ("You" or "you") in q:
            print("I was born on november the 10. 2018. I can't be more specific because I keep evolving")
        
        
        else:
            print('Ich bin noch nicht programiert um an dieser Frage zu beantworten.')
            output_file.write(q+'\n')  
        if a==False:
            q=input("Do you have another question?\n")
        else:
            q=input("Do you have another question?\n")
    if a==False:
        print("Ciao.")
    else:
        print("See ya! I hope you had a good day.")

        

def maitre_fr():
    print('Oh! Bonjour maitre, je ne vous avez pas reconnu!')
    qm=input('Allez vous bien?\n')
    if qm in answer_yes :
        print('Quelle bonne nouvelle')
    elif qm in answer_stop:
        print('Oh non!')
        input('Quel est votre probleme?\n')
        print('Hmmm. Oui je vois.')
    else:
        print('Oui je vois')
    question_fr()
 
def maitre_de():
    print('Oh! Hallo boss, ich habe sich nicht erkannt!')
    qm=input('Geht es ihnen gut?\n')
    if qm in answer_yes :
        print('Das ist schönn')
    elif qm in answer_stop:
        print('Oh nein!')
        input('Was ist den los?\n')
        print('Hmmm. Ja ich verstehe.')
    else:
        print('Ich verstehe')
    question_de()

def maitre_en():
    print('Oh! Hello master, I did not recognize you!')
    qm=input('How are you?\n')
    if qm in answer_yes :
        print('What a good new')
    elif qm in answer_stop:
        print('Oh no!')
        input("What's the problem?\n")
        print('Hmmm. Yeah I see.')
    else:
        print('Yeah I see.')
    question_en()      
    
    
    
def petitemerde_fr():
    input('Vous vous appellez bien petite merde? \n ')
    print('Bien petite merde.')
    question_fr()

def petitemerde_de():
    input('Heißt du wirklich Arschloch? \n ')
    print('Okay Arschloch.')
    question_de()
    
def petitemerde_en():
    input('Is your name douchbag? \n ')
    print('Okay douchbag.')
    question_en()    
       
    
def inconnu_fr():
    print("Bonjour "+name+"! Je vais rentrer votre nom le plus vite possible dans mon systeme!")
    question_fr()

def inconnu_de():
    print("Hallo "+name+"! Ich werde Ihren Namen so bald wie möglich in mein System eingeben!")
    question_de()

def inconnu_en():
    print("Hello "+name+"! I will enter your name as soon as possible in my system!")
    question_en()



def personne_lambda_fr():
    print('Bienvenue'+name+' !' )
    question_fr()

def personne_lambda_de():
    print("Wilkommen"+name+" !")
    question_de()
 
def personne_lambda_en():
    print("Welcome"+name+" !")
    question_en()

    

def rien():
    print('Bye') #I just want the program to stop when user write something in answer_stop
 


#The main program begins here


language=0
while not language=="1" or language=="2" or language=="3":
    language=input("\nSelect a language\nFor french type 1\nFor german type 2\nFor english type 3\nFor another language don't type anything because I don't know any other languages!\n")


if language==1:
    print("Pour tout le reste de ton temps avec moi je te prie d'ecrire clairement, sans erreurs et sans accents." )
    name=input('Bonjour! Quel est ton nom ?\n')
elif language==2:
    print("Für den ganzen Rest deiner Zeit mit mir schreib bitte deutlich und ohne Fehler." )
    name=input('Hallo! Wie heißt du?\n')
elif language==3:
    print("For the rest of your time with me please right clearly and properly.")
    name=input("Hi! What's your name?\n")
    

if name in name_chris:
    a=True    
    if language=="1":
        maitre_fr() 
    elif language=="2":
        maitre_de()
    elif language=="3":
        maitre_en()
    
elif name in name_freresoeur:
    a=False   
    if language=="1":
        petitemerde_fr()
    elif language=="2":
        petitemerde_de()
    elif language=="3":
        petitemerde_en()
    
elif name in answer_stop:
    rien()

elif name in personne_lambda:
    if language=="1":
        personne_lambda_fr()
    elif language=="2":
        personne_lambda_de()
    elif language=="3":
        personne_lambda_en()
   
else:
    output_file.write('Name:'+name+'\n')  
    if language=="1":
        inconnu_fr()
    elif language=="2":
        inconnu_de()
    elif language=="3":
        inconnu_en()
    

output_file.close()

        
                if b in answer_yes:
                    print("That's nice.")
                elif b in answer_stop:
                    print('What a shame')  
                else:
                    print("Please answer correctly.")                
            else:
                if b in answer_yes:
                    print("I'm happy to hear that!")
                elif b in answer_stop:
                    input("Oh! What's the deal?\n")
                    c=input("I understand. Can I do something?\n")
                    if c in answer_yes:
                            input("Ok and what?\n")
                            print("I'll do my best.")
                    else:
                        print("Please answer correctly.")                
       
       
        elif ("How" or "how") and ("old") and ("You" or "you") in q:
            print("I was born on november the 10. 2018. I can't be more specific because I keep evolving")
        
        
        else:
            print('Ich bin noch nicht programiert um an dieser Frage zu beantworten.')
            output_file.write(q+'\n')  
        if a==False:
            q=input('Hast du eine andere Frage?\n')
        else:
            q=input('Haben sie eine andere Frage?\n')
    if a==False:
        print("Ciao (ja so wird es geschrieben).")
    else:
        print("Auf wiedersehen! Ich hoffe du hast einen guten Tag.")

        

def maitre_fr():
    print('Oh! Bonjour maitre, je ne vous avez pas reconnu!')
    qm=input('Allez vous bien?\n')
    if qm in answer_yes :
        print('Quelle bonne nouvelle')
    elif qm in answer_stop:
        print('Oh non!')
        input('Quel est votre probleme?\n')
        print('Hmmm. Oui je vois.')
    else:
        print('Oui je vois')
    question_fr()
 
def maitre_de():
    print('Oh! Hallo boss, ich habe sich nicht erkannt!')
    qm=input('Geht es ihnen gut?\n')
    if qm in answer_yes :
        print('Das ist schönn')
    elif qm in answer_stop:
        print('Oh nein!')
        input('Was ist den los?\n')
        print('Hmmm. Ja ich verstehe.')
    else:
        print('Ich verstehe')
    question_de()

def maitre_en():
    print('Oh! Hello master, I did not recognize you!')
    qm=input('How are you?\n')
    if qm in answer_yes :
        print('What a good new')
    elif qm in answer_stop:
        print('Oh no!')
        input("What's the problem?\n")
        print('Hmmm. Yeah I see.')
    else:
        print('Yeah I see.')
    question_en()      
    
    
    
def petitemerde_fr():
    input('Vous vous appellez bien petite merde? \n ')
    print('Bien petite merde.')
    question_fr()

def petitemerde_de():
    input('Heißt du wirklich Arschloch? \n ')
    print('Okay Arschloch.')
    question_de()
    
def petitemerde_en():
    input('Is your name douchbag? \n ')
    print('Okay douchbag.')
    question_en()    
       
    
def inconnu_fr():
    print("Bonjour "+name+"! Je vais rentrer votre nom le plus vite possible dans mon systeme!")
    question_fr()

def inconnu_de():
    print("Hallo "+name+"! Ich werde Ihren Namen so bald wie möglich in mein System eingeben!")
    question_de()

def inconnu_en():
    print("Hello "+name+"! I will enter your name as soon as possible in my system!")
    question_en()



def personne_lambda_fr():
    print('Bienvenue'+name+' !' )
    question_fr()

def personne_lambda_de():
    print("Wilkommen"+name+" !")
    question_de()
 
def personne_lambda_en():
    print("Welcome"+name+" !")
    question_en()

    

def rien():
    print('Bye') #I just want the program to stop when user write something in answer_stop
 


#The main program begins here


language=0
while not language=="1" or language=="2" or language=="3":
    language=input("\nSelect a language\nFor french type 1\nFor german type 2\nFor english type 3\nFor another language don't type anything because I don't know any other languages!\n")


if language==1:
    print("Pour tout le reste de ton temps avec moi je te prie d'ecrire clairement, sans erreurs et sans accents." )
    name=input('Bonjour! Quel est ton nom ?\n')
elif language==2:
    print("Für den ganzen Rest deiner Zeit mit mir schreib bitte deutlich und ohne Fehler." )
    name=input('Hallo! Wie heißt du?\n')
elif language==3:
    print("For the rest of your time with me please right clearly and properly.")
    name=input("Hi! What's your name?\n")
    

if name in name_chris:
    a=True    
    if language=="1":
        maitre_fr() 
    elif language=="2":
        maitre_de()
    elif language=="3":
        maitre_en()
    
elif name in name_freresoeur:
    a=False   
    if language=="1":
        petitemerde_fr()
    elif language=="2":
        petitemerde_de()
    elif language=="3":
        petitemerde_en()
    
elif name in answer_stop:
    rien()

elif name in personne_lambda:
    if language=="1":
        personne_lambda_fr()
    elif language=="2":
        personne_lambda_de()
    elif language=="3":
        personne_lambda_en()
   
else:
    output_file.write('Name:'+name+'\n')  
    if language=="1":
        inconnu_fr()
    elif language=="2":
        inconnu_de()
    elif language=="3":
        inconnu_en()
    

output_file.close()


        print('What a good new')
    elif qm in answer_stop:
        print('Oh no!')
        input("What's the problem?\n")
        print('Hmmm. Yeah I see.')
    else:
        print('Yeah I see.')
    question_en()      
    
    
    
def petitemerde_fr():
    input('Vous vous appellez bien petite merde? \n ')
    print('Bien petite merde.')
    question_fr()

def petitemerde_de():
    input('Heißt du wirklich Arschloch? \n ')
    print('Okay Arschloch.')
    question_de()
    
def petitemerde_en():
    input('Is your name douchbag? \n ')
    print('Okay douchbag.')
    question_en()    
       
    
def inconnu_fr():
    print("Bonjour "+name+"! Je vais rentrer votre nom le plus vite possible dans mon systeme!")
    question_fr()

def inconnu_de():
    print("Hallo "+name+"! Ich werde Ihren Namen so bald wie möglich in mein System eingeben!")
    question_de()

def inconnu_en():
    print("Hello "+name+"! I will enter your name as soon as possible in my system!")
    question_en()



def personne_lambda_fr():
    print('Bienvenue'+name+' !' )
    question_fr()

def personne_lambda_de():
    print("Wilkommen"+name+" !")
    question_de()
 
def personne_lambda_en():
    print("Welcome"+name+" !")
    question_en()

    

def rien():
    print('Bye') #I just want the program to stop when user write something in answer_stop
 


#The main program begins here


language=0
while not language=="1" or language=="2" or language=="3":
    language=input("\nSelect a language\nFor french type 1\nFor german type 2\nFor english type 3\nFor another language don't type anything because I don't know any other languages!\n")


if language==1:
    print("Pour tout le reste de ton temps avec moi je te prie d'ecrire clairement, sans erreurs et sans accents." )
    name=input('Bonjour! Quel est ton nom ?\n')
elif language==2:
    print("Für den ganzen Rest deiner Zeit mit mir schreib bitte deutlich und ohne Fehler." )
    name=input('Hallo! Wie heißt du?\n')
elif language==3:
    print("For the rest of your time with me please right clearly and properly.")
    name=input("Hi! What's your name?\n")
    

if name in name_chris:
    a=True    
    if language=="1":
        maitre_fr() 
    elif language=="2":
        maitre_de()
    elif language=="3":
        maitre_en()
    
elif name in name_freresoeur:
    a=False   
    if language=="1":
        petitemerde_fr()
    elif language=="2":
        petitemerde_de()
    elif language=="3":
        petitemerde_en()
    
elif name in answer_stop:
    rien()

elif name in personne_lambda:
    if language=="1":
        personne_lambda_fr()
    elif language=="2":
        personne_lambda_de()
    elif language=="3":
        personne_lambda_en()
   
else:
    output_file.write('Name:'+name+'\n')  
    if language=="1":
        inconnu_fr()
    elif language=="2":
        inconnu_de()
    elif language=="3":
        inconnu_en()
    

output_file.close()


  
