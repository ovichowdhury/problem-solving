// problem: https://leetcode.com/problems/longest-palindromic-substring/

var isPalindrome = function (s) {
  const reverseString = s.split("").reverse().join("");
  if (s === reverseString) return true;
  return false;
};

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindromeN3Complexity = function (s) {
  let longest = "";
  if (s.length === 1) return s;
  for (let i = 0; i < s.length - 1; i++) {
    for (let j = i + 1; j <= s.length; j++) {
      const subStr = s.substring(i, j);
      if (isPalindrome(subStr) && subStr.length >= longest.length)
        longest = subStr;
    }
  }
  return longest;
};

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function (s) {
  let res = "";
  let resLen = 0;
  for (let i = 0; i < s.length; i++) {
    /**
     * Checking the odd string from middle
     */
    let l = i;
    let r = i;
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      if (r - l + 1 > resLen) {
        res = s.substring(l, r + 1);
        resLen = r - l + 1;
      }
      l--;
      r++;
    }

    /**
     * Checking the even string
     */
    l = i;
    r = i + 1;
    while (l >= 0 && r < s.length && s[l] === s[r]) {
      if (r - l + 1 > resLen) {
        res = s.substring(l, r + 1);
        resLen = r - l + 1;
      }
      l--;
      r++;
    }
  }
  return res;
};

console.log(
  longestPalindrome(
    "anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"
  )
);

// console.log(longestPalindrome("babad"));
