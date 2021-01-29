var coinlist = {};
let chartURL = "/api/api_coins";

function initdropdown() {

  var dropdown = d3.select("#selDataset");

  d3.json(chartURL).then((d) => {
    d.forEach(function (id, index) {
      dropdown.append("option").text(id.asset_id).property("value", id.asset_id);
    });
  });
};

initdropdown();

//Initializes the page with a default plot
function init() {
  data = [{
    x: [1, 2, 3, 4, 5],
    y: [1, 2, 4, 8, 16]
  }];

  Plotly.newPlot("mainchartdiv", data);
}

init();

// Call updatePlotly() when a change takes place to the DOM
d3.select("#selDataset").on("change", updatePlotly);

// This function is called when a dropdown menu item is selected
function updatePlotly() {
  // Use D3 to select the dropdown menu
  var dropdownMenu = d3.select("#selDataset");
  // Assign the value of the dropdown menu option to a variable
  var dataset = dropdownMenu.property("value");
  //console.log(dataset);


  //UPDATE CODE
  //COIN UPDATE FUNCTION USING JAVASCRIPT
  var api_key = "200EF4DD-8BF3-4A8A-9FC9-CF9C9D6D1173";
  var myvar = {};
  var xplots = [];
  var yplots = [];
  var myurl = "https://rest.coinapi.io/v1/ohlcv/" + dataset + "/USD/history?period_id=6HRS&time_start=2021-01-26T00:00:00&apikey=" + api_key;

  $.ajax({
    url: 'https://rest.coinapi.io/v1/ohlcv/' + dataset + '/USD/history?period_id=6HRS&time_start=2021-01-26T00:00:00', // The URL to the API
    type: 'GET', // The HTTP Method, can be GET POST PUT DELETE etc
    data: {}, // Additional parameters here
    dataType: 'json',
    success: function (data) {
      myvar = data; myvar
        .forEach(function (item, index) {
          yplots.push(data[index].price_close,
            xplots.push(data[index].time_period_start),
          )
        })
    },
    error: function (err) { alert(err); },
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CoinAPI-Key", "200EF4DD-8BF3-4A8A-9FC9-CF9C9D6D1173"); // Enter here your key
    }
  });

  //console.log("#######");
  console.log(myurl)
  console.log(yplots);
  console.log(xplots)
  //var sdate = xplots[0];
  //console.log(sdate);
  //END UPDATE CODE

  //     // Initialize x and y arrays
  //     var x = [];
  //     var y = [];

  //     if (dataset === 'dataset1') {
  //       x = [1, 2, 3, 4, 5];
  //       y = [1, 2, 4, 8, 16];
  //     }

  //     if (dataset === 'dataset2') {
  //       x = [10, 20, 30, 40, 50];
  //       y = [1, 10, 100, 1000, 10000];
  //     }

  //     // Note the extra brackets around 'x' and 'y'
  Plotly.restyle("mainchartdiv", "x", [xplots]);
  Plotly.restyle("mainchartdiv", "y", [yplots]);
}