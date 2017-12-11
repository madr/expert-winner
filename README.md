Advent of Code 2017
===================

Lösningar för #aoc2017 i Python 3 (testat mot 3.5.2).


Logg
----

 * Särskilt svåra dagar (tidsåtgång mer än 60 min) vid kodtillfället: dag 3, 6 och 7.
 * Dag 3: del 2 kopierades från en [färdig sekvens](https://oeis.org/A141481). Restpunkt är att faktiskt
   implementera den.
 * Dag 11: Allt som behövs finns beskrivet på
   [Hexagonal Grids from Red Blob Games](https://www.redblobgames.com/grids/hexagons/).


Hjälpscript
-----------

För att köra alla lösningar:

    python aoc.py
    

För att starta nya dag (skapar filerna `inputs/<dagnummer>.txt`, `solutions/day_<dagnummer>.py` och
`tests/day_<dagnummer>_tests.py`):

    python aoc.py <dagnummer> "<namn på dag>"


För att köra separat lösning (ersätt `XX` med dagens nummer):

    PYTHONPATH=$(pwd) python solutions/day_XX.py

    
Starta automatisk testkörare (ersätt `XX` med dagens nummer):

    export PYTHONPATH=$(pwd)
    ls solutions/**/*.py | entr -c -r python tests/day_XX_tests.py
