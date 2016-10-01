Title: Sikker forbindelse til nettsider
Slug: https

HTTPS er et todelt sikkerhetssystem for websider som både verifiserer
identiteten til serveren man snakker med og krypterer forbindelsen slik
at trafikken [ikke kan
avlyttes](/trusler/trafikkavlytting/). Når nettleseren
din benytter HTTPS vises et hengelås-symbol i adresselinjen øverst i
nettleseren.

Det eneste som vanligvis "lekker ut" når man bruker HTTPS er
[DNS-forespørslene](/tiltak/dns/), men disse inneholder
kun servernavnet. Det vil si det som kommer først i nettadressen, for
eksempel "www.vg.no". Så en eventuell overvåker vil vite når
kommunikasjonen skjedde, og med hvilken server.

Derfor bør man alltid etterstrebe å bruke HTTPS hvis man kan, og man bør
holde et øye med identiteten til serveren man kobler til, for å avsløre
om noen har omdirigert trafikken til sin egen server.

Som hjelp til å huske dette, kan man installere [HTTPS
Everywhere](https://www.eff.org/https-everywhere), en nettleserutvidelse
som automatisk bruker HTTPS på de fleste store nettsteder som støtter
dette.

Mange nettsteder (for eksempel
[Facebook](http://www.nettvett.no/chat-og-sosiale-medier/facebook/sikkerhetsinnstillinger-på-facebook)) har
også en innstilling et sted som gjør at de alltid vil "flytte deg over"
til HTTPS hvis mulig.
