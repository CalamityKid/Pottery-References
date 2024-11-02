import user_input 
from Classes.FunctionalPottery import FunctionalPottery
from Classes.Planters import Planter
from Classes.Decorative import Decorative
def programa():
    print ("\nWelcome to the pottery recomendation program.")
    print ("This will eventually help you make custom orders too.")
    print ("I'll ask a few questions to lead you through the things I've made so far.\n\n")
    print ("First of all, do you eat or drink in it?")

    functional = user_input.yes_or_no()
    if functional == True:
        answer = user_input.select_categories(FunctionalPottery)
        print (answer)
        return answer
    else:
        #planter or decorative
        print ("\nWill it house a living plant?")
        planterbool = user_input.yes_or_no()
        if planterbool == True:
            answer = user_input.select_categories(Planter)
            print (answer)
            return answer
        else:
            answer = user_input.select_categories(Decorative)
            print (answer)
            return answer

            

programa()
