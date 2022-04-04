# Vaatimus määrittely

## Sovelluksen tarkoitus
#### (minun piti ensin tehdä miinaharava-peli, mutta se osoittautui hieman liian vaikeaksi)

Sovelluksella voi pelata wordle-tyyppistä peliä
Wordle on newyorktimes -lehden sanaarvauspeli, jossa pelaajan tulee kuudella vuorolla arvata oikein 5-kirjaiminen 
englanninkielinen sana. Peli näyttää jokaisen arvauksen jälkeen oikealla paikalla olevat kirjaimet vihreällä ja oikeassa sanassa olevat, mutta arvauksessa väärässä kohdassa olevat kirjaimet keltaisella

## Käyttäjät
Sovelluksella on vain yksi käyttäjärooli

## Käyttöliittymät
Sovellus aukeaa kirjautumisnäkymään, josta on mahdollista luoda uusi käyttäjä. Käyttäjän luomiselle 
on oma luomisnäkymä. Onnistuneen kirjautumisen jälkeen avautuu valikko, josta voi valita uuden pelin, pelitilastot, tai kirjautua ulos. 


## Ennen kirjautumista
- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
   - Tunnus pitää olla uniikki ja vähintään kolmen merkin pituinen
- Käyttäjä voi kirjautua järjestelmään
   - Kirjautuminen onnistuu, kun syötetään olemassaoleva käyttäjätunnus ja oikea salasana
   - Järjestelmä ilmoittaa virheestä, jos salasana on väärin tai käyttäjätunnusta ei ole

## Kirjautumisen jälkeen
- Käyttäjä voi valita, että pelaa uuden pelin
- Käyttäjä voi nähdä omat pelitilastonsa
   - Tilastoissa näkyy pelien voittoprosentti ja jakauma siitä, kuinka monennella arvauksella käyttäjä sai sanan        oikein
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita
- Mahdollisuus vaihtaa pelinäkymän värejä/teemaa
- Käyttäjä voi valita 6-kirjaimen peliversion
- Yleiset tilastot, jossa näkyy eniten voittoja tehneet pelaajat ja käyttäjän oma sijoitus
