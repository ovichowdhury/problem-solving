function isDivisible(prefix: string, str: string): boolean {
  // checking the length is divisible or not
  if (str.length % prefix.length !== 0) return false;
  let start = 0;
  let end = prefix.length;
  while (end <= str.length) {
    const subStr = str.substring(start, end);
    if (prefix !== subStr) return false;
    start += prefix.length;
    end += prefix.length;
  }
  return true;
}

function gcdOfStrings(str1: string, str2: string): string {
  let gcd = "";
  const minLenStr = str1.length < str2.length ? str1 : str2;
  for (let i = 0; i < minLenStr.length; i++) {
    const prefix = minLenStr.substring(0, i + 1);
    if (isDivisible(prefix, str1) && isDivisible(prefix, str2)) gcd = prefix;
  }

  return gcd;
}

console.log(gcdOfStrings("LEET", "CODE"));
