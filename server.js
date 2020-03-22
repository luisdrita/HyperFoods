// ---------------------------------------------- Importing Packages ----------------------------------------------

const fs = require('fs');
const express = require('express');
const {PythonShell} = require('python-shell');
const pluralize = require('pluralize');

const app = express();
let ingredient_top5SimilarIngredients = JSON.parse(fs.readFileSync('./data/recipe1M+/ingredient_top5SimilarIngredients.json', 'utf-8'));

app.use(express.static('website'));
app.listen(process.env.PORT || 3000);

// ---------------------------------------------- From Binary to String Function ----------------------------------------------

function binaryToString(str) {
    // Removes the spaces from the binary string
    str = str.replace(/\s+/g, '');
    // Pretty (correct) print binary (add a space every 8 characters)
    str = str.match(/.{1,8}/g).join(" ");

    let newBinary = str.split(" ");
    let binaryCode = [];

    for (let i = 0; i < newBinary.length; i++) {
        binaryCode.push(String.fromCharCode(parseInt(newBinary[i], 2)));
    }

    return binaryCode.join("");
}

// ---------------------------------------------- Server Receiving Image URL ----------------------------------------------

// Sending data back to interface that resulted from community finding process.
app.get('/run/:url', function (req, res) {

    let options = {
  mode: 'text',
  pythonOptions: ['-u'], // get print results in real-time
  scriptPath: './',
  args: [binaryToString(req.params.url)]
};

PythonShell.run('demo.py', options, function (err, results) {
  if (err) throw err;

  // results is an array consisting of messages collected during execution
  console.log('results: %j', results[2]);
  res.send(results[0] + "," + results[2]);
});
});

app.get('/ingredient/:ingr', function (req, res) {

    let alternative_ingredients = "";

    for (let i = 0; i < 5; i = i + 1) {

        alternative_ingredients = alternative_ingredients + "," + ingredient_top5SimilarIngredients[pluralize.singular((req.params.ingr).replace(/^\s/, ""))][i][0]
    }

    res.send(alternative_ingredients)
});