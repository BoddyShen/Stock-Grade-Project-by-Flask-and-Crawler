# Stock-Grade-Project-by-Flask-and-Crawler
This is a Stock Grading project by crawler, Flask and Bootrap.

To begin with, I aim to use the Profit matrix theory to evaluate stocks in Taiwan by grading them in A1, A2, B1, B2, C1, C2 and D.
![image](https://github.com/BoddyShen/Stock-Grade-Project-by-Flask-and-Crawler/blob/fc672df17656662982a2fbca6fb4f088c59f3077/image/Profit_Matrix.png)
![image](https://github.com/BoddyShen/Stock-Grade-Project-by-Flask-and-Crawler/blob/7041326f5e6cb541cc22e9714e0d4127fe05c780/image/Grade.png))
Reference: 雷浩斯價值投資網(https://redhouse.statementdog.com/archives/2178#more-2178,https://statementdog.com/explain/earningMatrix.html)

By using annual ROE and Free Cashflow as references, we can grade the stock and evalute its profitability.




This project uses Python-Flask as the backend, and the design is presented above. The backend uses "blueprint" to build a 
cleaner structure, including "core" and "users". The "core" is only for the landing page, and "users" is for other routes.

