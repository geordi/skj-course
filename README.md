# SKJ Course

## Overview

- [Grading](#grading)
- [Books](#books)
- [Exercises](#exercises)
- [Project for full time students](#project-assignment-for-full-time-students)


## Labs

See [labs](labs) section for some scripts.


## Jupiter notebooks

You can find some codes of first few lessons in [notebooks](notebooks) section.

For course notes, see [spja-skripta repo](http://github.com/geordi/spja-skripta) (in Czech language)


## Grading

In the course of the semester, you will be assigned 8 exercises, which you will elaborate independently under the supervision of the instructor in the given exercise. Of course, you will be able to ask the teacher if you need any help.
These tasks will cover topics discussed in lectures.
For each exercise you will also have a short text explaining the issue.
You will be able to earn up to 5 points for each exercise.
The total score will be calculated from the 6 best results you will achieve in the exercises (maximum 30 points).
This is set so, because you may be ill and therefore you will not be able to attend the exercise, etc.

You will be also assigned one homework.
The assignment will be posted on this page and you will be informed about it in lectures and exercises.
Your task is to elaborate this task individually or in pairs and present it to your teacher by the given deadline, who will evaluate the functionality of the solution and also the way the task is programmed.
The task is worth 30 points.
If you do not submit the assignment within the deadline, 3 points will be subtracted from the maximum ammount of points for each commenced week after the due deadline.
The task is mandatory!
You must delived it!
You must earn at least 10 points from this task.

<!-- In the final week will also take the final test, which you must pass. You can earn up to 40 points for this test. You must get at least 15 points. -->


### Final test

The final test will take place in the credit week and you will be informed about it in advance on the lecture and this website.
The term is NOT listed in Edison.


### Summary

<table>
<tr><th>Task type</th><th>MAX points</th><th>MIN points</th><th>Note</th></tr>
<tr><td>Elaboration of tasks at seminars</td><td>30 (40)</td><td>6</td><td>Scoring mentioned above.</td></tr>
<tr><td>Submission of the project in Django</td><td>30</td><td>10</td><td>Can be worked out in pairs.</td></tr>
<tr><td>Final test</td><td>40</td><td>15</td></tr>
</table>


## Books

I recommend [Dive Into Python 3](https://diveintopython3.problemsolving.io/) book for reading.
Important chapters are:
1. Your First Python Program
2. Native Datatypes
3. Comprehensions
4. Strings
<!--Regular Expressions-->
6. Closures & Generators
7. Classes & Iterators
8. Advanced Iterators
<!--9. Unit Testing-->
<!--10. Refactoring-->
11. Files
12. XML
<!--13. Serializing Python Objects-->
14. HTTP Web Services
<!--Case Study: Porting chardet to Python 3
Packaging Python Libraries
Porting Code to Python 3 with 2to3
Special Method Names
Where to Go From Here-->
D. Troubleshooting


## Additional resources

* [Python documentation](http://docs.python.org/index.html)

<!--An interesting online interactive course found at Codeacademy .-->

* For the basics of programming, you can use the [Think Python](http://www.greenteapress.com/thinkpython/) book, which you can download for free.

Also read the [MIT's course notes](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/Syllabus/MIT6_01SCS11_notes.pdf) , which I highly recommend.

* You can use the official [Python Tutorial](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/Syllabus/MIT6_01SCS11_notes.pdf) as additional literature.

* A set of [lectures from MIT ](https://www.youtube.com/watch?v=ewd7Lf2dr5Q&list=PL2C8C1F1B1FD608C0) that explain the use of Python on various tasks.


## Django

Part of our tutorials focus on developing web applications using the [Django framework](http://www.djangoproject.com/).
<!--There are also Czech pages where you can find documentation for version 1.0 in Czech.-->
For those interested in using Django, I recommend [The Django Book](https://djangobook.com/).

<!--Nice series about Djang was published on Zdroják server.-->

<!--
Project for full-time students
The assignment of the project for full-time students is given as task 5 (full-time) .

Combined Studies
For students of the combined form of study, 4 tasks will be prepared. The deadline for submitting individual tasks (they will gradually appear on this page) is ideally within the credit week. However, it is no problem to submit the tasks and complete the test at a later date (ideally by the 2nd week of the examination period).

Assign tasks to the tutor's e-mail, where the subject will be: SPJA-KOMB-PROJ-X-login , where X is the task number and login is your student number. Your solutions will be continuously reviewed and scored. Of course, discussions on the solutions will be on tutorials.

Evaluation
Task type	MAX points	MIN points	Note
Submitting a set of 4 tasks	60	25	All assignments must be submitted!
Test	40	15 Dec	
Dates of tests
Below are terms of credit tests for the combined form of study. The test can be repeated. So you can come to more dates if you test. Everything will take place in the EB405 classroom.

Date	Time
6. 1. 2017	14:00
9. 1. 2017	14:00
11. 1. 2017	14:00
13. 1. 2017	14:00
20. 1. 2017	14:00
-->

## Exercises

### Exercise 1

The script to which you can gradually add the code is available here: [ex_01.py](labs/ex_01.py). The solution is available in: [ex_01_solution.py](labs/ex_01_solution.py).

We will discuss the following topics in the exercise:
* Dynamic typing
* Garbage collector

* Working environment:
  * ipython
  * Magic command,% hist

* Basic data types:
  * numbers (int, long, float, complex)
  * string:
    * immutable
    * literal for long string
    * encoding (prefix u)
* list, tuple
* dict

* Singletons: `None`, `True`, `False`

* Syntax basics:
  * Comments (+ docstring)
  * Assignment to a variable
  * Calling functions
  * print (basic `{}` substitution)
  * Conditions (possibility to bypass the absence of the switch)
  * Cycles:
    * for
    * while
  * Function definition

Recommended for practice:

A script from the 2011/2012 academic year that also includes recursion: [ex_01_extended.py](labs/ex_01_extendedn.py).

<!--Solution: cv1_labs_extended_full.py-->

### Exercise 2

Scoring exercises on the topics discussed in the first lecture + the content of the first exercise where simple function calls were used.

<!--The study material is the text stated at the beginning of the page.-->

### Exercise 3

Scoring exercises on the topics discussed in the second lecture: Function, list comprehension, functional elements of programming, reading from a file.

<!--The study material is the text stated at the beginning of the page. Exceptions and file readings are explained in the presentation .-->


### Exercise 4

Scoring exercises on the topics discussed in the 3rd lecture: Object-oriented programming.

<!--
The study material is the text stated at the beginning of the page.
Slides to imports and packages .
Slides to object-oriented programming .
-->

### Exercise 5

Scoring exercises on topics discussed in third and fourth lecture: Object-oriented programming.

<!--
The study material is the text stated at the beginning of the page.
Slides to object-oriented programming .
-->


### Exercise 6

Scoring exercises on topics discussed at 3.-5. lecture: Object-oriented programming.

<!--
The study material is the text stated at the beginning of the page.
Slides to object-oriented programming .
-->


### Exercise 7

Scoring exercises on topics discussed in the 6th lecture: XML

Slides to process XML .

Example of [parsing XML](labs/ex_06_xml_examples.py) file [canteen.xml](notebooks/canteen.xml).

There is also a [newer version of parsing](notebooks/lecture_05_parsing_xml.ipynb) using the ElementTree library and [converting an xml file to Python objects](notebooks/lecture_05_xml_to_object.ipynb).

<!--
Example of searching on Twitter (not running since 2013).
-->


### Exercise 8

Scoring exercises on topics discussed in the 8th lecture: XML-RPC

The study material is the text stated at the beginning of the page.

XML-RPC examples:
- [calc_client.py](calc_client.py)
- [calc_service.py](calc_service.py)
- [calc_service2.py](calc_service2.py)


### Exercise 9

Exercise on topics from all previous exercises.


## Project assignment for full-time students
Deadline for submitting: at seminars in the week from 16.12.2019 to 20.12.2019

Using the Django framework, program a simple web application that meets the following criteria:

- the application will contain at least 6 models (team of 2 students) or 3 models (team of 1 student), which will be interrelated
- create adequate administrative interfaces for the models
- the application will contain at least 12 view (team of 2 students) or 6 view (team of 1 student) and the associated URL that will work with the models
- view Your application will pass content to templates (you will implement 12 templates (team of 2 students) or 6 templates (team of 1 student)
- the application will contain at least 6 forms (team of 2 students) or 3 forms (team of 1 student) (either model-bound or your own)
- the resulting application should form some logical whole, ie the individual pages will be linked to each other using links
- blogging and forum apps are not allowed as we did them in the lecture
- a gas station project is not acceptable as we did it at the exercises
- the application does not have to contain graphic elements and CSS styles
- the app may not have a geographic folder
- the application must not contain a generic view
- The application can be eg your very simple implementation of Twitter service, part of the school information system (granting credit to students), some part of the blue page (Facebook), etc.

<!--
## Distance Students Tasks

### Task 1

Implement the `dot_product` and `cross_product` functions to return the scalar and vector product of the vectors. As input, consider 2D and 3D vectors, which will be represented by a sheet (in the case of a vector product, consider only 3D vectors). Be sure to treat when the vectors are not 2D or 3D, and when the functions get vectors of different lengths. In this case, the function returns None .

Input function: two sheets representing vectors (suppose 2D and 3D vectors)
Function output: number (for dot_product ) or list (for cross_product )

Sample:

`dot_product ([1,2,2], [0,1,2])`
Output: `2`

`cross_product ([1,2,2], [0,1,2])`
Output: `[4, -2, 1]`

Example of incorrect entry (not all combinations listed):

`cross_product ([1, 2, 0], [0, 1, 2, 4])`
Output: `None`


### Task 2

Program `make_index` and `search_by_index`

Description of function `make_index`:
Creates an index of words from the input file with information on which lines are words.
The index is saved to a file.
A space separator is a space, period, comma, semicolon, question mark, exclamation mark, and quotation marks.

Index format:
`<word> <line1> <line2> ... <lineN>`

Each word is on a separate line.

Example:
```
first-rate
flexible 18
for 12 13 20 25 27 29
```

The register shall be sorted lexicographically. Line numbers are sorted and not repeated.

Input: The name of the input file and the name of the file in which the index will be stored
Output: None

Description of function `search_by_index`:
Uses the created index and returns the line numbers that contain the word.

Input: The name of the index file and the search word
Output: Integer list

Example:
```
make_index ("input.txt", "index.txt")
search_by_index ("index.txt", "Python")
```
Output: `[1, 3, 16, 18, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36, 37, 39, 41, 42, 44, 46]`

`search_by_index ("index.txt", "Kreatrix")`
Output: `[]`

Test data:
The test input file is available here.
A test index file is also available.
If you're using Windows, be careful not to break the line that is in this Unix-style file, or encode the input file.

Further specification specifications
All exceptions must be handled in the program.
To work with sheets, use the "list comprehension" that we used a lot in exercises. Do not use map and reduce functions.
To parse an input file and hyphenate delimiters, first edit the input file using the `string.translate` function (link to the documentation),
then separate the lines with a single delimiter.
This will eliminate the browsing of each character on the line.
An index file reverse lookup will be effective;
you won't create a new dictionary.
You just browse the file and return the result for that word.
The same rules as above apply to work with the sheet.
Use slicing where possible.


Task 3 (combined)
Program the Inventar and Item classes.

Description of the "Item" class:
The class represents a physical item owned by VŠB. Its attributes and methods are listed below:

The item id is always a string in the form <fakulta> / number , where <fakulta> is one of the following abbreviations: FEI, HGF, EkF, FBI, FMMI, FS, FAST.

Amortization method amortizes the item according to the given amortization coefficient. When you create an object, the original price and the residual price are set to the same value. For amortization, the residual cost will be reduced. The formula for calculating the residual price is as follows:
residual_price = residual_price - original_price * co-amortization

The __str__ method will return a string in the following form: Type: <type>, ID: <id>, Room: <room> , where the values ​​between the arrows will be the current values ​​of the item. The method is called, for example, when using print . An example is given below.

Its attributes and methods are listed below:

Class Item:

attributes:
id
name
room
original price
residue_price
coef_amortization
methods:
__init __ (self, id, name, room, price, coefficient)
amortization (self)
__str __
Description of the "Inventar" class:
The class represents the database of VŠB property. Simple adding, browsing the number of items and browsing the total price of assets can be performed over this database.

Implement the database containing the assets as a dictionary where the key is the item id.

The item_price method returns the residual price of all items that belong to the faculty.

The count_items method returns the number of items belonging to the faculty.

The amortization method amortizes the items belonging to the faculty.

The class attributes and methods are listed below:

Inventar Class:

attributes:
inventar (dictionary)
methods:
__init __
add (self, property)
count_items (self, faculty)
price_item (self, faculty)
amortization (self, faculty)
Example:
inventory = Inventory ()
inventory add (Item ("FEI / 4605511", "Chair", "A1036", 1600, 0.05))
inventory add (Item ("FEI / 4605512", "Stul", "A1036", 2360, 0.05))
print inventory.inventar ["FEI / 4605511"]
print inventory.price_item ("FEI")
amortization inventory ("FEI")
print inventory.price_item ("FEI")
print inventory.price_item ("HGF")

Exit:
Type: Chair, ID: FEI / 4605511, Room: A1036
3960
3762.0
0

Task 4 (combined)
Due date: in the week of 17.12.2012 to 20.12.2012

Create a simple XML-RPC service that works with a property inventory that is very similar to the previous assignment. However, the declarations of some methods are different.

Program the Inventar and Item classes.

Description of the "Item" class:
The class represents a physical item owned by VŠB. Its attributes and methods are listed below:

The item id is always a string in the form <fakulta> / number where <fakulta> is one of the following abbreviations: FEI, HGF, EkF, FBI, FMMI, FS, FAST

Amortization method amortizes the item according to the given amortization coefficient. When you create an object, the original price and the residual price are set to the same value. For amortization, the residual cost will be reduced. The formula for calculating the residual price is as follows:
residual_price = residual_price - original_price * co-amortization

The __str__ method will return a string in the following form: Name: <name>, ID: <id>, Room: <room> , where the values ​​between the arrows will be the current values ​​of the item. The method is called, for example, when using print .

The vrat_xml_element method returns an item as an XML element from the Python ElementTree module. Use this method when saving a database. Start with a sample representation of one item in your inventory, which you can download below.

Attributes and methods of the Item class:

attributes:
id
name
room
original price
residue_price
coef_amortization
methods:
__init __ (self, id, name, room, original_price, residual_price, amortization)
amortization (self)
return_xml_element (self)
__str __
Of course, you can add additional attributes or methods to make your work easier.

Description of the "Inventar" class:
The class represents the VŠB property database and is also an XML-RPC service for remote access to this database. Above this database it is possible to perform simple operations of adding, browsing the number of items, browsing the total price of assets, carrying out amortization of assets and permanently saving this database to an XML file. This ensures that if the service is stopped and then started, you will still have items that you added while the service was running.

The database will be saved to an XML data file whose name will be passed as an argument to the Inventar class constructor. You can represent the database in memory as last time using a dictionary. However, this is not a requirement, so this attribute is not mentioned in the list below.

Note that only the following methods can be called from the client: add , item_path , number_of_items , make_amortization .

The import_xml_db method retrieves the file passed to the constructor. Loads the database from the XML data into memory for further work using methods from the Python ElementTree module.

The save_xml_db method saves assets from memory to an XML file using methods from the Python ElementTree module.

The add method adds the entry to the database. When you call this method on a client with an argument that is an instance of the Item class, that instance is passed as a dictionary. This is the standard behavior of XML-RPC. It is therefore necessary to recreate an object of the Item type from this dictionary.

The item_price method returns the residual price of all items that belong to the faculty.

The count_items method returns the number of items belonging to the faculty.

The amortization method amortizes the items belonging to the faculty.

Attributes and methods of the Inventar class:

attributes:
xml_db_file
methods:
__init __ (self, xml_db)
import_xml_db
uloz_xml_db
add (self, item)
count_items (self, faculty)
price_item (self, faculty)
amortization (self, faculty)
Think carefully when it is necessary to store the database in memory into XML, because you do not have to call the save method from the client and you are not sure whether the service will still be accessible.

The initial database that can be used as a constructor argument is available here: inventar.xml . Also, review the structure of the XML document to correctly create an XML representation of the Item class and the entire database for future execution.

Also, remember that methods called via XML-RPC must return something. So if you do not expect any return value on the client side, simply return integer 0.

Test your service properly using ideally two clients according to the following instructions. You can use the following sequence of steps to test the permanent storage of items in an XML file:

start the service
run client with browsing, adding items and amortization
turn the service off and then on
the browsing service should already be reflected here, the amortized cost of the items should already be reflected here
Use the following Python modules for implementation: xml.etree.ElementTree and SimpleXMLRPCServer (or other standard modules).

Use the ElementTree module help to work with XML.
-->
