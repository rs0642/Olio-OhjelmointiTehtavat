import random #Lisätty random 
"""Bug Hunt - Buginmetsästys

Yksinkertainen peli, jossa hahmo tutkii luolaa etsien bugeja. Kun hahmo (@)
ohjataan bugin (B) päälle, se hoitelee bugin, joka poistetaan pelistä. Lopuksi
kerrotaan montako bugia hoideltiin ja monellako siirrolla.

Luolassa erotellaan tutkitut (.) ja tutkimattomat (#) ruudut. Hahmoa siirretään
antamalla ilmansuunta (NESW). Luolan ulkopuolelle vieviä ilmansuuntia ei voi
antaa.

Pelin alussa käyttäjältä kysytään miten suuri luola tehdään ja montako bugia
sinne sijoitetaan. Luola on aina neliö, jossa on pysty- ja vaakasuunnassa
annettu määrä ruutuja.
"""

class Luola:
    """Kuvaa neliön muotoisen luolan.

    :param koko: Kokonaisluku, luolan sivun pituus ruutuina.
    """

    # Tutkimattomia ja tutkittuja ruutuja kuvaavat merkit.
    OUTO = '#'
    TUTTU = '.'

    def __init__(self, koko):
        # self.ruudut on lista, joka kuvaa luolan ruutuja. Se sisältää listoja,
        # joista kukin kuvaa yhden ruutujen rivin. Rakenne on siis seuraava:
        # [[0, 1, 2],
        #  [3, 4, 5],
        #  [6, 7, 8]]
        # Tässä luolan ruudut on numeroitu havainnollistamisen vuoksi.
        # Kukin ruutu on merkki, joka kertoo onko ruutu tutkittu vai ei.
        self.ruudut = []
        for x in range(koko):
            self.ruudut.append([self.OUTO] * koko)
        # Tulostetaan tunnelmaan virittävä viesti.
        # "{} ja {}".format(foo, bar) sijoittaa merkkijonossa {}-merkkien
        # kohdalle muuttujien foo ja bar arvon järjestyksessä edeten.
        # Merkkijonon sisällä oleva ohjausmerkki \n on rivinvaihto.
        print("Luotiin {}x{} luola. Pidä hauskaa!\n".format(koko, koko))
        # self.otukset tallentaa luolassa olevan hahmon ja bugit olioina.
        self.otukset = []

    def tutki(self, x, y):
        """Merkitsee annetun ruudun ja sitä ympäröivät ruudut tutkituiksi."""
        # for käy läpi rivin, jolla annettu ruutu on, sekä sitä edeltävän ja
        # sen jälkeisen rivin.
        for rivi in (y-1, y, y+1):
            # if tarkistaa onko rivi luolan rajojen ulkopuolella.
            if rivi < 0 or rivi >= len(self.ruudut):
                continue
            # for käy läpi sarakkeen (pystyrivin), jolla annettu ruutu on, sekä
            # sitä edeltävän ja sen jälkeisen sarakkeen.
            for sarake in (x-1, x, x+1):
                # if tarkistaa onko sarake luolan rajojen ulkopuolella.
                if sarake < 0 or sarake >= len(self.ruudut):
                    continue
                # Silmukoiden nykyisen kierroksen ruutu merkitään tutkituksi,
                # koska se täytti ehdot ja on luolan sisäpuolella.
                # Huomaa että tämä poistaa näkyvistä ruudussa mahdollisesti
                # sijaitsevan otuksen, joka sijoitetaan näkyviin
                # paivita-metodissa.
                self.ruudut[rivi][sarake] = self.TUTTU

    def tulosta(self):
        """Tulostaa luolan tilanteen ruudulle."""
        # for käy läpi kaikki luolan rivit.
        for rivi in self.ruudut:
            # for käy läpi kaikki rivin ruudut.
            for ruutu in rivi:
                # Tulostetaan ruutu laittamatta sen perään rivinvaihtoa.
                print(ruutu, end='')
            # Tulostetaan rivin viimeisen ruudun jälkeen rivinvaihto.
            print()

    def paivita(self):
        """Päivittää luolan otusten sijainnit."""
        # for käy läpi kaikki luolan otukset.
        for otus in self.otukset:
            # Sijoitetaan otuksen merkki sen sijaintiruutuun, jos ruutu on
            # tutkittu.
            if self.ruudut[otus.y][otus.x] == self.TUTTU:
                self.ruudut[otus.y][otus.x] = otus.MERKKI


class Otus:
    """Kuvaa jotakin otusta, joka sijaitsee luolassa.

    Tämä on ns. abstrakti yläluokka, jonka muut luokat voivat periä. Tästä
    luokasta ei ole tarkoitus luoda olioita, vaan oliot luodaan näistä perivistä
    alaluokista.

    Luokan perivät luokat saavat käyttöönsä kaikki yläluokan ominaisuudet, mutta
    voivat lisäksi määritellä omia ominaisuuksiaan. Tällainen perintä kuuluu
    merkittäviin olio-ohjelmoinnin mahdollistamiin työkaluihin.
    """

    # Otuksen oma merkki, jolla sitä kuvataan kartalla.
    # Otus-luokan merkki on None, mikä tarkoittaa, että sen perivien luokkien
    # tulee kunkin määritellä oma merkkinsä.
    MERKKI = None

    def __init__(self):
        # Jokaisella oliolla on sijainti, joka tallennetaan x- ja
        # y-koordinaatteina. Näistä x kuvaa luolan saraketta ja y riviä.
        # Näihin tallennetaan oletuksena nollat, mutta tässäkin voisi olla None,
        # jolloin aliluokkien tulisi aina määritellä koordinaatit itse.
        self.x = 0
        self.y = 0


# Alaluokalle annetaan parametrina sen yläluokka.
class Hahmo(Otus):
    """Kuvaa hahmoa, pelimme sankaria.

    Hahmoa voidaan siirtää luolassa.

    :param nimi: Merkkijono, hahmon nimi.
    """

    MERKKI = '@'

    def __init__(self, nimi):
        # Alaluokan tulee kutsua __init__-metodissaan yläluokan
        # __init__-metodia, jotta se saa käyttöönsä yläluokan tarjoamat
        # ominaisuudet.
        Otus.__init__(self)
        # Tallennetaan parametrina saatu nimi olion omaan muuttujaan, jolloin
        # se on käytössä koko olion olemassaolon ajan.
        self.nimi = nimi

    def liiku(self, dx, dy):
        """Siirtää olion sijaintia.

        :param dx: Kokonaisluku, sijainnin muutos vaakasuunnassa.
        :param dy: Kokonaisluku, sijainnin muutos pystysuunnassa.
        """
        # Jos dx on False, se on nolla, eikä vaakasuunnassa liikuta.
        if dx:
            # Lisätään dx olion x-muuttujan arvoon. Jos dx on negatiivinen,
            # tämä siirtää hahmoa vasempaan. Positiivinen dx siirtää oikealle.
            self.x += dx
        if dy:
            self.y += dy


class Bugi(Otus):
    """Kuvaa bugia, sankarimme metsästämää kohdetta.

    Bugi pysyy paikallaan pelin ajan.

    :param x: Kokonaisluku, bugin sijainti vaakasuunnassa.
    :param y: Kokonaisluku, bugin sijainti pystysuunnassa.
    """

    MERKKI = 'B'

    def __init__(self, x, y):
        Otus.__init__(self)
        self.x = x
        self.y = y


class Peli:
    """Mallintaa pelin, jossa itse toiminta tapahtuu.

    :param koko: Kokonaisluku, luolan sivun pituus.
    :param bugeja: Kokonaisluku, bugien määrä luolassa.
    """

    def __init__(self, koko, bugeja):
        self.koko = koko
        # self.luola on pelialueemme, Luola-luokasta luotu olio, joka kuvaa
        # neliön mallista luolaa, jonka sivun pituus on annettu koko.
        self.luola = Luola(self.koko)
        # self.hahmo on sankarimme, jolle annetaan tässä aina sama nimi 'foo'.
        self.hahmo = Hahmo('foo')
        # Sankarimme lisätään luolan otuksiin.
        self.luola.otukset.append(self.hahmo)
        # self.bugit on lista, joka sisältää luolassamme piileskelevät bugit.
        # Kukin näistä bugeista, eli listan alkioista, on Bugi-luokan olio.
        self.bugit = []
        # for luo bugeja parametrina annetun määrän.
        for i in range(0, bugeja):
            # Kukin bugi luodaan omassa metodissaan _luo_bugi().
            bugi = self._luo_bugi()
            # Bugi lisätään sekä pelin että luolan ylläpitämiin listoihin.
            self.bugit.append(bugi)
            self.luola.otukset.append(bugi)
        # Pelin alustuksen lopuksi merkitään sankarimme ruutu sekä hänen
        # ympärillään olevat ruudut tutkituiksi.
        self.luola.tutki(self.hahmo.x, self.hahmo.y) # korjattu kirjoitusvirhe

    # Alaviiva metodin nimen edessä kertoo, että kyseistä metodia on tarkoitus
    # kutsua vain tämän luokan sisällä.
    def _luo_bugi(self):
        """Luo bugin, jonka sijainti on satunnainen tutkimaton luolan ruutu.

        return: Bugi, uusi bugi satunnaisessa sijainnissa.
        """
        # Arvotaan bugin x- ja y-koordinaatti siten, että ne ovat luolan
        # sisällä (luvun yläraja) eivätkä ole sankarimme ruudussa (0, 0) tai
        # heti sen vieressä (luvun alaraja). Sankarin vieressä ovat (0, 1) ja
        # (1, 0). Sankari näkee myös viistosti ruudun (1, 1), muttei pääse
        # siihen yhdellä siirrolla, joten sen ei katsota olevan vieressä.
        x = random.randint(1, self.koko - 1)
        y = random.randint(1, self.koko - 1) # lisätty - 1
        # return-lauseessa luodaan bugi arvotuilla koordinaateilla ja
        # palautetaan se.
        return Bugi(x, y)

    def _luo_suunnat(self):
        """Luo listan liikesuunnista, jotka pitävät hahmon luolan sisällä.

        :return: Lista, mahdolliset liikesuunnat kirjaimin NESW.
        """
        # suunnat-listaan kerätään mahdolliset liikesuunnat.
        suunnat = []
        # if-lauseet tarkistavat veisikö kunkin liikesuunnan valitseminen hahmon
        # luolan rajojen ulkopuolelle.
        if self.hahmo.y > 0:
            # Jos liikesuunta pitäisi hahmon luolan sisäpuolella, lisätään se
            # suunnat-listaan.
            suunnat.append('N')
        if self.hahmo.x < self.koko - 1:
            suunnat.append('E')
        if self.hahmo.y < self.koko - 1:
            suunnat.append('S')
        if self.hahmo.x > 0:
            suunnat.append('W')
       
        return suunnat

    def _kysy_suunta(self):
        """Kysyy käyttäjältä liikesuunnan.

        :return: Monikko, muutokset x- ja y-koordinaatteihin muodossa (dx, dy).
        """
        # suunnat-muuttujaan tallennetaan mahdolliset liikesuunnat listana.
        suunnat = self._luo_suunnat()
        # suunta-muuttujaan tallennetaan käyttäjän antama liikesuunta.
        # ''.join(suunnat) liittää suunnat-listan alkiot yhteen merkkijonoksi,
        # laittaen alkioiden väliin tyhjän merkkijonon '', eli käytännössä
        # sijoittaen ne peräkkäin. Esim. ''.join(['N', 'E']) == 'NE'.
        suunta = input("Valitse suunta ({}):" .format(''.join(suunnat))) #" paikkaa muutettu
        # if-elif-haarat tarkistavat, onko kukin ilmansuunta mahdollisissa
        # suunnissa JA onko käyttäjän antama suunta kyseisen ilmansuunnan
        # kirjain pienenä tai isona. Esim. 'n' in ('N', 'n') == True.
        if 'N' in suunnat and suunta in ('N', 'n'):
            # Jos kyseinen suunta oli sallittu ja käyttäjän antama suunta,
            # palautetaan hahmoa yhden askeleen kyseiseen ilmansuuntaan
            # siirtävät x- ja y-muutokset monikkona muodossa (dx, dy), missä
            # dx on muutos vaakasuunnassa ja dy muutos pystysuunnassa.
            return (0, -1)
        elif 'E' in suunnat and suunta in ('E', 'e'):
            return (1, 0)
        elif 'S' in suunnat and suunta in ('S', 's'):
            return (0, 1)
        elif 'W' in suunnat and suunta in ('W', 'w'):
            return (-1, 0)
        else:
            # Jos käyttäjä antoi jotain muuta kuin sallitun suunnan, pyydetään
            # suuntaa uudestaan, muistuttaen mahdollisista suunnista.
            print("Sallitut suunnat ovat ({}).\n".format(''.join(suunnat)))
            # return hyödyntää rekursio-nimistä ohjelmointitekniikkaa, jossa
            # funktion sisältä kutsutaan funktiota itseään. Tämä voidaan tehdä
            # vaikka kuinka monta kertaa, sillä kun käyttäjä viimein antaa
            # sallitun suunnan, se palautetaan ketjussa takaisin päin aina
            # ensimmäiseen funktiokutsuun saakka, josta se palautetaan edelleen
            # funktion ulkopuoliselle kutsujalle.
            return self._kysy_suunta()

    def _debuggaa(self):
        """Poistaa bugin, jos hahmo on sen kohdalla.

        :return: True jos bugi poistettiin, muuten False.
        """
        # for käy läpi kaikki bugit pelin bugilistassa.
        for bugi in self.bugit:
            # if-lauseet tarkistavat ovatko hahmon ja bugin x- ja y-koordinaatit
            # samat.
            if bugi.x == self.hahmo.x:
                if bugi.y == self.hahmo.y:
                    # Jos hahmo ja tämä bugi ovat samassa paikassa, poistetaan
                    # tämä bugi sekä pelin että luolan ylläpitämistä listoista
                    # ja palautetaan True.
                    self.bugit.pop(self.bugit.index(bugi))
                    self.luola.otukset.pop(self.luola.otukset.index(bugi))
                    return True
        # Mikäli yksikään bugi ei ollut samassa ruudussa sankarin kanssa,
        # palautetaan False.
        return False

    def main(self):
        # Mikäli yksikään bugi ei ollut samassa ruudussa sankarin kanssa,
        # palautetaan False.
        siirrot = 0
        # bugit laskee montako bugia on hoideltu.
        bugit = 0
        # Monissa ohjelmissa on tällainen pääsilmukka, jossa sen jatkuvaa
        # toimintaa hallitaan suorituksen ajan.
        while True:
            # Päivitetään luolan otusten sijainti.
            self.luola.paivita()
            # Tulostetaan luola nykyisessä tilassaan.
            self.luola.tulosta()
            # Jos bugeja ei ole jäljellä, poistutaan pääsilmukasta.
            if not self.bugit:
                break
            # Kysytään käyttäjältä liikesuunta.
            suunta = self._kysy_suunta()
            # Liikutetaan sankariamme annettuun suuntaan.
            # Tässä asteriski (*) kohdassa *suunta purkaa argumenttina annetun
            #(dx, dy)-monikon alkiot erillisiksi muuttujiksi dx ja dy ennen
            # funktiolle liiku syöttämistä. Tämä siksi, että funktio ottaa
            # parametreinaan x- ja y-siirtymät erillisinä. Kyseessä on siis
            # lyhyempi tapa kirjoittaa self.hahmo.liiku(suunta[0], suunta[1]).
            self.hahmo.liiku(*suunta)
            # Sankarimme siirtyi, joten kasvatetaan siirtolaskuria yhdellä.
            siirrot += 1
            # Tutkitaan sankarimme uuden sijainnin viereiset ruudut.
            self.luola.tutki(self.hahmo.x, self.hahmo.y)
            # Jos sankarimme sijainnista löytyi bugi (_debuggaa() palauttaa
            # True, jos löytyi), kasvatetaan hoideltujen bugien laskuria
            # yhdellä.
            if self._debuggaa():
                bugit += 1
            # Tulostetaan rivinvaihto kierrosten erottamiseksi toisistaan. Tämä
            # tehdään ihan selkeyden vuoksi.
            print()

        # Kun pääsilmukasta poistutaan, tulostetaan tieto montako bugia
        # hoideltiin ja monellako siirrolla.
        # Pitkä koodirivi on jaettu useammalle riville \-merkkiä käyttäen.
        print("\n\n*** {} bugia hoideltu {} siirrolla! ***\n\n".format(bugit, \
                                                                       siirrot))


# Kun ohjelma suoritetaan, nämä rivit suoritetaan ennen aiempia luokkien
# määrittelyjä. Luokkien sisältämä koodi suoritetaan vasta sitten, kun sitä
# ohjelman suorituksen aikana tarvitaan.

# Kysytään käyttäjältä pelialueen koko ja bugien määrä.
koko = int(input("Miten iso luola? ")) #int 
bugeja = int(input("Montako bugia? ")) #int
# Luodaan uusi Peli-olio käyttäen annettuja arvoja.
# Tässä vaiheessa Peli-olion alustaminen aiheuttaa sen __init__()-metodissa myös
# Luola-, Hahmo- ja Bugi-olioiden luomiset.
peli = Peli(koko, bugeja)
# Käynnistetään Peli-olion päämetodi, mikä käynnistää pelin.
peli.main()