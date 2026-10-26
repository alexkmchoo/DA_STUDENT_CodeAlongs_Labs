#!/usr/bin/env python3
"""Day 5 code-along: Recall & Practice. Run: python3 <file> or ./<file>"""

# ===== 1. Loop + Conditional + Function, Together =====
# Count how many scores pass a threshold of 70. Here the answer is 3.
print('----- 1. Loop + Conditional + Function, Together -----')
# TODO: define count_passing(scores, threshold)
# TODO: return how many scores are >= threshold

def count_passing(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1
    return count
print(count_passing([55, 82, 91, 40, 76], 70))

# TODO: call it with [55, 82, 91, 40, 76] and 70; print the result

