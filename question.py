from preparing_movies import Preparing_Movies
from select_film import Select_Film
import os

class Question ():

    def head(self, ):

        print("######### Are you ready ############")

        print("1 - How long this movies?")
        print("2 - How is the Actor?")
        print("3 - When was Created?")
        print("4 - What are the Keywords?")
        print("5 - When was Created?")
        print("6 - When was Publish?")
        print("7 - Give me a Description?")
        print("8 - Whats is the Genre")
        print("9 - How is the Director?\n")
               

    def answers(self, ):
        
        self.select_movie = Preparing_Movies().name()
        print(f'Movie answers: {self.select_movie}')
        self.answer = ""

        resp = input("Do you know what's this movies?(Y/N): ")
                    
        if (resp == "Y") or (resp =="y") or (resp =="Yes") or (resp =="yes"):

            resp_movie = input("What's the movie: ")

            if resp_movie == self.select_movie:
                self.answer = "rigth"
                return(self.answer)
            else:
                print("Resposta errada")
                
        else:
            pass
                


    def question(self, ):

        right_film = Preparing_Movies().name()
        list_movies = Select_Film().movies()
        list_movies.append(right_film)
        self.mix = sorted(list_movies) 


        self.duration      = Preparing_Movies().duration()
        self.actor         = Preparing_Movies().actor()
        self.creator       = Preparing_Movies().creator()
        self.keywords      = Preparing_Movies().keywords()
        self.datas_created = Preparing_Movies().datas_created()
        self.data_publish  = Preparing_Movies().data_publish()
        self.description   = Preparing_Movies().description()
        self.genre         = Preparing_Movies().genre()
        self.director      = Preparing_Movies().director()

        answer = ""
        cont = 0
        cont_qst = 0

        while answer != "rigth":

            del self.mix[cont_qst]
            self.mix = sorted(list_movies)

            print("MOVIES LIST FOR YOU CHOSE: \n")

            for index, item in enumerate(self.mix):
                print(index,item)
            
            lang = input("\nChoise your question: ")

            match lang:

                case "1":
                    cont += 1
                    cont_qst += 1
                    print("1 - How long this movies?")
                    print(self.duration)
                    
                    # os.system('cls')

                    answer = Question().answers()

                    if answer == 'rigth':
                        print("Congratulation")
               
                case "2":

                    cont += 1
                    cont_qst += 1
                    print("2 - How is the Actor?")

                    for index, item in enumerate(self.actor):
                        print(index,item)

                    answer = Question().answers()             

                    if answer == 'rigth':
                        print("Congratulation")

                case "3":

                    cont += 1
                    cont_qst += 1
                    print("3 - How is the Create?")
                    print(self.creator)
                    
                    answer = Question().answers()
    
                    if answer == 'rigth':
                        print("Congratulation")

                case "4":

                    cont += 1
                    cont_qst += 1
                    print("4 - What are the Keywords?")
                    print(self.keywords)
                    
                    answer = Question().answers()
                    if answer == 'rigth':
                        print("Congratulation")

                case "5":

                    cont += 1
                    cont_qst += 1
                    print("When was Created?")
                    print(self.datas_created)
                    
                    answer = Question().answers()
                    if answer == 'rigth':
                        print("Congratulation")
                
                case "6":

                    cont += 1
                    cont_qst += 1
                    print("When was Publish?")
                    print(self.data_publish)
                    
                    answer = Question().answers()
                    if answer == 'rigth':
                        print("Congratulation")

                case "7":

                    cont += 1
                    cont_qst += 1
                    print("7 - Give me a Description? ")
                    print(self.description)
                
                    answer = Question().answers()
                    if answer == 'rigth':
                        print("Congratulation")

                case "8":

                    cont += 1
                    cont_qst += 1
                    print("8 - Whats is the Genre")
                    print(self.genre)
                    
                    answer = Question().answers()
                    if answer == 'rigth':
                        print("Congratulation")

                case "9":

                    cont += 1
                    cont_qst += 1
                    print("9 - How is the Director?")
                    print(self.director)
                    
                    answer = Question().answers()
                    if answer == 'rigth':
                        print("Congratulation")

                case _:
                    print("The language doesn't matter, what matters is solving problems.")
            
        self.score = 100/cont
            

        return(self.score)
        

head = Question().head()

test = Question().question()
print(f'Your score is {test}')

# test2 = Question().answers()

