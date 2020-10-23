
#this is the template for making PartyAnimal

class PartyAnimal:                      #class is reserved word
    x=0                                 # each PartyAnimal has a bit of data
    def party(self):                        #each party animal object has a bit of code
        self.x = self.x+1
        print("So far",self.x)

an = PartyAnimal()                        # Constuct a PartyAnimal object and store in an variable


#def party() tells the object to run the party() code within it.
an.party()
an.party()                               # PartyAnimal.party(an)
an.party()