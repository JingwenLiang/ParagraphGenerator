Paragraph generator according to frequency of words
Author: Jingwen Liang
===================================================

## Prerequisites

- Python3, re, random, argparse, os

## Assumptions

- We append a <BOS> token to the start of each paragraph, and a <EOS> token to the end of each paragraph.
- The cutoff length is assumed to be 100.
- If the input P (number of prefix) is too large, an error will be thrown and the generated paragraphs will all be " ".
- The vocabulary dictionary has keys to be all possible prefix, and values to be candidate words shown after the prefix.

## Examples

- Input: An apple.
- code input: <BOS> An apple.<EOS>
- If P=2, vocabulary dictionary is {'<BOS>': ['An'], '<BOS>An': ['apple'], 'Anapple': ['.'], 'apple.':['<EOS>']}
- When counting the unique prefix, the prefix containing '<BOS>' or having '<EOS>' as the next word does not count. So in the previous paragraph, the number of unique prefix is 1.

## Runing the code
```bash
python main.py --dataset 'my/data/directory' --P number_of_prefix --N number_of_paragraphs_to_generate
```
