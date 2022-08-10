# Stock-Grade-Project-by-Flask-and-Crawler
This is a Stock Grading project by crawler, Flask and Bootrap. 

To begin with, I aim to use the Profit matrix theory to evaluate stocks in Taiwan by grading them in A1, A2, B1, B2, C1, C2 and D.
![image](https://github.com/BoddyShen/Stock-Grading-Project-by-Flask-and-Crawler/blob/85e44efb85e85aa98c0621b99a5e5458a14942ae/image/stock_grade.png)
Reference: [雷浩斯價值投資網](https://redhouse.statementdog.com/archives/2178#more-2178,https://statementdog.com/explain/earningMatrix.html)

By using annual ROE and Free Cashflow as references, we can grade the stock and evalute its profitability in a certain period.

See the [demo](https://www.youtube.com/watch?v=bwfWWsZeR0M&ab_channel=BoddyShen).

# Design
[image](https://github.com/BoddyShen/Stock-Grading-Project-by-Flask-and-Crawler/blob/e766be2ab81951a03ab5ec77d2a0630d1aa175b7/image/Stock_Grading.png)
<br>
<br>
This project uses Python-Flask as the backend, and the design is presented above. The backend uses "blueprint" to build a cleaner structure, including "core" and "users". The "core" is only for the landing page, and "users" is for other routes.

