/**
 * Given a number n and an array of positive number m[]
 * Can you sum up to n using the elements of m
 * for ex. bestSum(7, [2, 4, 5, 7]) = [2, 5] and [7]
 * bestSum(5, [1, 3]) = null
 * Here you have to optimize the solution and return the shortest solution
 * for ex. bestSum(8, [1, 4, 5]) = [5, 1, 1, 1] and [4, 4]
 * you have to return [4, 4] rather than [5, 1, 1, 1]
 */


function bestSum(targetSum, numbers) {
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    let shortestCombination = null;

    for (let num of numbers) {
        let remainder = targetSum - num;
        let newCombination = bestSum(remainder, numbers);
        if (newCombination !== null) {
            let possibleCombination = [...newCombination, num];
            if (shortestCombination === null || possibleCombination.length < shortestCombination.length) {
                shortestCombination = possibleCombination;
            }
        }
    }

    return shortestCombination;
}


function bestSumDP(targetSum, numbers, memo = {}) {
    if(targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;

    let shortestCombination = null;

    for (let num of numbers) {
        let remainder = targetSum - num;
        let newCombination = bestSumDP(remainder, numbers, memo);
        if (newCombination !== null) {
            let possibleCombination = [...newCombination, num];
            if (shortestCombination === null || possibleCombination.length < shortestCombination.length) {
                shortestCombination = possibleCombination;
            }
        }
    }

    memo[targetSum] = shortestCombination;
    return shortestCombination;
}

console.log(bestSumDP(8, [1, 4, 5]));
console.log(bestSumDP(5, [3, 3]));
console.log(bestSumDP(100, [1, 2, 5, 25]));