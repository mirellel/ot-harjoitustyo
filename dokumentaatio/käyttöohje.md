# Käyttöohje

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Kirjautuminen
Sovellus käynnistyy kirjautumisnäkymään
![image](https://user-images.githubusercontent.com/101889891/166432882-e9b8d22b-480b-4526-8533-e1f6956d83fe.png)

Kirjautuminen onnistuu kirjoittamalla olemassaoleva käyttäjätunnus sekä salasana syöttökenttän ja painamalla "Login"-painiketta

## Uuden käyttäjän luominen
Kirjautumisnäkymästä on mahdollista siirtyä uuden käyttäjän luomisnäkyään painamalla "Create user"-painiketta.

Uusi käyttäjä luodaan syöttämällä tiedot syötekenttiin ja painamalla "Create"-painiketta:

![image](https://user-images.githubusercontent.com/101889891/166433316-0eef12d7-63ad-4611-ac56-274ab100fb69.png)

Jos käyttäjän luominen onnistuu, siirtyy ohjelma käyttäjänäkymään.

## Pelaaminen

Kun käyttäjä on kirjautunut sisään, hän voi käynnistää pelin painamalla "Play"-painiketta.

Nyt ruudulle avautuu pelinäkymän aloitusmenu, josta pelin voi aloittaa painamalla "Start game"-painiketta. Sovelluksen voi sulkea painamalla "Quit"-painiketta.

![aloitusmenu](https://user-images.githubusercontent.com/101889891/166437141-1232f5b8-e9cd-4a8c-ac22-211a66daa281.png)


![tyhjäpeliruutu](https://user-images.githubusercontent.com/101889891/166434022-cf66d537-0c84-4903-990c-bb089acc5272.png)

Peliä pelataan kirjoittamalla 5-kirjaiminen englanninkielinen sana ja painamalla enter-näppäintä näppäimistöllä. Tämän jälkeen arvaus ilmestyy ylimpiin ruutuihin. Ruutujen väri ilmoittaa, kuinka lähellä arvaus on.

![arvaukset](https://user-images.githubusercontent.com/101889891/166434437-e56ba5c2-991e-4897-b798-92f7f3f630eb.png)

Jos käyttäjän arvaama sana ei ole sovelluksen hyödyntämässä sanalistassa tai arvattu sana on liian lyhyt, antaa peli virheilmoituksen.

Vihreä ruutu tarkoittaa, että kirjain on voittosanassa täysin samassa paikassa. Keltainen ruutu tarkoittaa että kirjain on voittosanassa, mutta väärässä kohdassa. Harmaa ruutu tarkoittaa, että kirjain ei ole voittosanassa ollenkaan.

Jos käyttäjä ehtii arvata voittosanan oikein kuudella yrityksellä, voittaa hän pelin. Tämän jälkeen avautuu menu, jossa lukee voittosana. Menusta voi valita uuden pelin "Replay"-painiketta painamalla tai palata takaisin aloitusmenun "Main menu"-painiketta painamalla.

![voittomenu](https://user-images.githubusercontent.com/101889891/166434514-b90e028a-c0a6-4205-a660-08cb968de5cc.png)



