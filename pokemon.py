class Pokemon(): #Définit ce qu'est un pokémon
    def __init__(self,nb,nom,desc,type,basepv,atk,defn,resn,atk1,atk2,atk3,atk4,portrait,sprite,sprite_type):
        self.__id=nb
        self.__nom=nom
        self.__desc=desc
        self.__type=type
        self.__basepv=basepv
        self.__atk=atk
        self.__defn=defn
        self.__resn=resn
        self.__attaques=[atk1,atk2,atk3,atk4]
        self.__portrait=portrait
        self.__sprite=sprite
        self.__sprite_type=sprite_type
    def retourneid(self):
        return(self.__id)
    def retournenom(self):
        return(self.__nom)
    def retournedesc(self):
        return(self.__desc)
    def retournetype(self):
        return(self.__type)
    def retournebasepv(self):
        return(self.__basepv)
    def retourneatk(self):
        return(self.__atk)
    def retournedef(self):
        return(self.__defn)
    def retourneres(self):
        return(self.__resn)