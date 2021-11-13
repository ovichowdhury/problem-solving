

function permute(str, l, r, pArr) {
    if (l == r) pArr.push(str);
    else {
        for (let i = l; i <= r; i++) {
            str = swap(str, l, i);
            permute(str, l + 1, r, pArr);
            str = swap(str, l, i);
        }
    }
}

function swap(str, l, r) {
    const charArr = str.split("");
    if (l >= 0 && r < charArr.length) {
        const temp = charArr[l];
        charArr[l] = charArr[r];
        charArr[r] = temp;
        return charArr.join("");
    }
    throw new Error("Swap out of index");
}

let s = "ABC";
let arr = []
permute(s, 0, s.length-1, arr);

console.log(arr);