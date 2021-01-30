//alert("The Overview Javascript file was loaded...");

function init() {

  let chartURL = "/api/api_overview";
  //console.log(chartURL);
  //console.log('#####');
  xplots = [];
  yplots = [];

  d3.json(chartURL).then(function (data) {
    data.forEach(function (d) {
      xplots.push(d.asset_id);
      yplots.push(d.price_usd);
    });

    xplots.shift();
    yplots.shift();
    xplots.shift();
    yplots.shift();
    xplots.shift();
    yplots.shift();

    //console.log(xplots);
    //console.log(yplots);

    var trace1 = {
      x: xplots,
      y: yplots,
      type: "bar",
      color: "#063970"
    };

    var data = [trace1];

    var layout = {
      title: "Current Cryptocurrency Prices in $USD",
      font: {
        family: 'ABeeZee',
        size: 12,
        color: '#7f7f7f'
      },
      xaxis: { title: "Cryptocurrency code" },
      yaxis: { title: "Price in USD" },
    };

    Plotly.newPlot('mainchartdiv', data, layout);
  })
}

// Call initialisation function
init();