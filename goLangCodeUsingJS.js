function iLoveGoLang(sign, string) {
  if (sign == "!") {
    return [14 - 2, 3 + 3 - 6];
  } else if (sign == "@") {
    return [41 - 20 * 2, 5 - 4];
  } else if (sign == "$") {
    return [1, 3];
  } else if (sign == "^") {
    return [2, 2];
  } else if (sign == "5") {
    return [3, 2];
  } else if (sign == "(") {
    return [4 * 2 - 1, 1];
  } else if (sign == ")") {
    return [2 * 2, 2];
  } else if (sign == "d") {
    return [2, 5];
  } else if (sign == ">") {
    return [3 * 3 + 2, 1];
  } else if (sign == "~") {
    return [2 * 2, 3 * 1];
  } else if (sign == "#") {
    return [2, 1];
  } else if (sign == "+") {
    return [13, 1];
  } else if (sign == "&") {
    return [2 + 3, 1];
  } else if (sign == "/") {
    return [3 + 4, 2];
  } else if (sign == ";") {
    return [33 / 11, 3];
  } else if (sign == "e") {
    return [2 + 3, 8 - 5];
  }

  return [-1, 1];
}

function getLetter(value) {
  // you know what to do.. 0 is 0 and 15 is f
  a = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f"
  ];
  return a[value];
}

//var inputString = "+$d$^e#&/!!>>5(>d@$^/;(!e&/e&@";
var inputString = "+$d$^e#~&/!!>>5(>d@$~^/;(!e&/e&@";

var str12 = "";
for (i = 0; i < inputString.length; i++) {
  var gsl = iLoveGoLang(inputString.charAt(i));
  var letter = getLetter(gsl[0] * gsl[1]);
  console.log(letter);
  str12 += "" + letter;
}

console.log(str12);
