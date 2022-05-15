# Testausdokumentti
Ohjelmaa on testattu yksikkö- ja integraatiotestein automatisoiduilla unittestilla.

## Yksikkö- ja integraatiotestaus


### Sovelluslogiikka
Sovelluslogiikasta vastaavaa 'GameService'-luokkaa testataan [TestGameService](../src/tests/game_service_test.py)-testiluokalla. Testausta varten on käytössä luokka 'FakeUserRepository'.

Pelin sovelluslogiikasta vastaavaa 'CheckGuess'-luokkaa testataan [TestCheck](../src/tests/game_test)-testiluokalla.

### Repositorio
Repositorio-luokkaa 'UserRepository' on testataan [TestUserRepository](..src/tests/test_users.py)-luokalla.

### Testikattavuus
Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 90%. 

![image](https://user-images.githubusercontent.com/101889891/168440715-f02f3bd9-aa82-4eaf-b5e8-788047aea6ca.png)

Testaamatta jäivät _build.py_- ja _initialize\_database.py_-tiedostojen suorittaminen komentoriviltä.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus 

Sovellus on haettu ja sitä on testattu sekä Linux- että Windows-ympäristössä.
