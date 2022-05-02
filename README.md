# Word.py
Sovelluksessa käyttäjä voi pelata Wordle-kaltaista sanaarvauspeliä (suomeksi Sanuli). Sovellus ja peli ovat englanninkielisiä. Sovellukseen on mahdollista rekisteröityä käyttäjänä, jolloin peliä voi pelata ja pelaaja voi nähdä omat pelitilastonsa.



### Dokumentaatio
[Vaatimusmäärittely](https://github.com/mirellel/ot-harjoitysty-/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/mirellel/ot-harjoitysty-/blob/main/dokumentaatio/tyoaikakirjanpito.md)

[Changelog](https://github.com/mirellel/ot-harjoitysty-/blob/main/dokumentaatio/changelog)

[Käyttöohje](https://github.com/mirellel/ot-harjoitysty-/blob/main/dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

[Testaus](https://github.com/mirellel/ot-harjoitysty-/blob/main/dokumentaatio/testaus.md)

[Arkkitehtuurikuvaus](https://github.com/mirellel/ot-harjoitysty-/blob/main/dokumentaatio/arkkitehtuuri.md)

### Asennus
1. Riippuvuudet tulee asentaa komennolla:
```bash
poetry install
```
2. Vaadittavat alustustoimenpiteet suoritetaan komennolla
```bash
poetry run invoke build
```
3. Sovellus käynnistetään komennolla
```bash
poetry run invoke start
```
### Ohjelman suorittaminen
Ohjelman voi suorittaa komennolla:
```bash
poetry run invoke start
```
### Testaus
Testit voi suorittaa komennolla:
```bash
poetry run invoke test
```
### Testikattavuus
Testikattavuusraportin voi generoida komennolla:
```bash
poetry run invoke coverage-report
```
Raportti löytyy _htmlcov_-hakemistosta painamalla index.html-tiedostoa.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
