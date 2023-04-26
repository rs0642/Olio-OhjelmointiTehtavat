import random

class Asiakas:
    def __init__(self, nimi, ika):
        self.__nimi = nimi  # Asiakkaan nimi
        self.__asiakasnro = self.__luo_nro()  # Asiakasnumero, joka generoidaan luokan sisäisesti
        self.__ika = ika  # Asiakkaan ikä

    def __luo_nro(self):
        numerot = []
        for i in range(3):
            x = random.randint(10, 99)  # Satunnainen kaksinumeroinen luku
            y = random.randint(100, 999)  # Satunnainen kolminumeroinen luku
            z = random.randint(100, 999)  # Satunnainen kolminumeroinen luku
            return (f"{x}-{y}-{z}")  # Palautetaan asiakasnumero muodossa "xx-yyy-zzz"

    def get_nimi(self):
        return self.__nimi  # Palautetaan asiakkaan nimi

    def get_ika(self):
        return self.__ika  # Palautetaan asiakkaan ikä

    def get_asiakasnro(self):
        return self.__asiakasnro  # Palautetaan asiakasnumero

    def set_nimi(self, nimi):
        if bool(nimi):  # Tarkistetaan, että uusi nimi ei ole tyhjä
            self.__nimi = nimi  # Asetetaan uusi nimi
        else:
            raise ValueError("Uusi nimi on annettava.")  # Jos uusi nimi on tyhjä, nostetaan virhe

    def set_ika(self, ika):
        if bool(ika):  # Tarkistetaan, että uusi ikä ei ole tyhjä
            self.__ika = ika  # Asetetaan uusi ikä
        else:
            raise ValueError("Uusi ikä on annettava.")  # Jos uusi ikä on tyhjä, nostetaan virhe

             

class Palvelu(Asiakas):
    def __init__(self, tuotenimi):
        self.tuotenimi = tuotenimi  # Palvelun tuotenimi
        self.__asiakkaat = []  # Asiakaslista, johon lisätään asiakkaita

    def _luo_asiakasrivi(self, asiakas):
        merkkijono = f'{asiakas.get_nimi()} {asiakas.get_asiakasnro()} on {asiakas.get_ika()}-vuotias'
        return (merkkijono)  # Palauttaa merkkijonon, joka kuvaa asiakasta

    def lisaa_asiakas(self, asiakas):
        self.__asiakkaat.append(asiakas)  # Lisätään asiakas listaan
        if bool(asiakas):
            self.__asiakas = asiakas
        else:
            raise ValueError("Asiakas on annettava.")  # Jos asiakas on tyhjä, nostetaan virhe

    def poista_asiakas(self, asiakas):
        self.__asiakkaat.remove(asiakas)  # Poistetaan asiakas listalta

    def tulosta_asiakkaat(self):
        print(f'Tuotteen {self.tuotenimi} asiakkaat ovat:')
        for asiakas in self.__asiakkaat:
            rivi = self._luo_asiakasrivi(asiakas)  # Luodaan merkkijono, joka kuvaa asiakasta
            print(rivi)  # Tulostetaan asiakkaan kuvaava merkkijono
        print()  # Tyhjä rivi tulostuksen loppuun

       
class ParempiPalvelu(Palvelu):
    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)  # Kutsutaan yläluokan konstruktoria
        self.__edut = []  # Edut-lista, johon lisätään palvelun edut

    def lisaa_etu(self, etu):
        self.__edut.append(etu)  # Lisätään etu listaan

    def poista_etu(self, etu):
        if etu == False:  # Jos etu on False, nostetaan virhe
             raise ValueError()
        if etu == True:  # Jos etu on True, poistetaan se listalta
            self.__edut.remove(etu)

    def tulosta_edut(self):
        print(f'Tuotteen {self.tuotenimi} edut ovat:')
        for etu in self.__edut:
            print(f'{etu}')  # Tulostetaan palvelun edut