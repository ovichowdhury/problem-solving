/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
  const MIN = -Math.pow(2, 31);
  const MAX = Math.pow(2, 31) - 1;
  const neg = x < 0 ? true : false;
  const xAbs = Math.abs(x);
  let rev = xAbs.toString().split("").reverse().join("");
  rev = neg ? "-" + rev : rev;
  rev = parseInt(rev);
  if (rev >= MIN && rev <= MAX) return rev;
  return 0;
};

console.log(reverse(-65648));
