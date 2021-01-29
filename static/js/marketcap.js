//Import the price data for current top 10 coins 
let chartURL = "/api/api_coins";

d3.json(chartURL).then(function(data){

    //Results in order of Market Capitalisation
    var topten = ["BTC", "ETH", "USDT", "DOT", "XRP", "ADA", "LINK", "LTC", "BCH", "XLM"]
    var results = []
    var coin_ticker = []
    var coin_price = [] 
    var coin_name = []

    for (var j = 0; j < topten.length; j++) { 
        for (var i = 0; i < data.length; i++) { 
            if (data[i].asset_id == topten[j]){
                // results.push(data[i])
                results.push(data[i])
                coin_ticker.push(data[i].asset_id)
                coin_price.push(data[i].price_usd)
                coin_name.push(data[i].name)
            }
        }
    };
    // console.log(coin_ticker, coin_price, coin_name)


// MC given by Price * Circulating Supply 
//After initial chart is working, attempt another api to collect and sort by circulaiting supply top ten (if time)
//CURRENT TOP TEN 
//Bitcoin, Ethereum, Tether, Polkadot, Ripple, Cardano, Chainlink, Litecoin, Bitcoin Cash, Stellar

var circulating_supply = [
{name: "bitcoin", supply: 18611656},
{name: "ethereum", supply: 114421421},
{name: "tether", supply: 25196886298},
{name: "polkadot", supply: 904761407},
{name: "ripple", supply: 45404028640},
{name: "cardano", supply: 31112484646},
{name: "chainlink", supply: 402509556},
{name: "litecoin", supply: 66365548},
{name: "bitcoin_cash", supply: 18638494}, 
{name: "stellar", supply: 22239700519},
]

//Finding MC 
var market_capitalisation = []
for (var i = 0; i < coin_ticker.length; i++) { 
    market_capitalisation.push(coin_price[i] * circulating_supply[i].supply)
};

console.log(coin_name, market_capitalisation)

//Scaling MC for bubble size 
// var scaled_mc = []
// for (var i = 0; i < market_capitalisation.length; i++) { 
//     scaled_mc.push(market_capitalisation[i] / 1500000000)
// };


//Scaling MC for Y axis 
// var scaled_mc2 = []
// for (var i = 0; i < market_capitalisation.length; i++) { 
//     scaled_mc2.push(market_capitalisation[i] / 3)
// };



//Plot as a bubble chart to show BTC dominance of the field 
var trace1 = {
    x: coin_ticker,
    y: market_capitalisation,
    text: coin_name , 
    colorscale: 'Blackbody', 
    mode: 'markers',
    marker: {
      size: market_capitalisation, 
      sizeref: 10000000,
      sizemode: 'area'

    }
  };
  
  var data = [trace1];
  
  var layout = {
    title: 'Top 10 Crypto Market Capitalisations',
    showlegend: false,
    height: 800,
    width: 800
  };
  
  Plotly.newPlot('mainchart', data, layout);
  
});