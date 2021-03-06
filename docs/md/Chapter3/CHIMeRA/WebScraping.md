## How to find the data - Web Scraping

The INFN [FiloBlu project](https://agenda.infn.it/event/16961/contributions/34949/attachments/24579/28029/filoblu_0312.pdf) was developed by the collaboration between the Physics Department of the University of Bologna and the INFN group of the Sapienza University of Rome.
The project aims to implement a NLP pipeline to process messages with medical theme using sentimental analyses.
Domiciliary care for oncologic patients is preferred due to cheaper costs than hospitalization and a more comfortable living for the him.
To successfully follow therapy during the domiciliary care the patient is in constant contact with health-care professionals and he is monitored frequently during his therapy.
Patients are interested in actively collaborate to the management of their health and they are willing to use also ICT technologies.
The FiloBlu project meets the citizens' needs developing a tool to optimize the efficiency and the effectiveness of care processes developing two APPs (patient and medical sides) to support doctor-patient communication.
The final purpose of the project is to process doctor-patient chat messages (using an interface similar to "WhatsApp") computing from them a score related to the patient state.
The APPs are equipped with features specifically designed for health-care applications and using a Natural Language Processing pipeline on the text messages we compute an "attention" score for each of them.
The "attention" score is then used to rank the patients' messages on the medical side and thus prioritize potential critical situations.

The project was financed by Lazio region and it was developed to work at the Sant'Andrea Hospital of Rome so the project involves only Italian words.
This constrain drastically affects the data availability which are very hard to find on-line.
The text messages analysis concerns the evaluation of critical keywords and medical terms so we faced on this problem generating a diseases ontology.
In particular we were interesting in the relation between symptoms, diseases and their mutual interactions for the realization of our score function.
More details about the pipeline used for the message processing are given in [Appendix E](../../Appendix/FiloBlu/README.md).

The English is becoming the predominant language in the research community and it is really hard to find (enough) data in other languages: everyone who wants to share his data and information via Internet have to provide them in English if he wants to increase its visibility and availability.
The Italian constrain posed by the project drastically limits the data sources and no public database was found.
We would stress that as database we consider a publicly available set of structured data which can be downloaded and easily used.

Surfing on Internet many web pages can be found about diseases and their interactions with symptoms and causes, the so-called *on-line doctor* [^1]  (or Medical Services) pages.
An on-line doctor is a querable Internet service which allows to provide user auto-diagnosis based on the information provided.
The reliability of the information stored in these tools is only partially guaranteed by the service provider and thus it can not be considered as a scientific method for medical diagnosis.
However, the amount of information collected by these applications is very interesting and it can be used to simulate reasonable medical queries, needed by our project.
Also in this case, it is important to notice that, despite the availability of these public information, the data are structured according to the web page needs and moreover there is not an immediate download of the raw data.

So, how can we obtain these useful information and re-organize them into a structured data format?
The answer is given by the `web-scraping` techniques.
With the term `web-scraping` we identify the wide set of algorithms aim to extract the information from a website, or more in general from the Internet: while `web-scraping` can be done also manually, with this term we typically refer to automated processes.
All the Internet pages are intrinsically pieces of codes written in different programming languages (HTML, PHP, ...).
The major part of websites are written in HTML, an extreme verbose language, with more or less JavaScript supports.
The way chosen to write a code and to reach the desired output is always left to the programmer: in these way we do not have a rigid standard (excepted by the programming language constrains) and under each website underlies a potential completely different ensemble of code lines.
Thus, the realization of a web-scraper poses several issues to the programmer who has to find the underlying patterns inside the web page to get the information stored.
In other words, the `web-scraping` technique is an emblematic example of Big Data Analytics algorithm since it aims to extract a *value* from a large amount of *unstructured* information (raw website code).

A web-scraping algorithm is made by a series of multiple steps which has to be performed automatically (without human overview).
First of all, the algorithm has to recognized the unique website structures: we can broadly summarize this task as the parsing of the underlying HTML code.
Inside the large amount of code lines [^2] are stored the set of information useful for our application.
So, the algorithm should be able to detect the relevant and interesting part and filter them.
At this step we can easily reorganize the information into a usable data format and save them.

There are multiple way in which all these tasks could be performed and multiple open source libraries provide user friendly interfaces for the creation of own web-scraper.
The most common one (and also used in our applications) is the `BeautifulSoup` [[richardson2007beautiful](https://www.crummy.com/software/BeautifulSoup/)] `Python` package.
This package provides a very powerful `Python` library designed to navigate and read website source codes.
The integration of this library with other pre- and post-processing techniques allow the extraction of the desired information from websites and moreover their reorganization into a structured and usable data format.


[^1]: Famous English applications are [SteadyMD](https://www.steadymd.com/?utm_source=bestonlinedoctors&utm_medium=partner&utm_campaign=bizdev), [MDLIVE](https://www.mdlive.com/), [Sherpaa](https://sherpaa.com/), [LiveHealth Online](https://livehealthonline.com/) and so on. Each service provides slight different information and the choice of the best one vary according to the user needs.

[^2]: Very large if we consider a pure HTML web page.

[**next >>**](./SymptomsNet.md)


