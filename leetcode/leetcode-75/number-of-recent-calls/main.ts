// https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

class RecentCounter {
  private queue: number[];

  constructor() {
    this.queue = [];
  }

  ping(t: number): number {
    // Add the new ping time
    this.queue.push(t);

    // Remove all times that are older than (t - 3000)
    while (this.queue[0] < t - 3000) {
      this.queue.shift(); // remove from front
    }

    // The queue length = number of recent calls
    return this.queue.length;
  }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */
