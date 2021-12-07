



function gridTraversal(row, col) {
    if (row === 0 || col === 0) return 0;
    if (row === 1 && col === 1) return 1;
    return gridTraversal(row - 1, col) + gridTraversal(row, col - 1);
}

function gridTraversalDP(row, col, memo = {}) {
    const key = row + "=>" + col;
    if (row === 0 || col === 0) return 0;
    if (row === 1 && col === 1) return 1;
    if(key in memo) return memo[key];

    memo[key] = gridTraversalDP(row - 1, col, memo) + gridTraversalDP(row, col - 1, memo);
    return memo[key];
}



console.log(gridTraversal(3, 3));
console.log(gridTraversalDP(25, 25));