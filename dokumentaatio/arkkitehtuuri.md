# Arkkitehtuurikuvaus

## Rakenne
Koodin pakkausrakenne on seuraava

![pakkausrakenne](https://user-images.githubusercontent.com/101889891/166236085-c469b263-8045-4967-b0bf-be8c0852199d.png)

Pakkaus ui sisältää käyttöliittymästä, services sovelluslogiikasta ja repositories tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus entities sisältää luokan User, joka kuvaa sovelluksen käyttämää tietokohdetta user.

## Käyttöliittymä
Käyttöliittymä sisältää kuusi erillistä näkymää
- Kirjautuminen
- Uuden käyttäjän luominen
- Stats, mistä voi kirjautua ulos ja aloittaa pelin
- Pelin aloitusmenu
- Pelinäkymä
- Loppumenu riippuen voitosta

Kirjautuminen, uuden käyttäjän luominen, stats ja pelinäkymä on toteutennu omina luokkinaan. Pelin menut ovat samassa luokassa. Näkymien näyttämisestä vastaa [UI](../src/ui/ui.py) ja [Main](../src/ui/game_ui.py).


## Päätoiminnallisuudet
Kuvataan sovelluksen toimintalogiikkaa muutaman päätoiminnallisuuden osalta sekvenssikaavioina

### Sisäänkirjautuminen
Kun kirjautumisnäkymän syötekenttiin kirjoitetetataan käyttäjätunnus ja salasana, jonka jälkeen klikataan _Login_-nappia, etenee sovelluksen kontrolli seuraavasti:
```mermaid
sequenceDiagram
  actor User
  participant UI
  participant GameService
  participant UserRepository
  User->>UI: click "Login" button
  UI->>GameService: login("mirelle", "salasana1")
  GameService->>UserRepository: find_by_username("mirelle")
  UserRepository-->>GameService: user
  GameService-->>UI: user
  UI->>UI: show_stats_view()
```
### Pelin pelaaminen
Käyttäjän kirjaudutta sisään ja painettuaan _Play_-nappia, etenee sovelluksen kontrolli seuraavasti
```mermaid
sequenceDiagram
  actor User
  participant Main
  participant MainRun
  participant CheckGuess
  User->>Main: click "start game" button
  Main->>MainRun: guess("guide")
  MainRun->>CheckGuess: check("guide", "guide")
  CheckGuess-->>MainRun:[green, green, green, green, green]
  MainRun-->>Main: win = True
  Main-->>Main: win_menu()
```

