# Scripting Languages Course

Here, you can find all necessary information about Scripting Languages course.


## Labs

Information about labs is available in a [separate page](exercises_en.md).


## Source Codes

You can find source codes from lectures in the [Jupyter notebooks](notebooks) section.

See also [labs](labs) section for codes for Labs.


## Grading

In the course of the semester, you will be assigned 8 exercises, which you will elaborate independently. Tasks will appear in the [Kelvin](https://kelvin.cs.vsb.cz) system.

You will be also assigned one project.
The assignment will be posted on this page and you will be informed about it.
Your task is to elaborate this task individually and present it to your teacher by the given deadline, who will evaluate the functionality of the solution and also the way the task is programmed.
The project is worth 30 points.
If you do not submit the assignment within the deadline, 3 points will be subtracted from the maximum ammount of points for each commenced week after the due deadline.
The task is mandatory!
You must delived it!
You must earn at least 10 points from this task.

<!-- In the final week will also take the final test, which you must pass. You can earn up to 40 points for this test. You must get at least 15 points. -->


### Final test

The final test will take place in the examination period and you schedule will be announced in [EdISon](https://edison.vsb.cz).


### Summary

<table>
<tr><th>Task type</th><th>MAX points</th><th>MIN points</th><th>Note</th></tr>
<tr><td>Elaboration of tasks</td><td>30 (40)</td><td>10</td><td>Scoring mentioned above.</td></tr>
<tr><td>Submission of the project in Django</td><td>30</td><td>10</td><td></td></tr>
<tr><td>Final test</td><td>40</td><td>15</td></tr>
</table>


## Delivering Tasks

To handout task, use [Kelvin](https://kelvin.cs.vsb.cz) system.


## Books

I recommend [Dive Into Python 3](https://diveintopython3.problemsolving.io/) book for reading.


Text from [MIT 6.01](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/syllabus/MIT6_01SCS11_textbook.pdf) course is also recommend.


## Additional resources

* [Python documentation](http://docs.python.org/index.html)

<!--An interesting online interactive course found at Codeacademy .-->

* For the basics of programming, you can use the [Think Python](http://www.greenteapress.com/thinkpython/) book, which you can download for free.

* You can use the official [Python Tutorial](https://docs.python.org/3/tutorial/) as additional literature.

* A set of [lectures from MIT ](https://www.youtube.com/watch?v=bX3jvD7XFPs&list=PLB2BE3D6CA77BB8F7) that explain the use of Python on various tasks.


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


## Project assignment for full-time students
Deadline for submitting: at seminars in the week from 9.5.2022 to 13.5.2022.

Using the Django framework, program a simple web application that meets the following criteria:

- Your application will contain at least 6 models (team of 2 students) or 3 models (team of 1 student), which will be interrelated.
- Create adequate administrative interfaces for models.
- Your application will contain at least 12 view (team of 2 students) or 6 view (team of 1 student) and the associated URL that will work with the models.
- Your application will pass content to templates (you will implement 12 templates (team of 2 students) or 6 templates (team of 1 student).
- Your application will contain at least 6 forms (team of 2 students) or 3 forms (team of 1 student) (either model-bound or your own).
- Resulting application should form a logical concept, i.e. individual pages will be linked to each other.
- Blogging and forum apps are not allowed as we did them in lectures.
- A gas station project is not acceptable as we did it at the exercises.
- Your application does not have to contain graphic elements and CSS styles.
- Your app doesn't have contain spatial data (GeoDjango).
- Your application must not contain generic views.
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
