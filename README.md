## Hello welcome to The Market Dashboard. 
There are two parts to this project with part one being the stock page and part two being the options page. 

### 1) Stock Page
   The main features of this page will be with the selection of a stock using their symbol a candlestick graph of their past market data will be displayed,
   as well as their current price, volume, all time high for the period and all time low for the period. Then under the graph it will be met with their dividend
   percentage, EPS, and PE.

### 2) Options Page
   This page will revolve around calculations instead of display like the stock page. For example with a given stock inputted it will display the options contracts data and when
   the user selects one the IV (Involuntary Volatility), and the Greeks (Delta, Gamma, Theta, Vega, Rho) will be calculated as well.

## What are the Greeks?
The Greeks are used to measure risk on how the price of an options contract is going to shift based on a multitude of factors. 
### Delta (Δ): 
It measures how much the price of the option will change for the dollar ($1) change in the stock, in physics terms think of it as the velocity of the options price.

For calls it will be between 0 - 1

For puts it will be between -1 - 0

Example: With 0.6 for NVDA every dollar the stock rises the price of the call will increase by 60 cents vice versa with a put. 

### Gamma (Γ):
It is used to measure how much the Delta changes per dollar change of the underlying stock, in physics think of it as the acceleration to the velocity. 

Gamma will always be a positive value since it is derived from both the stock price and Delta value. It is critical for hedging against risk but is often misunderstood. 

Gamma will the at its highest whenever the options contract is At-The-Money (ATM) which can cause somethign called Gamma Risk which results in huge swings in Delta. However when the contract is Deep In-The-Money (ITM) or Out-The-Money (OTM) the Gamma will be low. 

Example: You have a Delta of 0.6 and a Gamma of 0.1, AAPL goes up one dollar and now your new Delta is 0.7, but soon AAPl drops a dollar now your delta is back at 0.6. 

Theta (Θ):
Vega (ν):
Rho (ρ):

## What is IV? 
