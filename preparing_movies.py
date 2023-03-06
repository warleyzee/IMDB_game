from pprint import pprint

class Preparing_Movies():

    def arq(self, ):
        from select_film import Select_Film
        self.arq = Select_Film().salve_film()
        #pprint(self.arq)
        
        return(self.arq)

    def name(self, ):
        data_name = Preparing_Movies().arq()

        if data_name == "":
            self.nome = "Outro Filme"
        else:
            self.name = data_name["Name"]
            print(f'Nome do filme e: {self.name}')
        return(self.name)

    def duration (self, ):
        data_duration = Preparing_Movies().arq()
        self.durantion = data_duration["Duration"]

        return(self.durantion)
    
    def actor(self,):

        data_actor = Preparing_Movies().arq()
        actor = data_actor["Actor"]
        self.list_actor = []

        for i in actor:
            self.list_actor.append(i["name"])

        return(self.list_actor)

    def creator(self, ):

        data_creator = Preparing_Movies().arq()
        creator = data_creator["Creator"]
        self.list_creator = []

        for i in creator:
            self.list_creator.append(i["name"])
        
        return(self.list_creator)
    
    def keywords(self, ):

        data_keywords = Preparing_Movies().arq()
        self.keyword = data_keywords["Keywords"]

        return(self.keyword)
    
    def datas_created(self, ):

        data_created = Preparing_Movies().arq()
        created = data_created["Date Created"]
        day_cre = created[8:10]
        month_cre = created[5:7]
        year_cre = created[0:4]
        self.formt_created = (f'{day_cre}/{month_cre}/{year_cre}')
        
        return(self.formt_created)
   
    def data_publish(self, ):

        data_publish = Preparing_Movies().arq()
        publish = data_publish["Data Publish"]
        day_pub = publish[8:10]
        month_pub = publish[5:7]
        year_pub = publish[0:4]
        self.formt_publish = (f'{day_pub}/{month_pub}/{year_pub}')
        
        return(self.formt_publish)

    def description(self,):

        data_description = Preparing_Movies().arq()
        self.description = data_description["Description"]

        return(self.description)

    def genre(self,):
        
        data_genre = Preparing_Movies().arq()
        self.genre = data_genre["Genre"]

        return(self.genre)

    def director (self, ):
        
        data_director = Preparing_Movies().arq()
        director = data_director["Director"]
        self.list_director = []

        for i in director:
            self.list_director.append(i["name"])
        
        return(self.list_director)



# test = Preparing_Movies().arq()