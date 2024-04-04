function mergeAlternately(word1: string, word2: string): string {
  let mergedString = "";
  const minLenWord = word1.length < word2.length ? word1 : word2;
  const maxLenWord = word1.length > word2.length ? word1 : word2;
  for(let i = 0; i<minLenWord.length; i++) {
    mergedString += word1[i] + word2[i]
  }
  return mergedString + maxLenWord.substring(minLenWord.length);
};

console.log(mergeAlternately("abcd", "pq"))