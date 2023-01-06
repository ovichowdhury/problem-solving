// Problem: https://leetcode.com/problems/valid-sudoku/

/**
 * Checks validity of sub grid
 */
var isSubGridValid = function (board, iStart, iEnd, jStart, jEnd) {
  const ht = {};
  for (let i = iStart; i <= iEnd; i++) {
    for (let j = jStart; j <= jEnd; j++) {
      const number = board[i][j];
      if (ht[number] === undefined) {
        if (number !== ".") ht[number] = 1;
      } else return false;
    }
  }
  return true;
};

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
      if (rowTable[rowNumber] === undefined) {
        if (rowNumber !== ".") rowTable[rowNumber] = 1;
      } else return false;

      // checking col
      if (colTable[colNumber] === undefined) {
        if (colNumber !== ".") colTable[colNumber] = 1;
      } else return false;
    }
  }
  // checking uniqueness of 3X3 grid
  if (
    isSubGridValid(board, 0, 2, 0, 2) &&
    isSubGridValid(board, 0, 2, 3, 5) &&
    isSubGridValid(board, 0, 2, 6, 8) &&
    isSubGridValid(board, 3, 5, 0, 2) &&
    isSubGridValid(board, 3, 5, 3, 5) &&
    isSubGridValid(board, 3, 5, 6, 8) &&
    isSubGridValid(board, 6, 8, 0, 2) &&
    isSubGridValid(board, 6, 8, 3, 5) &&
    isSubGridValid(board, 6, 8, 6, 8)
  )
    return true;
  else return false;
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
