# Cvičení

Pro editaci zdrojového kódu doporučuji [VisualStudio Code](https://code.visualstudio.com/) s nainstalovaným rozšířením [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python). Pokud chcete používat jiný editor, tak můžete využít, např. [PyCharm](https://www.jetbrains.com/pycharm/), kde můžete získat plnou verzi jako studenti (BTW: IntelliJ IDEA má pěkný [Rust plugin](https://plugins.jetbrains.com/plugin/8182-rust), do kterého příspívá i jeden ze cvičících tohoto předmětu a to [Jakub Beránek](https://github.com/Kobzol)), [Doom Emacs](https://github.com/hlissner/doom-emacs), [SpaceVim](https://spacevim.org/), aj.

Osobně jsem si vždy vystačil s obyčejným textovým editorem, příkazovou řádkou [iPython](https://ipython.org/) a [Jupyter Notebooky](https://jupyter.org/) (v předmětu je k dispozici i [pár vlastních noteboků](notebooks)).


## Cvičení 1

Skript, do kterého můžete postupně doplňovat kód, je k dispozici zde: [ex_01.py](labs/ex_01.py). (řešení: [ex_01_solution.py](labs/ex_01_solution.py)).

Na cvičení budeme probírat níže uvedená témata:
* Dynamická typovost
* Garbage collector

*Pracovní prostředí:
  * ipython
  * Magic command `%run`, `%hist`

* Základní datové typy:
  * čísla (`int`, `long`, `float`, `complex`)
  * `string`:
    * immutable
    * literal pro long string
    * kódováni, encoding (bytes)
* `list`, `tuple`
* `dict`

* Singletony: `None`, `True`, `False`

* Základy syntaxe:
  * Komentáře (+ docstring)
  * Přiřazení do proměnné
  * Volání funkcí
  * funkce `print` (základní `{}` substituce)
  * Podmínky (možnost obejití absence switche)
  * Cykly:
    * `for`
    * `while`
  * Definice funkce

Doporučeno k procvičení:

Skript z akademického roku 2011/2012, který navíc obsahuje rekurzi: [ex_01_extended.py](labs/ex_01_extendedn.py) (řešení: [cv1_labs_extended_full.py](cv1_labs_extended_full.py)).

<!--Solution: cv1_labs_extended_full.py-->

## Cvičení 2

Procvičíme si kolekce a práci s nimi.

Skript, do kterého můžete postupně doplňovat kód, je k dispozici zde: [ex_02.py](labs/ex_02.py).<!--(řešení: [ex_02_solution.py](labs/ex_02_solution.py)).-->

<!--
Scoring exercises on the topics discussed in the first lecture + the content of the first exercise where simple function calls were used.
-->

<!--The study material is the text stated at the beginning of the page.-->

<!--
## Exercise 3

Scoring exercises on the topics discussed in the second lecture: Function, list comprehension, functional elements of programming, reading from a file.

-->
<!--The study material is the text stated at the beginning of the page. Exceptions and file readings are explained in the presentation .-->

<!--
## Exercise 4

Scoring exercises on the topics discussed in the 3rd lecture: Object-oriented programming.
-->

<!--
The study material is the text stated at the beginning of the page.
Slides to imports and packages .
Slides to object-oriented programming .
-->

<!--
## Exercise 5

Scoring exercises on topics discussed in third and fourth lecture: Object-oriented programming.
-->

<!--
The study material is the text stated at the beginning of the page.
Slides to object-oriented programming .
-->

<!--
## Exercise 6

Scoring exercises on topics discussed at 3.-5. lecture: Object-oriented programming.
-->

<!--
The study material is the text stated at the beginning of the page.
Slides to object-oriented programming .
-->

<!--
## Exercise 7

Scoring exercises on topics discussed in the 6th lecture: XML

Slides to process XML .

Example of [parsing XML](labs/ex_06_xml_examples.py) file [canteen.xml](notebooks/canteen.xml).

There is also a [newer version of parsing](notebooks/lecture_05_parsing_xml.ipynb) using the ElementTree library and [converting an xml file to Python objects](notebooks/lecture_05_xml_to_object.ipynb).
-->
<!--
Example of searching on Twitter (not running since 2013).
-->

<!--
## Exercise 8

Scoring exercises on topics discussed in the 8th lecture: XML-RPC

The study material is the text stated at the beginning of the page.

XML-RPC examples:
- [calc_client.py](calc_client.py)
- [calc_service.py](calc_service.py)
- [calc_service2.py](calc_service2.py)


## Exercise 9

Exercise on topics from all previous exercises.


-->

## Cvičení 14

Odevzdávání projektů.
