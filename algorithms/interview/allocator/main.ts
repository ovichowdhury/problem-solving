function allocateProductInBags(
  numOfProduct: number,
  numOfBags: number
): number[] {
  const bags = new Array(numOfBags).fill(0);

  const evenProducts = Math.floor(numOfProduct / numOfBags);
  bags.fill(evenProducts, 0, numOfBags);
  const remainder = numOfProduct % numOfBags;

  if (remainder > 0) {
    bags.fill(evenProducts + 1, 0, remainder);
  }

  return bags;
}

console.log(allocateProductInBags(111, 16));
