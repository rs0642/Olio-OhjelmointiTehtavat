import random

class Asiakas:
    def __init__(self, nimi, ika):
        self.__nimi = nimi
        self.__asiakasnro = self.__luo_nro()
        self.__ika = ika
   
    def __luo_nro(self):
        nrot = []
        for i in range(3):
            x = random.randint(10, 99)
            y = random.randint(100, 999)
            z = random.randint(100, 999)
            return (f"{x}-{y}-{z}")
    
    def get_nimi(self):
        return self.__nimi
    
    def get_ika(self):
        return self.__ika
    
    def get_asiakasnro(self):
        return self.__asiakasnro
    
    def set_nimi(self, nimi):
        if nimi == "":
            raise ValueError("Uusi nimi on annettava.")
        if nimi == True:
            self.__nimi = nimi
   
    def set_ika(self, ika):
        if bool(ika):
            self.__ika = ika
        else:
            raise ValueError("Uusi ikä on annettava.")

class Palvelu(Asiakas):
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakasrivi(self, asiakas):
        merkkijono = f'{asiakas.get_nimi()} {asiakas.get_asiakasnro()} on {asiakas.get_ika()}-vuotias'
        return (merkkijono)
    
    def lisaa_asiakas(self, asiakas):
        self.__asiakkaat.append(asiakas)
        if bool(asiakas):
            self.__asiakas = asiakas
        else:
            raise ValueError("Uusi asiakas on annettava.")

    def poista_asiakas(self, asiakas):
        self.__asiakkaat.remove(asiakas)
    
    def tulosta_asiakkaat(self):
        print(f'Tuotteen {self.tuotenimi} asiakkaat ovat:')
        for asiakas in self.__asiakkaat:
            rivi = self._luo_asiakasrivi(asiakas)
            print(rivi)
        print("")
        


class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, etu):
        self.__edut.append(etu)

    def poista_etu(self, etu):
        if etu == False:
            raise ValueError("Uusi ikä on annettava.")
        if etu == True:
            self.__edut.remove(etu)

    def tulosta_edut(self):
        print(f'Tuotteen {self.tuotenimi} edut ovat:')
        for etu in self.__edut:
            print(f'{etu}')