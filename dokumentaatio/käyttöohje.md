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

HUOM! käyttäjänimen tulee olla kokonaan pienillä kirjaimilla.

Jos käyttäjän luominen onnistuu, syöttökentät pyyhkiytyvät ja käyttäjä voi siirtyä kirjautumisnäkymään painamalla "Login"-painiketta.

## Pelaaminen

Kun käyttäjä on kirjautunut sisään, pelinäkymä avautuu heti.

Pelinäkymä avautuu ensin aloitusmenuun, jossa näkyy kirjautuneen käyttäjän käyttäjätunnus, voitettujen pelien määrä, pelattujen pelien määrä ja voittoprosentti. Pelin voi aloittaa painamalla "START GAME"-painiketta. Sovelluksen voi sulkea painamalla "QUIT"-painiketta.

![startmenu](https://user-images.githubusercontent.com/101889891/168469179-8dfbf220-2e3d-442c-ad02-784b64d44a55.png)

"START GAME"-painikkeen painamisen jälkeen ruudulle avautuu peli:

![tyhjäpeliruutu](https://user-images.githubusercontent.com/101889891/166434022-cf66d537-0c84-4903-990c-bb089acc5272.png)

Peliä pelataan kirjoittamalla 5-kirjaiminen englanninkielinen sana ja painamalla enter-näppäintä näppäimistöllä. Tämän jälkeen arvaus ilmestyy ylimpiin ruutuihin. Ruutujen väri ilmoittaa, kuinka lähellä arvaus on.

![arvaukset](https://user-images.githubusercontent.com/101889891/166434437-e56ba5c2-991e-4897-b798-92f7f3f630eb.png)

Jos käyttäjän arvaama sana ei ole sovelluksen hyödyntämässä sanalistassa tai arvattu sana on liian lyhyt, antaa peli virheilmoituksen.

Vihreä ruutu tarkoittaa, että kirjain on voittosanassa täysin samassa paikassa. 
Keltainen ruutu tarkoittaa että kirjain on voittosanassa, mutta väärässä kohdassa. 
Harmaa ruutu tarkoittaa, että kirjain ei ole voittosanassa ollenkaan.

Jos käyttäjä ehtii arvata voittosanan oikein kuudella yrityksellä, voittaa hän pelin. Tämän jälkeen avautuu menu, jossa lukee voittosana. Menusta voi valita uuden pelin "Replay"-painiketta painamalla tai palata takaisin aloitusmenun "Main menu"-painiketta painamalla.

![voittomenu](https://user-images.githubusercontent.com/101889891/166434514-b90e028a-c0a6-4205-a660-08cb968de5cc.png)
![häviömenu](https://user-images.githubusercontent.com/101889891/168469419-eb9c14d7-a085-404d-b8ca-e0dfc74a7c28.png)




