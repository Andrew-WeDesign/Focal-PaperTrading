Focal - a paper trading experiment


What does it do?

Using HTTP Get and Post requests in python to get data, process the data into common stock indicators like MACD and Stochastic Oscillator, make decision on a good time or buy and sell then executing those buy and sell commands.


What does it use?

The core of this project uses 2 libraries: Alpaca's trading API and btalib.


How does it work?

All data is stored into JSON files locally (used json as I was planning on using MongoDB in the future versions) and from that data algorithms determine if different types stock indicators (Trending, Volume, Momentum, and Volitility) create a buy or sell signal


Does it make money?

Yes, it does turn a profit when paper trading and can be viewed through a gui on Alpaca's website, BUT the profit I was experiencing was not going to beat out just putting your money in SPY. More tweaking to the buy and sell algorithms could almost certainly yield better profit, I am not currently working on this and plan to rewrite the program in another language before doing anymore work.


Why did I make this?

As I was first learning to write programs Python and C# interested me the most, but writing a program and entering in filler/placeholder data was not something I wanted to do. I decided the amount of data collected on stocks would be a lot more interesting and fulfilling to use than something that had little or no use. Finally who wouldn't want to make a bot that could buy and sell stocks at a profit without any user input? 
