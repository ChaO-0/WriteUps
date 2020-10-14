let ans = [
  246,
  56,
  101,
  211,
  75,
  28,
  215,
  26,
  173,
  48,
  141,
  250,
  238,
  6,
  102,
  39,
  227,
  26,
  102,
  173,
  214,
  102,
  27,
  6,
  95,
  241,
  102,
  246,
  41,
  250,
  250,
  182,
];

let letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu1234567890_{}";
let flag = "COMPFEST12{tH3_c4T_15_v3rY_Cute}";

for (let i = 0; i < letters.length; i++) {
  console.log(letters.charCodeAt(i) ** 128 % 251, letters[i]);
}
