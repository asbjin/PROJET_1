class Bateau :

    def __init__(self,id):
        long=0
        self.id=id
        if(id==1):
            self.long=5
        if(id==2):
            self.long=4
        if(id==3 or id==4 ):
            self.long=3
        if(id==5):
            self.long=2
        print(f"bateau avec id {self.id} a etait crée")
   

    def get_long(self):
        return self.long
    
    def get_id(self):
        return self.id
