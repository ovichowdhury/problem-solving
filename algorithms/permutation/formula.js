/**
 * Reading: https://www.mathsisfun.com/combinatorics/combinations-permutations.html
 */

/**
 * Scenario-1
 * n number of elements and n times to pick
 * formula: permutation(n) = n! (factorial)
 */

function factorial(n) {
    return n > 1 ? n * factorial(n-1) : 1; // ex. 5 = 5*4*3*2*1
}

/**
 * Scenario-2
 * n number of elements and r times to pick
 * formula: permutation(n, r) = n!/(n-r)!
 */

function permutation(n, r) {
    return factorial(n) / factorial(n - r);
}



