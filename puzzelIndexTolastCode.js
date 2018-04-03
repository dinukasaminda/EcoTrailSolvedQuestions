var s = ""; // puzzl below code
var sDictionry = s.split("");

var list = [
  7,
  2,
  3,
  19,
  5,
  11,
  1,
  21,
  28,
  10,
  25,
  12,
  32,
  9,
  15,
  24,
  6,
  14,
  4,
  29,
  18,
  17,
  23,
  31,
  22,
  26,
  27,
  8,
  20,
  13,
  16,
  30
];
console.log("detected len:" + list.length);
var s2 = [];
for (var i = 0; i < list.length; i++) {
  s2[i] = sDictionry[list[i] - 1];
}
console.log(s2);

var str = "";
for (var i = 0; i < s2.length; i++) {
  str += "" + s2[i];
}

console.log(str);
