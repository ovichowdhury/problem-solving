//leetcode.com/problems/palindrome-number/

function isPalindrome(x: number): boolean {
  if (x < 0) return false;
  const org = x;
  let rev = 0;
  while (x > 0) {
    const mod = x % 10;
    rev = rev * 10 + mod;
    x = Math.floor(x / 10);
  }

  return rev == org;
}

// Test cases
console.log(isPalindrome(121)); // true
console.log(isPalindrome(-121)); // false
console.log(isPalindrome(10)); // false
console.log(isPalindrome(12321)); // true
console.log(isPalindrome(0)); // true
