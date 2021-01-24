//alert("The Coins Javascript file was loaded...");
var plotpoints = {};
let chartURL = "/api/api_coins";

//Define chart size
var svgWidth = 1200;
var svgHeight = 660;

//Define chart margins
var chartMargin = {
  top: 30,
  right: 100,
  bottom: 30,
  left: 100
};

// Define dimensions of the chart area
var chartWidth = svgWidth - chartMargin.left - chartMargin.right;
var chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
var svg = d3.select(".mainchart")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

// Append a group to the SVG area and shift ('translate') it to the right and to the bottom
var chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

// Import Data
d3.json(chartURL).then(function(chartData, err) {
  if (err) throw err;

  chartData.shift();
  console.log(chartData)


  // load data
  chartData.forEach(function(d) {
    plotpoints.asset_id = +d.asset_id;
    plotpoints.price_usd = +d.price_usd;
    console.log(d.asset_id + " --- " + d.price_usd);
  });

    // Step 2: Create scale functions
    // ==============================
    var xBandScale = d3.scaleBand()
    .domain(chartData.map(plotpoints => plotpoints.asset_id))
    .range([0, chartWidth])
    .padding(0.1);

  // Create a linear scale for the vertical axis.
  var yLinearScale = d3.scaleLinear()
    .domain([0, d3.max(chartData, plotpoints => plotpoints.price_usd)])
    .range([chartHeight, 0]);

    // Step 3: Create axis functions
    // ==============================
    var bottomAxis = d3.axisBottom(xBandScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Step 4: Append Axes to the chart
    // ==============================
    chartGroup.append("g")
    .call(leftAxis);

    chartGroup.append("g")
    .attr("transform", `translate(0, ${chartHeight})`)
    .call(bottomAxis);

    // // Bar
    var barGroup = chartGroup.selectAll(".bar")
    .data(chartData)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", plotpoints => xBandScale(plotpoints.asset_id))
    .attr("y", plotpoints => yLinearScale(plotpoints.price_usd))
    .attr("width", xBandScale.bandwidth())
    .attr("height", plotpoints => chartHeight - yLinearScale(plotpoints.price_usd));

    // Step 6: Initialize tool tip
    // ==============================
    var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
        return (`Name: ${d.name}<br>Asset Code: ${d.asset_id}<br>Price in USD: ${d.price_usd}`);
      });

    // Step 7: Create tooltip in the chart
    // ==============================
    chartGroup.call(toolTip);

    // Step 8: Create event listeners to display and hide the tooltip
    // ==============================
    barGroup.on("mouseover", function(data) {
      toolTip.show(data, this);
    })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });

    // Create axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - chartMargin.left + 40)
      .attr("x", 0 - (chartHeight / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Price (USD)");

    chartGroup.append("text")
      .attr("transform", `translate(${chartWidth / 2}, ${chartHeight + chartMargin.top + 30})`)
      .attr("class", "axisText")
      //.attr("transform", "rotate(-65)")
      .text("Cryptocurrency Code");


  }).catch(function(error) {
    console.log(error);
  });