# Cryptocurrency Versus the Stock Market


Capstone Project
By Shaunil Maharaj


## Introduction

On January 25th, 2020, the Dow Jones traded above 20,000 for the first time, marking an important milestone in financial markets. Soon after, on February 5th, another important milestone was achieved for Bitcoin, having completed over 500 million transactions in it's 11 year history. The beginning of 2020 set expectations of a break out year for financial markets. Unfortunately, a deadly a viral outbreak had caused the US and World economies to come to a halt. In mid-March 2020, shelter in place orders and the forlough of non-essential employees began around the US, causing the assets market to take a price dive.

We will explore the performance of cryptocurrencies versus stock markets in order to gain insight on whether cryptocurrency can be seen as a worthy financial product. Observing the mean change of price of the past 20 days of each asset, we can gauge how well each marketplace reacted to shelter-in-place orders which caused a "bearish" marketplace where the price went down. Observing the mean change of price over the past 200 days will give us insight on how each marketplace performed during times of where the price went up, also known as a "bullish" market. 


### Data

We will scrape historical pricing data from yahoo finance from the top 3 stock exchanges and the top 3 cryptocurrencies for the past 3 years. This data will then be scrubbed by filling missing values by front fill method and indexed for non-trading days if applicable to the assest as cryptocurrencies can be traded at anytime while stocks can be traded during banking hours.


### Data Description

The important features of our data will be the adjusted closing price and the volume by trade. The adjusted closing price is the asset's closing price, adjusted for stock splits or cryptocurrency halving and volume by trade reports the net amount of trade of that asset by volume. A price change column will be added to record the daily change in price over time.

The data will include all historical pricing information from January 1st 2017 to April 9th 2020. The stock market has data from decades past but cryptocurrencies are relatively new so we will only go back 3 years.


## Exporatory Data Analysis


### Dow Jones versus Bitcoin

### NASDAQ versus Etherium

### S&P 500 versus XRP/Ripple


# Hypothesis Testing

We will Hypothesis test with the [Mann-Whitney U-test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test) which will no make any distributional assumptions considering the distributions of our assets could be very complicated. We will adopt the **Null Hypothesis** that each cryptocurrency is equally likely to grow in price as it's respective stock exchange counterpart. The **Alternate Hypothesis** is that the stock exchanges are better places for investment because they have better growth. We will test each hypothesis to a threshold of $\alpha = 0.05$ for each category.


## Dow Jones versus Bitcoin

### 3 year growth
  
**Null Hypothesis**: Bitcoin is likely to grow in price less than the Dow Jones grows in price.

**Alternate Hypothesis**: Bitcoin is likely to grow in price greater than the Dow Jones grows in price.
  
  $\alpha = 0.05$
  
  **P Value** = 0.011
  
We accept the **Alternative**, the p value for this competition is less than our threshold, signifying that the long term potential of bitcoin growth over the Dow Jones.
  
  
### Short term growth (20 days)

**Null Hypothesis**: Bitcoin is likely to grow in price less than the Dow Jones grows in price.

**Alternate Hypothesis**: Bitcoin is likely to grow in price greater than the Dow Jones grows in price.
  
  $\alpha = 0.05$
  
  **P Value** = 0.601
  
We accept the **Null**, with great significance we can say that in the short term, Dow Jones will grow and will likely to out grow bitcoin.

  
### Longer term growth (200 days)

**Null Hypothesis**: Bitcoin is likely to grow in price less than the Dow Jones grows in price.
  
**Alternate Hypothesis**: Bitcoin is likely to grow in price greater than the Dow Jones grows in price.

  $\alpha = 0.05$
  
  **P Value** = 0.896
  
We accept the **Null** once again. Long term growth for the Dow Jones will surpass that of bitcoin.



## Conclusion