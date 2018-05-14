"""
Jung S Lee
UID: 112973353
CMSC456-0201
"""

import fractions as fracs

# Get Length of Key
	# Find all repeating "words"
	# Evaluate distance between repeated words
		# for each common word..
			# Get the location of each instance
			# Find distance between each pair of instances
	# Use common denominators of distances as guesses for key length

def main():
	print("\n=== Estimated Key Lengths Using Repeated \'Words\' ===")
	with open('./ctext.txt') as f:
		ctext = f.read()
		for len_word in [3, 4, 5]:
			words_common = find_common_words(msg=ctext, len_words=len_word, threshold=5)
			key_lens = est_key_len(msg=ctext, words=words_common)
			print("= using words of len %d =" % len_word)
			print(key_lens)
			print()


def find_common_words( msg, len_words, threshold ):
	"""
	Returns top occurences of words in a message.
	
	Reads a message in the form of a list and counts all occurrences of words of a 
	specific length. Common words are returned. Words are any substrings of 
	specified length. 

	Parameters
    ----------
	msg : str
		the message bytestream as a string of hexadecimal digits

	len_words : int
		the length of the words being checked

	threshold : int
		minimum number of occurrences to qualify as a common word

	Returns
    -------
	list(str)
		list of the top words
	"""

	words = count_words(msg, 2*len_words)
	words_common = []
	for word in words.keys():
		if words[word] >= threshold:
			words_common.append(word)
	return words_common


def est_key_len( msg, words ):
	"""
	Returns the shared distances found in each of the common words in a message. 

	Parameters
    ----------
	msg : str
		the message stream

	words: list(str)
		list of common words in the stream

	Returns
    -------
	list(int)
		estimated key lengths revealed by the occurrences of each of the common words
	"""

	dists_shared = []
	for word in words:
		word_locs = find_word_locs(msg,word)
		dists = calc_list_dists(word_locs)
		dists_shared.append(int(calc_gcd_of_list(dists)/2))
	return dists_shared


def count_words( msg, len_words ):	
	""" count the number of words of len_words in the input message """
	words = {}
	byteRange = int((len(msg) - len_words + 1)/2)
	for i in range(byteRange):
		word = msg[i*2:i*2+len_words]
		words[word] = words.get(word, 0) + 1
	return words


def find_word_locs( msg, word ):
	""" find all instance locations of the input word in the given msg """
	loc = msg.find(word)
	locs = []
	while loc != -1:
		locs.append(loc)
		loc = msg.find(word, loc+1)
	return locs


def calc_list_dists( nums ):
	""" calculate all combinations of dists between int pairs in a list """
	nums.sort()
	dists = []
	for n in nums:
		for m in nums:
			dists.append(m-n)
	return [x for x in dists if x > 0]


def calc_gcd_of_list( nums ):
	""" calculate the greatest common denominator of a list of ints """
	den_common = nums[0]
	for n in nums: 
		den_common = fracs.gcd(n, den_common)
	return den_common


main()