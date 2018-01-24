PySynonym: your Python 2.x and 3.x package for finding synonym and definition for keywords.

---------------------------------------------------



PySynonym is a package for Python 2/3 to get synonyms,

definitions of words. 



This package uses Python Requests and BeautifulSoup4 as dependencies



Installation

~~~~~~~~~~~~



Installing PySynonym is very simple using pip



::



    pip install PySynonym
    
    or 
    
    pip3 install PySynonym





Usage

~~~~~



PySynonym currently has two functions: explain and synonym. They 

are used to get defintions and synonyms for your entered keywords. 



A simple example for using the two main functions:



.. code:: python



    import PySynonym as ps

    ps.explain('house')
    ps.synonym('house')






The source is in the source.py file. 



Created By Mats Bauer. Copyright 2018 - but free to use everywhere.

