## How to find the data - Web Scraping

The INFN FiloBlu project was developed by the collaboration between the Physics Department of the University of Bologna and the INFN group of the Sapienza University of Rome.
The project aims to implement a NLP pipeline to process messages with medical theme.
The critical issue of this project was about the message language: the project was financed by the Lazio region and it was developed to work at the Sant'Andrea Hospital of Rome so the project involves only Italian words.
This constrain drastically affects the data availability which are very hard to find on-line.
We tried to overcome this issue with a synthetic generator of phrases.
To this purpose, a large set of medical words have to be provided and a valid interactions between symptoms and diseases can be useful to create reasonable phrases.
The development of the NLP pipeline goes out from the scopes of this thesis (see Appendix E for further informations about our contributions about this task) but our first contribution to the INFN FiloBlu project concerned the realization of an Italian disease ontology: if we have a sufficient disease ontology we can use it to train our synthetic generator.

The English is becoming the predominant language in the research community and it is really hard to find (enough) data in other languages: everyone who wants to share his data and informations via Internet have to provide them in English if he wants to increase its visibility and availability.
The Italian constrain posed by the project drastically limits the data sources and no public database was found.
We would stress that as database we consider a public available set of structured data which can be downloaded and easily used.

Surfing on Internet many web pages can be found about diseases and their interactions with symptoms and causes, the so-called *on-line doctor* [^1]  (or Medical Services) pages.
An on-line doctor is a querable Internet service which allows to provide user auto-diagnosis based on the information provided.
The validity of the informations inside these tools is only partially guaranteed by the service provider and thus it can not be considered as a scientific method for medical diagnosis.
However, the amount of informations collected by these applications is very interesting and it can be used to simulate reasonable medical queries, needed by our project.
Also in this case is important to notice that despite the availability of these public informations the data are structured according to the web page needs and moreover there is not an immediate download of the raw data.

So, how can we obtain these useful informations and re-organize them into a structured data format?
The answer is given by the `web-scraping` techniques.
With the term `web-scraping` we identify the wide set of algorithms aim to extract the informations from a website, or more in general from the Internet.
All the Internet pages are intrinsically pieces of codes written in different programming languages (HTML, PHP, ...).
The major part of websites are written in HTML, an extreme verbose language, with more or less JavaScript supports.
Write a code is a sort of art and the way chosen to reach the desired result is left to the programmer: in these way we do not have a rigid standard (excepted by the programming language constrains) and under each website underlies a potential completely different ensemble of code lines.
Thus, the realization of a web-scraper poses several issues to the programmer who has to find the underlying patterns inside the web page to get the informations stored.

A web-scraping algorithm is made by a series of multiple steps which has to be performed automatically (without human overview).
First of all, the algorithm has to recognized the unique website structures: we can broadly summarize this task as the parsing of the underlying HTML code.
Inside the large amount of code lines [^2] are stored the set of informations useful for our application.
So, the algorithm should be able to detect the relevant and interesting part and filter them.
At this step we can easily reorganize the informations into a usable data format and save them.

There are multiple way in which all these tasks could be performed and multiple open source libraries provide user friendly interfaces for the creation of own web-scraper.
The most common one (and also used in our applications) is the `BeautifulSoup` [[richardson2007beautiful](https://www.crummy.com/software/BeautifulSoup/)] `Python` package.
This package provides a very powerful `Python` library designed to navigate and read website source codes.
The integration of this library with other pre- and post-processing techniques allow the extraction of the desired informations from websites and moreover their reorganization into a structured and usable data format.


[^1]: Famous English applications are [SteadyMD](https://www.steadymd.com/?utm_source=bestonlinedoctors&utm_medium=partner&utm_campaign=bizdev), [MDLIVE](https://www.mdlive.com/), [Sherpaa](https://sherpaa.com/), [LiveHealth Online](https://livehealthonline.com/) and so on. Each service provides slight different informations and the choice of the best one vary according to the user needs.

[^2]: Very large if we consider a pure HTML web page.

[**next >>**](./SymptomsNet.md)


