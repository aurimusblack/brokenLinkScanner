***********************
* Broken Link Scanner *
***********************

BY ANIRUDH VALPADASU(@aurimusblack)

--------------------------------------------------------------------------------------------------------------------------------------

Initially crawls the <a> , <script> , <img> , <link> tags *webpage* for src , href links and stores them in an array.

later makes a get request to every link crawled and checks whether the link is broken or not based upon the HTTP Status code 

--------------------------------------------------------------------------------------------------------------------------------------

Usage :

python brokenLinkScanner.py http://yourwebsite.com

--------------------------------------------------------------------------------------------------------------------------------------

