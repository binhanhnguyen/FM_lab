# TODO: [part d]
# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

import argparse
import utils

def main():
    accuracy = 0.0

    # Compute accuracy in the range [0.0, 100.0]
    ### YOUR CODE HERE ###
    total = 0
    correct = 0
    with open('birth_dev.tsv', encoding='utf-8') as f:
        for line in f:
            total += 1
            parts = line.strip().split('\t')
            if len(parts) > 1 and parts[1] == "London":
                correct += 1
    
    if total > 0:
        accuracy = (correct / total) * 100.0
    else:
        accuracy = 0.0
    ### END YOUR CODE ###
    print(accuracy)
    return accuracy

if __name__ == '__main__':
    accuracy = main()
    with open("london_baseline_accuracy.txt", "w", encoding="utf-8") as f:
        f.write(f"{accuracy}\n")
