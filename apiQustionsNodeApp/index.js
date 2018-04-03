const express = require("express");
const path = require("path");
const bodyParser = require("body-parser");
var fs = require("fs");

var request = require("request");
var base64 = require("base-64");
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

var data1 = {
  email: "saranathinfo@gmail.com",
  key: "d3a34f2c5e00bb67ba13c4e970f5ef51"
};
var data2 = {
  email: "saranathinfo@gmail.com",
  key: "d3a34f2c5e00bb67ba13c4e970f5ef51",
  answer: ""
};
var data = data1;
var token1 =
  "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJxdWVzdGlvbiI6IjAxLUxNSy03IiwiZXhwIjoxNTIxMjg4NDIzLCJpYXQiOjE1MjEyODgzOTMsImVtYWlsIjoibmFydGhhbmFqQGdtYWlsLmNvbSIsImtleSI6IjQ2ODNlNzM5MzUwNjQ5YmRmMjA5YzQ3ZGE2YjEzYjViIn0.5j_fP0kZjSmKNhVe_7dC4U74bS2fn16U7sZE5s_Tp8c";

function recrt1(auth) {
  rl.question("What do you think of Node.js? ", answer1 => {
    // TODO: Log the answer in a database
    console.log(`Thank you for your valuable feedback: ${answer1}`);

    request(
      {
        uri: "http://api.ecotrail.gdgsrilanka.org/",
        method: "POST",
        body: JSON.stringify({
          email: "saranathinfo@gmail.com",
          key: "d3a34f2c5e00bb67ba13c4e970f5ef51",
          answer: answer1
        }),
        headers: {
          "Content-Type": "application/json",
          Authorization: auth
        },
        timeout: 10000,
        followRedirect: true,
        maxRedirects: 10
      },
      function(error, response2, body7) {
        console.log(body7);
        var auth2 = response2.headers["authorization"];
        recrt1(auth2);
      }
    );
  });
}
request(
  {
    uri: "http://api.ecotrail.gdgsrilanka.org/",
    method: "POST",
    body: JSON.stringify(data1),
    headers: {
      "Content-Type": "application/json"
    },
    timeout: 10000,
    followRedirect: true,
    maxRedirects: 10
  },
  function(error, response, body) {
    console.log(body);
    var auth2 = response.headers["authorization"];
    recrt1(auth2);
  }
);
/*
const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log("Server started on port:" + PORT);
});*/
