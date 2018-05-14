# decrypt-vigenere
## Description
Decrypting a Vigènere Cipher using alphabet frequency of English plaintext.

I recovered the plaintext by finding the Vigenere Key. To do so, I first estimated the key length and then evaluated each character of the key using likely characters, based on the assumption that the text was grammatically correct english.

### Estimating the Key Length
To estimate the key length I looked for repeated 'words' within the ciphertext under the assumption that common strings of characters (like "the" or " an ") in the original text would coincide with the same location of the key given a short enough key (2-14 char) and a long enough message (3000+ char).

A search using words of length 3, 4, and 5 revealed that these repeated words occurred at locations separated by factors of 7. With a large enough sample size (~15 words at ~6 repetitions each) it was highly likely that the key length was 7.

### Evaluating the Key
To solve for the key the ciphertext was broken up into 7 separate streams.

For each stream the frequency of letters was observed, and under the assumption that the most common character in grammatically correct English would be a space, an XOR was performed with it and the most common character to determine the appropriate shift. 

If the shifted stream turned out to have characters outside of the valid range, the same method was performed with the next most frequent character. Fortunately, this was never the case. Once this was done the streams were combined to recover the original plaintext.


## Instructions
- run estkeylen.py using Python 3 and note estimated key lengths in text output
- set NUM_STREAMS parameter in evalkey.py according to output
- run evalkey.py using Python 3
- profit???


## Files
**Provided**
- ctext.txt

**Implemented**
- estkeylen.py
- evalkey.py
- texthelper.py

**Generated**
- ptext.txt
- key.txt
