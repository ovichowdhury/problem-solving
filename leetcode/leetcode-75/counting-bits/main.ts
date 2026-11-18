function decimalToBinary(n: number): string {
  if (n === 0) return "0";

  let binary = "";

  while (n > 0) {
    const bit = n & 1;
    binary = bit + binary;
    n = n >> 1;
  }

  return binary;
}

function countBits(n: number): number[] {
  const res: number[] = [];
  for (let i = 0; i <= n; i++) {
    const b = decimalToBinary(i);

    let count = 0;

    for (let j = 0; j < b.length; j++) {
      if (b[j] === "1") count++;
    }

    res.push(count);
  }

  return res;
}

function countBitsDP(n: number): number[] {
  const dp: number[] = new Array(n + 1).fill(0);

  for (let i = 1; i <= n; i++) {
    dp[i] = dp[i >> 1] + (i & 1);
  }

  return dp;
}

console.log(countBitsDP(5));
