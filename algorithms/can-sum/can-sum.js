/**
 * Given a number n and an array of positive number m[]
 * Can you sum up to n using the elements of m
 * for ex. canSum(7, [2, 4, 5]) = true
 * canSum(5, [1, 3]) = false
 */

// recursive brute force
function canSum(targetSum, numbers) {
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;

    for (let num of numbers) {
        const reminder = targetSum - num;
        if (canSum(reminder, numbers)) return true;
    }

    return false;
}

// recursive DP memoization
function canSumDP(targetSum, numbers, memo = {}) {
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;
    if (targetSum in memo) return memo[targetSum];

    for (let num of numbers) {
        const reminder = targetSum - num;
        if (canSumDP(reminder, numbers, memo)) {
            memo[targetSum] = true;
            return memo[targetSum];
        }
    }

    memo[targetSum] = false;
    return memo[targetSum];
}




console.log(canSum(7, [2, 3]));

console.log(canSumDP(3000, [7, 14]));