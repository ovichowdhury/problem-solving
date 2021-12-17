/**
 * Given a number n and an array of positive number m[]
 * Can you sum up to n using the elements of m
 * for ex. howSum(7, [2, 4, 5]) = [2, 5]
 * howSum(5, [1, 3]) = null
 */


function howSum(targetSum, numbers, memo = {}) {
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;
    if (targetSum in memo) return memo[targetSum];

    for (let num of numbers) {
        const reminder = targetSum - num;
        const reminderResult = howSum(reminder, numbers, memo);
        if(reminderResult !== null) {
            memo[targetSum] = [...reminderResult, num];
            return memo[targetSum];
        }
    }

    memo[targetSum] = null;
    return memo[targetSum];
}


console.log(howSum(7, [5, 3, 4, 7]));

console.log(howSum(8, [2, 3]));

console.log(howSum(7, [2, 4, 5]));

console.log(howSum(300, [7, 14]));