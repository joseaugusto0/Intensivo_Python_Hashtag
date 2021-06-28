# Intensivão Python - Hashtag Programações
![Python](https://github.com/MikeCodesDotNET/ColoredBadges/blob/master/svg/dev/languages/python.svg)

## Description
  Intensivão Python was a programming week proposed by [Hashtag Programaçãoo](https://www.youtube.com/channel/UCafFexaRoRylOKdzGBU6Pgg) which approached different useful applications in Python language. Each day had a different project, separed by folder in this repository.


# Index

- [Instalation](#instalation)
- [Projects Description](#project-description)
- [My Annotations - Day 1](https://github.com/joseaugusto0/Intensivo_Python_Hashtag/tree/main/1-System_automation/Annotations)
- [My Annotations - Day 2](https://github.com/joseaugusto0/Intensivo_Python_Hashtag/tree/main/2-Data_Analysis/Annotations)
- [My Annotations - Day 3](https://github.com/joseaugusto0/Intensivo_Python_Hashtag/tree/main/3-Data_Science_and_Machine_Learning/Annotations)
- [My Annotations - Day 4](https://github.com/joseaugusto0/Intensivo_Python_Hashtag/tree/main/4-Web_Scraping/Annotations)


## Instalation
-   Clone all the repository quoted in [Intensivo_Python_Hashtag](https://github.com/joseaugusto0/Intensivo_Python_Hashtag)
-   You can set different environments for the different projects proposed in this repository
    -   In all project folders, has a requirements.txt, so you can set your environment, and install all dependencies that you need with this command:
    ```
        pip install -r requirements.txt
    ```

## Projects Description
The programming week was composed basically by four project:

### 1 - System Automation
That application will simulate a billing email sent everyday in a commerce business. This email contains the sales amount in the day, like a daily report. Our application will automate the mouse and the keyboard with **pyautogui** library. Basically, the app will read a .xlsx file (which contains the sales of the day), abstract the informations, open the gmail, put the informations needed (recipient, the email subject, and the email body), and send automatically the email.

### 2 - Data Analysis
This application will simulate a telecom company which sells different kinds of service like internet and telephone. Although, recently had a 26% of churns (users cancelling their services), our application will check some possibilities for that churns. Will be imported an archive which contains clients (which has some service registered, and the ones who canceled) informations, like gender, type of contract signed, if have any dependents. And with that informations, show the proportions in different graphs, to make more easy to abstract some possibilities to why users has been cancelling some services. 

### 3 - Data Science and Machine Learning
That day, we simulate a company that make some advertisements in different types of media: TV, Radio and Newspaper. Our job was to import an archive which contains the percentage invested in advertisements for each communication channel and the monetary return at the end of the month. With that informations, make a machine learning to predict the monetary return if we change the percentage invested in the three types of media.

### 4 - Web Scraping
Basically our application will get a Excel sheet, which contains some products in different coins (euro, dolar and gold), get the coin value quoted on the day on some websites via web scraping (with selenium library), an update automatically the final price from each product on our sheet.   


### Created by: [José Augusto Coura](https://github.com/joseaugusto0) and [Teacher Lira Hashtag](https://www.instagram.com/hashtagprogramacao/)


