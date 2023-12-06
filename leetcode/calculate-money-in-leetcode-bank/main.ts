// Problem: https://leetcode.com/problems/calculate-money-in-leetcode-bank/

function totalMoney(n: number): number {
  let lastMonday = 1;
  let sum = lastMonday;
  let counter = lastMonday;
  for (let i = 1; i < n; i++) {
    if (i % 7 === 0) {
      lastMonday++;
      counter = lastMonday;
      sum += counter;
    } else {
      counter++;
      sum += counter;
    }
  }
  return sum;
}

console.log(totalMoney(20));
