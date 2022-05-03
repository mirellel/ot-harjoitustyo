# Arkkitehtuurikuvaus

## Rakenne
Koodin pakkausrakenne on seuraava
![image](https://user-images.githubusercontent.com/101889891/166429870-c36d6496-f4f1-46c2-a0a3-3d0e338ccc1a.png)

Pakkaus ui sisältää käyttöliittymästä, services sovelluslogiikasta ja repositories tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus entities sisältää luokan User, joka kuvaa sovelluksen käyttämää tietokohdetta user.

## Käyttöliittymä
Käyttöliittymä on jakautunut käyttäjäkäyttöliittymään ja pelikäyttöliittymään

__Käyttäjäkäyttöliittymä__
- sisäänkirjautumisnäkymä
- näkymä uuden käyttäjän luomiseen
- stats -näkymä, josta voi avata pelin ja nähdä tilastonsa

__Pelikäyttöliittymä__
- aloitusmenu
- pelinäkymä
- loppumenu riippuen voitosta

Kirjautuminen, uuden käyttäjän luominen, stats ja pelinäkymä on toteutennu omina luokkinaan. Pelin menut ovat samassa luokassa. Näkymien näyttämisestä vastaa [UI](../src/ui/ui.py) ja [Main](../src/ui/game_ui.py).

## Sovelluslogiikka
Pelin sovelluslogiikasta vastaa [CheckGuess](../src/services/checkguess.py)-luokka, joka vertaa pelaajan arvausta oikeaan sanaan ja palauttaa listan värejä, jotka kertovat oikeat ja väärät kirjaimet arvauksessa
```mermaid
 classDiagram
      CheckGuess
      class CheckGuess{
          word
          userguess
          check()
      }
```
Toiminnallisista kokonaisuuksista vastaa luokka [GameService](../src/services/game_service.py)
Luokka tarjoaa käyttäjäkäyttöliittymän toiminnoille oman metodin. Näitä ovat esimerkiksi:

- `login(username, password)`
- `logout()`
- `create_user(username, password, login=True)`

_GameService_ pääsee käsiksi käyttäjiin [UserRepository](../src/repositories/user_repository)-luokan kautta. _UserRepository_ vastaa tietojen tallennuksesta. 

## Tietojen pysyväistallennus
Pakkauksen _repositories_ luokka `UserRepository` huolehtii tietojen tallentamisesta. Luokka tallentaa tietoa SQLite-tietokantaan. 

## Tiedostot

Käyttäjät tallennetaan SQLite-tietokannan tauluun `users`, joka alustetaan [initialize_database.py](../src/initialize_database.py)-tiedostossa.

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

