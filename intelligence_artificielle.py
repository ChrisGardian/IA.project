#3 u 
import loging




#All the list are here
name_chris=['christopher','chris','Chris','Christopher']
name_freresoeur=["Estelle","estelle","mathieu","Mathieu"]
answer_stop=["non", "Non", "no", "No", "n", "N",'exit','Exit']
answer_yes=['Ouais','ouais','Oui','oui','Yes','yes','Yep','yep','Y','y','oui merci','Oui merci']




def question():    
    q=raw_input("Avvez-vous une question?")
    while (q not in answer_stop):
       
       if ("Qui" or "qui") and ("meilleur") in q:
            if a==True:
                print("C'est vous maitre bien sur")
            else:
                print("C'est le maitre Christopher bien sur.")
            
       
       elif q in answer_yes:
            if a==False:
                print("Ben pose la qu'est ce que t'attend.")
            else:                
                print("J'attends la question avec impatience")
                
       
       elif ("Ca" or "ca") and ("va") in q:
            b=raw_input('Bien et est ce que ca va?')
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
                    raw_input("Ah bon! Qu'est ce qui ne va pas?")
                    c=raw_input("Oui je vois. Est ce que je peut faire quelque chose?")
                    if c in answer_yes:
                            raw_input("Tres bien qu'est ce que je peut faire?")
                            print("Je ferais de mon mieux")
                    else:
                        print("Reponds correctement aux question s'il te plait")  
       
       
       #elif: 
        
       else:
            print('Je ne suis pas encore programmee pour repondre a une telle question')
        q=raw_input('Avez vous une autre question?')
    print("Au revoir! J'espere que vous passez une bonne journee.")


def maitre():
    print('Oh! Bonjour maitre, je ne vous avez pas reconnu!')
    qm=raw_input('Allez vous bien?')
    if qm in answer_yes :
        print('Quelle bonne nouvelle')
    elif qm in answer_stop:
        print('Oh non!')
        raw_input('Quel est votre probleme?')
        print('Hmmm. Oui je vois.')
    else:
        print('Oui je vois')
    
    question()
    
      
def petitemerde():
    raw_input('Vous vous appellez bien petite merde?  ')
    print('Bien petite merde.')
    question()
        
def inconnu():
    print("Bonjour inconnu! Je vais rentrer votre nom le plus vite possible dans mon systeme!")
    question()

def rien():
    print('Bye') #I just want the program to stop when user write something in answer_stop
 





print('')
print("Pour tout le reste ou tu seras avec moi je te prie d'ecrire clairement avec ponctuation et sans espace inutile" )
name=raw_input('Bonjour!Quel est ton nom ?  ')
if name in name_chris:
    a=True    
    maitre() 
    
elif name in name_freresoeur:
    a=False   
    petitemerde()
    
elif name in answer_stop:
    rien()
else:
    inconnu()
    
  
  
