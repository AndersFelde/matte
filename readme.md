Sette trekant i 2 dimensjonelt med punkt
    finne retningsvektor til planet med opprinnelig trekant (alfa)
    finne avstand fra punkt til plan alfa
    kopiere trekant ved å flytte punktene avstand lengde i retningsvektor retning
        Må også sjekke at det flyttes riktig vei (sjekke om punkt ligger i plan)

sjekke om punkt ligger innenfor trekant
    trekke horisontal linje (i alle retninger) og se om de krysser linjene i figur fler enn 1 gang eller 0
        kan være 1 gang hvis horisontal linje treffer perfekt på et hjørne, må sjekke det også
        
hvis ja: avstand mellom plan = avstand til trekant
hvis nei:
Finne nærmeste linje i forhold til punktet (fortsetter på 2d)
    Trekke sirkel med sentrum i punktet
    Finne punkt hvor sirkel tangerer med linje i kun ett punkt (gjør det for hver linje i trekant)
Sjekke om punkt ligger innenfor linjestykket
    Sjekk om AP er paralell med AB og hvilket fortegn t vil få
    T = negativ
        Sjekk om lengden AB >= lengden BP
    T = positivt
        sjekk om lengden AB >= lengden AP
Ligger punktet innenfor linjestykket så er korteste vei lengden fra P til punktet
Ligger punktet utenfor linjestykket så vil korteste vei være fra en av hjørnene til punktet
    Sammenlign og finn det korteste
Når du har korteste vei til alle linjene må du sammenligne og velge den korteste av de
For å da finne avstanden i 3d kan man ta hypotenus i trekant hvor katetene er avstand til linje og avstand mellom plan