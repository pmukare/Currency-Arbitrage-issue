# Currency-Arbitrage-issue

An arbitrage is the simultaneous purchase and sale of an asset in order to profit from a difference in the price. This type of trade exploits price differences between similar or identical financial instruments, either on different markets or in different forms.

You are a currency trader looking for arbitrage opportunities in the currency market using these three quotes:

1.	The cost of USD per EUR (USD/EUR) for converting USD to EUR.
2.	The cost of EUR per GBP (EUR/GBP) for converting EUR to GBP.
3.	The cost of GBP per USD (GBP/USD) for converting GBP to USD.

You must use your USD to buy EUR, then use your EUR to buy GBP, and finally use your GBP to buy USD, resulting in some sort of profit or loss (i.e., USD to EUR to GBP to USD). Reverse trading is not allowed, so you are limited to the 3 exchanges in the direction shown above. For example, you can convert USD to EUR, which means selling US Dollars and buying Euros; you cannot invert the fraction to sell Euros and buy US Dollars.

Given 100,000 USD for each trade, calculate the arbitrage profit truncated to whole dollars (USD); otherwise, print 0 if there is no arbitrage opportunity.


Input Format

The locked stub code in your editor reads the following input from stdin and passes it to your function:

The first line contains a single integer, N, denoting the number of quotes.

Each of the N subsequent lines describes a quote in the form of three space-separated floating-point numbers:

1.	The first quote is a real number denoting the price quote for (USD/EUR).
2.	The second quote is a real number denoting the price quote for (EUR/GBP).
3.	The third quote is a real number denoting the price quote for (GBP/USD).

Your function takes a string array parameter containing each of the N lines as described above, in the same order.


Constraints

1 ≤ N ≤ 1000
0.001 < quotes ≤ 1000



Output Format

The function must return an integer array that contains the arbitrage profit for each trade in the same order that they appear in the input. If no arbitrage opportunity exists, set that profit to 0 . The resulting array should have a total of N elements.


Sample Input


2
1.1837 1.3829 0.6102
1.1234 1.2134 1.2311



Sample Output


114
0



Explanation

There are N = 2 test cases:

1. You use your 100,000 USD to buy 84,480.8651 EUR. You then use your 84,480.8651 EUR to buy 61,089.6414 GBP. Finally, you use your 61,089.6414 GBP to buy 100,114.1288 USD. Because we started out with 100,000 USD, our net profit in whole dollars is 114 USD.

2. There is no arbitrage opportunity here (the conversion would end up losing money), so we print 0.
