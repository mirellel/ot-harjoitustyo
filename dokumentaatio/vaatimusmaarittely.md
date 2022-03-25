# Vaatimus määrittely

## Sovelluksen tarkoitus
Sovelluksella voi pelata miinaharava-peliä. Pelissä on kolme eri vaikeustasoa.

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
   - Valittuaan uuden pelin, käyttäjä voi valita kolmesta eri vaikeustasosta
- Käyttäjä voi nähdä omat pelitilastonsa
   - Tilastoissa näkyy pelien voittoprosentti
   - Keskenjätetty peli ei näy tilastoissa
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita
- Mahdollisuus vaihtaa pelinäkymän värejä/teemaa
- Jokaisesta voitetusta pelistä käyttäjä saa tilille saldoa, jolla voi ostaa uusia teemoja
- Käyttäjä voi valita "pelilaudan" koon ja miinojen määrän itse
- Yleiset tilastot, jossa näkyy eniten voittoja tehneet pelaajat ja käyttäjän oma sijoitus
- Käyttäjä voi saada vinkkejä peliin
