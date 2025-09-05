// https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75

function predictPartyVictory(senate: string): string {
  const n = senate.length;
  const radiantQueue: number[] = [];
  const direQueue: number[] = [];

  // Initialize the queues with the indices of each party's senators
  for (let i = 0; i < n; i++) {
    if (senate[i] === "R") {
      radiantQueue.push(i);
    } else {
      direQueue.push(i);
    }
  }

  // Simulate the rounds of banning
  while (radiantQueue.length > 0 && direQueue.length > 0) {
    const radiantIndex = radiantQueue.shift()!;
    const direIndex = direQueue.shift()!;

    if (radiantIndex < direIndex) {
      // Radiant senator bans Dire senator
      radiantQueue.push(radiantIndex + n);
    } else {
      // Dire senator bans Radiant senator
      direQueue.push(direIndex + n);
    }
  }

  if (radiantQueue.length > 0) {
    return "Radiant";
  } else {
    return "Dire";
  }
}

// Example usage:
console.log(predictPartyVictory("RD")); // Output: "Radiant"
console.log(predictPartyVictory("RDD")); // Output: "Dire"
console.log(predictPartyVictory("RRDDD")); // Output: "Radiant"
console.log(predictPartyVictory("DDRRR")); // Output: "Dire"
