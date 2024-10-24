# Arrays in Programming

## Summary Table

| **Array Type**    | **Description**                                             | **Example in Python**                                |
|-------------------|-------------------------------------------------------------|------------------------------------------------------|
| **Static Array**   | Fixed size, cannot grow or shrink after creation            | Use `numpy` or similar library                       |
| **Dynamic Array**  | Size can change dynamically; elements can be added/removed | Python `list`                                        |
| **Jagged Array**   | Array of arrays; each sub-array can have different lengths  | Lists of lists (e.g., `[[1, 2], [3, 4, 5]]`)        |

### Access Time
**O(1)**: Accessing any element in the array takes constant time due to contiguous memory storage, allowing direct address computation using its index.

---

## LeetCode Questions on Arrays

Here’s a curated list of common LeetCode questions involving arrays:

| **Question Title**                               | **Description**                                                                                       |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| **[Two Sum](https://leetcode.com/problems/two-sum/)**                        | Return indices of two numbers that add up to a specific target.                                        |
| **[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)** | Find the maximum profit from stock prices on given days.                                             |
| **[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)**    | Return true if any value appears at least twice in the array.                                       |
| **[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)** | Return an array such that each element is the product of all elements except itself.                 |
| **[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)**          | Find the contiguous subarray with the largest sum.                                                  |
| **[Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)** | Prove that at least one duplicate number exists in an array containing n + 1 integers.               |
| **[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)** | Return an array of the intersection between two arrays.                                              |
| **[Move Zeroes](https://leetcode.com/problems/move-zeroes/)**                   | Move all 0's to the end while maintaining the relative order of non-zero elements.                  |
| **[3Sum](https://leetcode.com/problems/3sum/)**                                  | Find all unique triplets such that their sum is zero.                                               |
| **[Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)** | Find the contiguous non-empty subarray with the largest product.                                     |
| **[Rotate Array](https://leetcode.com/problems/rotate-array/)**                 | Rotate the array to the right by k steps.                                                            |
| **[Valid Anagram](https://leetcode.com/problems/valid-anagram/)**                | Check if one string is an anagram of another.                                                        |
| **[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)** | Return the minimal length of a subarray whose sum is at least target.                                |
| **[Maximum Gap](https://leetcode.com/problems/maximum-gap/)**                   | Return the maximum difference between successive elements in a sorted form of an unsorted array.     |
| **[Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)**   | Return the sum of two integers without using + and - operators.                                       |

---

### Additional Notes on LeetCode Array Questions

| **Question Title**                            | **Key Considerations**                              | **Time Complexity** | **Space Complexity** |
|-----------------------------------------------|----------------------------------------------------|---------------------|----------------------|
| **Two Sum (#1)**                             | Use a hash map for O(1) lookups; handle duplicates | O(N)                | O(N)                 |
| **Best Time to Buy and Sell Stock (#121)**  | Track minimum price; calculate profit dynamically   | O(N)                | O(1)                 |
| **Contains Duplicate (#217)**                | Use a set to track seen numbers; check for duplicates| O(N)                | O(N)                 |

---

## Further Questions

Here are more LeetCode array-related questions worth exploring:

| **Question Number** | **Question Title**                                      |
|---------------------|--------------------------------------------------------|
| 1                   | [Two Sum](https://leetcode.com/problems/two-sum/)     |
| 2                   | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |
| 3                   | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |
| 4                   | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) |
| 5                   | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) |
| 6                   | [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) |
| 7                   | [3Sum](https://leetcode.com/problems/3sum/) |
| 8                   | [Rotate Array](https://leetcode.com/problems/rotate-array/) |
| 9                   | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) |
| 10                  | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) |
| 11                  | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| 12                  | [Maximum Gap](https://leetcode.com/problems/maximum-gap/) |
| 13                  | [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) |
| 14                  | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |
| 15                  | [Single Number](https://leetcode.com/problems/single-number/) |

