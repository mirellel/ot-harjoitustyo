# Testausdokumentti
Ohjelmaa on testattu automatisoiduilla unittestilla. 


### Sovelluslogiikka
Sovelluslogiikasta vastaavaa 'GameService'-luokkaa testataan [testGameService](../src/tests/game_service_test.py)-testiluokalla. 'GameService'-olio alustetaan niin, että sille injektoidaan riippuvuuksiksi repositorio-oliot, jotka tallentavat tietoa muistiin pysyväistallennuksen sijaan. Tätä varten on käytössä luokka 'FakeUserRepository'

Pelin sovelluslogiikasta vastaavaa 'CheckGuess'-luokkaa testataan [TestCheck](../src/tests/game_test)-testiluokalla.

### Repositorio
Repositorio-luokkaa 'UserRepository' on testataan [TestUserRepository](..src/tests/test_users.py)-luokalla.

### Testikattavuus
Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 90%. 

![image](https://user-images.githubusercontent.com/101889891/168440715-f02f3bd9-aa82-4eaf-b5e8-788047aea6ca.png)

Testaamatta jäivät _build.py_- ja _initialize\_database.py_-tiedostojen suorittaminen komentoriviltä. Nämä olisi myös voinut jättää testikattavuuden ulkopuolelle.
