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
var longestPalindrome = function (s) {
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

console.log(
  longestPalindrome(
    "anugnxshgonmqydttcvmtsoaprxnhpmpovdolbidqiyqubirkvhwppcdyeouvgedccipsvnobrccbndzjdbgxkzdbcjsjjovnhpnbkurxqfupiprpbiwqdnwaqvjbqoaqzkqgdxkfczdkznqxvupdmnyiidqpnbvgjraszbvvztpapxmomnghfaywkzlrupvjpcvascgvstqmvuveiiixjmdofdwyvhgkydrnfuojhzulhobyhtsxmcovwmamjwljioevhafdlpjpmqstguqhrhvsdvinphejfbdvrvabthpyyphyqharjvzriosrdnwmaxtgriivdqlmugtagvsoylqfwhjpmjxcysfujdvcqovxabjdbvyvembfpahvyoybdhweikcgnzrdqlzusgoobysfmlzifwjzlazuepimhbgkrfimmemhayxeqxynewcnynmgyjcwrpqnayvxoebgyjusppfpsfeonfwnbsdonucaipoafavmlrrlplnnbsaghbawooabsjndqnvruuwvllpvvhuepmqtprgktnwxmflmmbifbbsfthbeafseqrgwnwjxkkcqgbucwusjdipxuekanzwimuizqynaxrvicyzjhulqjshtsqswehnozehmbsdmacciflcgsrlyhjukpvosptmsjfteoimtewkrivdllqiotvtrubgkfcacvgqzxjmhmmqlikrtfrurltgtcreafcgisjpvasiwmhcofqkcteudgjoqqmtucnwcocsoiqtfuoazxdayricnmwcg"
  )
);
