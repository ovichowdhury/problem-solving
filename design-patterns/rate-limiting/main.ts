class RateLimitedCalculator {
  private tokenBucket: number = 0;
  constructor(capacity: number, refillTime?: number) {
    this.tokenBucket = capacity;
    setInterval(() => (this.tokenBucket = capacity), 1000 * (refillTime ?? 60));
  }
  getSum(a: number, b: number) {
    if (this.tokenBucket > 0) {
      this.tokenBucket -= 1;
      return a + b;
    } else throw new Error("Too many request");
  }
}

(function () {
  const rateCalc = new RateLimitedCalculator(300, 10);
  setInterval(() => {
    try {
      console.log(
        `SUM : ${rateCalc.getSum(Math.random() * 100, Math.random() * 100)}`
      );
    } catch (ex) {
      console.log(`LIMIT: ${(ex as Error).message}`);
    }
  }, 10);
})();
