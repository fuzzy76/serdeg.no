Title: Navnetjener (DNS)
Slug: dns
Summary: Skifte til en DNS-server utenfor myndighetenes kontroll.

Når maskinen din skal hente data fra en server gjøres tilkoblingen mot
serverens IP-adresse. For at vi mennesker skal slippe å måtte gå rundt
og huske IP-adresser, har man innført noe som heter DNS. Det gjør man
kan bruke et servernavn istedenfor IP-adresse, et eksempel kan være
"www.vg.no". Da vil maskinen din først kontakte en DNS-server for å be
om rett IP-adresse for hostnavnet. Først da kan maskinen din kontakte
serveren. Vanligvis brukes DNS-serveren til internettleverandøren din.

Svakheten med dette systemet er at de som driver DNS-serveren både kan
blokkere sider ved å returnere feil IP-adresse til deg, og de kan spore
hvilke sider du besøker basert på hvilke hostnavn maskinen din slår opp.

Den enkleste måten å unngå blokkering (og sporing) på er å bytte til en
DNS-server som ikke er omfattet av norsk lovgivning.

De vanligste alternativene er:

-   [Piratpartiets DNS](https://www.piratpartiet.no/dns/) (med detaljert
    bruksanvisning på norsk)
-   [OpenDNS](https://use.opendns.com)
-   [Google Public
    DNS](https://developers.google.com/speed/public-dns/docs/using)

 
