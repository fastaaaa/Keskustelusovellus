# Astro chat 

Kyseessä on keskustelusovellus, jossa käyttäjät voivat keskustella astrologiaan liittyvistä aiheista. Sovelluksessa on keskustelualueita, joita käyttäjät ja ylläpitäjät voivat luoda, ja joissa he voivat keskustella. Lisäksi sovelluksessa on tietoa ajankohtaisista astrologisista tapahtumista. Käyttäjät ovat joko peruskäyttäjiä tai ylläpitäjiä. Alla listaus sovelluksen keskeisistä ominaisuuksista. 

* Käyttäjä voi kirjautua sisään ja ulos 

* Käyttäjä voi rekisteröityä luomalla uuden käyttäjätunnuksen ja salasanan 

* Käyttäjä näkee sovelluksen etusivulla listan alueista, ja voi siirtyä haluamalleen alueelle klikkaamalla alueen nimeä 

* Keskustelualueella näkyy sinne lähetetyt viestit, niiden lähettäjät sekä viestin lähettämisajankohta 

* Käyttäjä voi luoda uuden alueen etusivulla antamalla alueelle otsikon, jonka jälkeen sovellus pyytää häneltä aloitusviestiä alueelle 

* Käyttäjä voi lukea etusivulta ylläpitäjien päivittämiä astrologian ajankohtaisia uutisia 

* Käyttäjä voi kirjoittaa uuden viestin olemassa olevalle alueelle. 

* Käyttäjä voi poistaa luomansa alueen sekä lähettämänsä viestit. 

* Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana. 

* Käyttäjä voi siirtyä haluamalleen keskustelualueelle hakutuloksista 

* Ylläpitäjä voi ylläpitäjät-sivulta lisätä uusia ylläpitäjiä käyttäjätunnuksen perusteella. 

* Ylläpitäjä voi ylläpitäjät-sivulta lähettää viestin etusivulle "astrologian ajankohtaiset" osioon. Osiossa näkyy aina uusin ylläpitäjän viesti, kuka sen on lähettänyt ja milloin. 

* Ylläpitäjä voi lisätä ja poistaa keskustelualueita. 

* Ylläpitäjä voi poistaa kenen tahansa käyttäjän viestin (esimerkiksi jos viestin sisältö on epäasiallista tai ei liity astrologiaan) 

* Navigointi palkista käyttäjä voi siirtyä aina takaisin etusivulle sekä kirjautua ulos, ja näiden lisäksi ylläpitäjät pääsevät ylläpitäjien sivulle 

 

Tallenna githubista tämän sovelluksen tiedostot omalle koneelle ja nimeä kansio haluamallasi tavalla. 

Sovelluksen testaamiseksi tulee sovelluksen kansioon .env tiedosto ja luoda oma SECRET KEY ja lisätä se .env tiedostoon muodossa 

SECRET_KEY=sinunsalainenavain

Db.py tiedostosta tulee tarkistaa tietokannan osoite, ja tarvittaessa muuttaa sinne tietokantasi paikallinen osoite. Valmiina osoitteena on seuraava 

_app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://"_

Siirry kansioon terminaalissa komennolla 

_cd kansion nimi_ 

Aktivoi ympärisö komennolla 

_source venv/bin/activate_ 

Avaa terminaali uuteen ikkunaan, ja aktivoi postgresql komennolla 

_Start-pg.sh_

Avaa uusi ikkuna ja määritä sovelluksen tietokanta komennolla 

_Psql < schema.sql_

Palaa takaisin ikkunaan, jossa sinulla on sovellus aktivoituna, ja aja komento 

_Flask run_ 

Nyt pääset testaamaan sovellusta! 

 

Jotta voit testata ylläpitäjän oikeuksia, lisää oma käyttäjätunnuksesi admin tauluun.  
