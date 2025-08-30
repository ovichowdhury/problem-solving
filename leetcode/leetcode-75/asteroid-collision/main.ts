// https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

function asteroidCollision(asteroids: number[]): number[] {
  if (asteroids.length === 0) return [];
  const stack = [asteroids[0]];

  for (let i = 1; i < asteroids.length; i++) {
    stack.push(asteroids[i]);
    let j = stack.length;
    while (j > 0) {
      if (stack[j] > 0 && stack[j - 1] > 0) {
        --j;
        continue;
      }
      if (stack[j] < 0 && stack[j - 1] < 0) {
        --j;
        continue;
      }
      if (stack[j] > 0 && stack[j - 1] < 0) {
        --j;
        continue;
      }
      if (stack[j] < 0 && stack[j - 1] > 0) {
        if (Math.abs(stack[j]) > Math.abs(stack[j - 1])) {
          stack.splice(j - 1, 1);
        } else if (Math.abs(stack[j]) < Math.abs(stack[j - 1])) {
          stack.splice(j, 1);
        } else stack.splice(j - 1, 2);
      }

      --j;
    }
  }
  return stack;
}

// solution 2 and efficient one
function asteroidCollision2(asteroids: number[]): number[] {
  const stack: number[] = [];
  for (const asteroid of asteroids) {
    let alive = true;
    while (
      alive &&
      asteroid < 0 &&
      stack.length > 0 &&
      stack[stack.length - 1] > 0
    ) {
      const top = stack[stack.length - 1];
      if (Math.abs(asteroid) > Math.abs(top)) {
        stack.pop();
        // asteroid survives, keep checking
      } else if (Math.abs(asteroid) === Math.abs(top)) {
        stack.pop();
        alive = false; // both destroyed
      } else {
        alive = false; // asteroid destroyed
      }
    }
    if (alive) {
      stack.push(asteroid);
    }
  }
  return stack;
}

// example usage
const asteroids = [5, 10, -5];
const result = asteroidCollision2(asteroids);
console.log(result); // Output: [5, 10]

const asteroids2 = [8, -8];
const result2 = asteroidCollision2(asteroids2);
console.log(result2); // Output: []

const asteroids3 = [10, 2, -5];
const result3 = asteroidCollision2(asteroids3);
console.log(result3); // Output: [10]

const asteroids4 = [-2, -2, 1, -2];
const result4 = asteroidCollision2(asteroids4);
console.log(result4); // Output: [-2, -2, -2]
