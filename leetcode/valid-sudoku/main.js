// Problem: https://leetcode.com/problems/valid-sudoku/

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {
  // cehcking uniqueness of row and col
  for (let i = 0; i < 9; i++) {
    let rowTable = {};
    let colTable = {};
    for (let j = 0; j < 9; j++) {
      const rowNumber = board[i][j];
      const colNumber = board[j][i];
      // process.stdout.write(`${colNumber} `);
      // checking row
      if (rowNumber === ".") continue;
      if (rowTable[rowNumber] === undefined) rowTable[rowNumber] = 1;
      else return false;

      // checking col
      if (colNumber === ".") continue;
      if (colTable[colNumber] === undefined) colTable[colNumber] = 1;
      else return false;
    }
  }
  return true;
};

const isVal = isValidSudoku([
  ["5", "3", ".", ".", "7", ".", ".", ".", "."],
  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
  [".", "9", "8", ".", ".", ".", ".", "6", "."],
  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
  [".", "6", ".", ".", ".", ".", "2", "8", "."],
  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
  [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]);

console.log(isVal);
