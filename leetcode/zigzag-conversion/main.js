// problem: https://leetcode.com/problems/zigzag-conversion/

/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
  if (s.length === 1 || numRows <= 1) return s;

  const rows = [];
  for (let i = 0; i < numRows; i++) rows.push([]);

  let currentRow = 0;
  let zigzag = false;
  let result = "";
  for (let i = 0; i < s.length; i++) {
    rows[currentRow].push(s[i]);
    if (zigzag === false) currentRow++;
    else currentRow--;

    if (currentRow === numRows - 1 || currentRow === 0) zigzag = !zigzag;
  }

  rows.forEach((row) => {
    result += row.join("");
  });

  return result;
};

console.log(convert("AB", 1));
