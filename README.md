# Cryptocurrency hacks

This jupyter notebook contains some data collection and analysis I did on cryptocurrency hacks. Amazon's Mechanical Turk was used to crowd source business data on cryptocurrency exchanges. The questionnaire scripts and raw data are included in the MTurk folder.

Below are some example figures and conclusions.<br>
<b>[Click here for the full jupyter notebook report](https://dariusparvin.github.io/Cryptocurrency_hacks/)</b>
<br>


<h3>Timing of hacks relative to Bitcoin market cap</h3>
By eye, it appears as though most hacks occur shorts after a bull run in the Bitcoin market cap.<br>
Black points - Market Cap of Bitcoin (log scale) <br>
Red points - Timing of hack<br>
<img src="example_figures/MarketCap_vs_hacks.png">
<br>
<h3>Number of hacks per year relative to the number of cryptocurrency exchanges in operation</h3>
While the number of hacks in total has been increasing over the years, relative to the number of exchanges in operation this ratio has been decreasing, suggesting that cryptocurrency exchanges are implementing better security measures.
<img src="example_figures/hacks_per_exchange.png", width = "400">
<br>

<h3>Wallet type involved in hacks</h3>
"Hot" wallets refer to those where the private keys are stored on a device connected to the internet. While these are more convenient for signing transactions, they are considered to be much more vulnerable to hacking than a "cold" wallet, where the private keys are stored offline. This is reflected in the data, showing that 66% of hacks involved hot wallets, whereas only 5% involved cold wallets.
<img src="example_figures/wallets.png", width = "400">
