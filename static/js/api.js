//alert("The Overview Javascript file was loaded...");

function init() {

  let chartURL = "/api/api_overview";
  console.log(chartURL);
  console.log('#####')

  d3.json(chartURL).then(function (data) {
    chartData = data[0].name;
    console.log(chartData);
    chartData = data[0].asset_id;
    console.log(chartData);
    chartData = data[0].price_usd;
    console.log(chartData);
  });
}

// Call initialisation function
init();