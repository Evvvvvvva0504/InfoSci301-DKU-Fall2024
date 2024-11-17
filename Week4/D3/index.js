const width = 800, height = 400;
const svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

const layers = {
    input: 3,
    hidden1: 4,
    hidden2: 3,
    output: 2
};

const layerColors = {
    input: "#ff6f61",    // Red for input layer
    hidden1: "#6fa8dc",  // Blue for first hidden layer
    hidden2: "#93c47d",  // Green for second hidden layer
    output: "#f9cb9c"    // Orange for output layer
};

const layerNames = Object.keys(layers);
const layerSpacing = width / (layerNames.length + 1);
const nodeSpacing = height / (Math.max(...Object.values(layers)) + 1);

const nodes = [];
const links = [];
const labels = [];
const annotations = []; // To store layer annotations

let xPos = layerSpacing;

for (const layer of layerNames) {
    const count = layers[layer];
    const yPosStart = (height - (count - 1) * nodeSpacing) / 2;

    for (let i = 0; i < count; i++) {
        nodes.push({
            id: `${layer}-${i}`,
            x: xPos,
            y: yPosStart + i * nodeSpacing,
            layer,
            color: layerColors[layer]
        });
    }

    labels.push({
        text: layer.toUpperCase() + " LAYER",
        x: xPos,
        y: 30,
        layer
    });

    // Add layer annotation above the layer
    annotations.push({
        text: layer === "hidden1" ? "Hidden Layer 1" :
              layer === "hidden2" ? "Hidden Layer 2" :
              layer === "input" ? "Input Layer" : "Output Layer",
        x: xPos,
        y: 10
    });

    xPos += layerSpacing;
}

for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
        if (nodes[i].layer !== nodes[j].layer &&
            Math.abs(layerNames.indexOf(nodes[i].layer) - layerNames.indexOf(nodes[j].layer)) === 1) {
            links.push({ source: nodes[i], target: nodes[j] });
        }
    }
}

// Define arrow markers
const defs = svg.append("defs");

defs.append("marker")
    .attr("id", "arrowhead")
    .attr("viewBox", "0 0 10 10")
    .attr("refX", 10)
    .attr("refY", 5)
    .attr("markerWidth", 6)
    .attr("markerHeight", 6)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M 0 0 L 10 5 L 0 10 Z")
    .attr("fill", "#999");

defs.append("marker")
    .attr("id", "arrowhead-large")
    .attr("viewBox", "0 0 10 10")
    .attr("refX", 15)
    .attr("refY", 5)
    .attr("markerWidth", 8)
    .attr("markerHeight", 8)
    .attr("orient", "auto")
    .append("path")
    .attr("d", "M 0 0 L 10 5 L 0 10 Z")
    .attr("fill", "#333");

// Draw input and output arrows
svg.append("line")
    .attr("class", "input-arrow")
    .attr("x1", 0)
    .attr("y1", height / 2)
    .attr("x2", nodes.find(d => d.layer === "input").x - 30)
    .attr("y2", height / 2)
    .attr("stroke", "#333")
    .attr("stroke-width", 2.5);

svg.append("line")
    .attr("class", "output-arrow")
    .attr("x1", nodes.find(d => d.layer === "output").x + 30)
    .attr("y1", height / 2)
    .attr("x2", width)
    .attr("y2", height / 2)
    .attr("stroke", "#333")
    .attr("stroke-width", 2.5);

// Draw links
svg.selectAll(".link")
    .data(links)
    .enter()
    .append("line")
    .attr("class", "link")
    .attr("x1", d => d.source.x)
    .attr("y1", d => d.source.y)
    .attr("x2", d => d.target.x)
    .attr("y2", d => d.target.y)
    .attr("stroke", "#999")
    .attr("stroke-width", 1.5)
    .attr("opacity", 0.8);

// Draw nodes
svg.selectAll(".node")
    .data(nodes)
    .enter()
    .append("circle")
    .attr("class", "node")
    .attr("cx", d => d.x)
    .attr("cy", d => d.y)
    .attr("r", 12)
    .attr("fill", d => d.color)
    .attr("stroke", d => d3.rgb(d.color).darker())
    .attr("stroke-width", 2)
    .style("filter", "drop-shadow(0px 2px 3px rgba(0, 0, 0, 0.3))");

// Draw labels
svg.selectAll(".label")
    .data(labels)
    .enter()
    .append("text")
    .attr("class", "label")
    .attr("x", d => d.x)
    .attr("y", d => d.y)
    .text(d => d.text)
    .attr("font-size", "14px")
    .attr("font-weight", "bold")
    .attr("fill", "#333")
    .attr("text-anchor", "middle");

// Draw layer annotations
svg.selectAll(".annotation")
    .data(annotations)
    .enter()
    .append("text")
    .attr("class", "annotation")
    .attr("x", d => d.x)
    .attr("y", d => d.y)
    .text(d => d.text)
    .attr("font-size", "16px")
    .attr("font-weight", "bold")
    .attr("fill", "#333")
    .attr("text-anchor", "middle");
