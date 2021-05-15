# VSTUP Project
## WEB-helper for abiturients during entering session
***
### Description
#### This project includes
* calculating probability of entering the university
* creating recommendations for appllicants
* convenient user interface

#### The visualisation provided
* number of applicants in previous year
* licenesed amount
* average rating score in previous year
* price of the studying year
* abiturient's probability of entering the university
***
### Aim and usage
* This project's aim is to make the process of university entering easier and more controlled. Abiturient can see the chance of his admission and in this way he'll be able to decide what in what subject he have to improve, etc.

* To launch and run web application, run module start.py.
* When web app launches, in requests information from CSV files.
***
### Contents
#### [chance_flask](https://github.com/Tsalyk/vstup_project/tree/main/chance_flask)
* [arrays.py](https://github.com/Tsalyk/vstup_project/blob/main/chance_flask/arrays.py) - contains ADT implementation
* [main.py](https://github.com/Tsalyk/vstup_project/blob/main/chance_flask/main.py) - the main module of the program, where HTML script connects with database analysis functions.
* [tools.py](https://github.com/Tsalyk/vstup_project/blob/main/chance_flask/tools.py) - contains all tools needed for web application.
#### [examples](https://github.com/Tsalyk/vstup_project/tree/main/examples)
* [adt_example.py](https://github.com/Tsalyk/vstup_project/blob/main/examples/adt_example.py) - example of ADT usage
* [arrays.py](https://github.com/Tsalyk/vstup_project/blob/main/examples/arrays.py) - contains ADT implementation
* [bsoup_example.py](https://github.com/Tsalyk/vstup_project/blob/main/examples/bsoup_example.py) - example of dealing with Beautiful Soup
* [flask_example.py](https://github.com/Tsalyk/vstup_project/blob/main/examples/flask_example.py) - example of dealing with Flask
* [pandas_example.py](https://github.com/Tsalyk/vstup_project/blob/main/examples/pandas_example.py) - example of dealing with Pandas
* [request_example.py](https://github.com/Tsalyk/vstup_project/blob/main/examples/request_example.py) - example of dealing with requests
* [sheets.py](https://github.com/Tsalyk/vstup_project/blob/main/examples/sheets.py) - example of usage of Google spreadsheets API
***
### Wiki contents
* [Homework #1 report](https://github.com/Tsalyk/vstup_project/wiki/1.-%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B8-%D0%B2%D0%B8%D0%BA%D0%BE%D0%BD%D0%B0%D0%BD%D0%BD%D1%8F-%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8C%D0%BE%D0%B3%D0%BE-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%961)
* [Homework #2 report](https://github.com/Tsalyk/vstup_project/wiki/2.-%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B8-%D0%B2%D0%B8%D0%BA%D0%BE%D0%BD%D0%B0%D0%BD%D0%BD%D1%8F-%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8C%D0%BE%D0%B3%D0%BE-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%962)
* [Homework #3 report](https://github.com/Tsalyk/vstup_project/wiki/3.-%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B8-%D0%B2%D0%B8%D0%BA%D0%BE%D0%BD%D0%B0%D0%BD%D0%BD%D1%8F-%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8C%D0%BE%D0%B3%D0%BE-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%963)
* [Homework #4 report](https://github.com/Tsalyk/vstup_project/wiki/4.-%D0%A0%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D0%B8-%D0%B2%D0%B8%D0%BA%D0%BE%D0%BD%D0%B0%D0%BD%D0%BD%D1%8F-%D0%B4%D0%BE%D0%BC%D0%B0%D1%88%D0%BD%D1%8C%D0%BE%D0%B3%D0%BE-%D0%B7%D0%B0%D0%B2%D0%B4%D0%B0%D0%BD%D0%BD%D1%8F-%E2%84%964)
* [Homework #5 report]
***
### Web application
After opening web application, you can see a start web-page. There're examples of how does page look.


![1](https://user-images.githubusercontent.com/74105219/118358297-d5137780-b586-11eb-97f2-adfa68619f38.jpg)




After pressing "Calculate" button, you will be able to input your test results and choose the university and specialty:


![2](https://user-images.githubusercontent.com/74105219/118358382-32a7c400-b587-11eb-9879-04469ecaf47b.jpg)




Then if you press button "Search" and scroll down, you will see some info about chosen university and specialty, your rating score and probability of your entering. Here is the example:


![4](https://user-images.githubusercontent.com/74105219/118358478-a1851d00-b587-11eb-8805-9fbd21ddd973.jpg)

***
### Preinstallations
* <code>pip install Flask</code>
***
### Credits
* Taras Onyshkiv, UCU(Ukrainian Catholic University)
* Mykhailo-Markiian Tsalyk, UCU(Ukrainian Catholic University)
* Severyn-Dmytro Peleshko, UCU(Ukrainian Catholic University)
* Tymofii Kozak, UCU(Ukrainian Catholic University)
* Oksana Sadova, UCU(Ukrainian Catholic University)
