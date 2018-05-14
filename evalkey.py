"""
Jung S. Lee
UID: 112973353
CMSC456-0201
"""
import texthelper as th

# Find estimated number of streams using estkeylen.py
# For each of the streams..
	# Shift entire stream so most frequent character is a space
	# Check that all characters are either printable or newline
	# If any are not, assume the next most frequent character is a space and try again

NUM_STREAMS = 7
KEY = []

def main():
	with open('./ctext.txt') as fin:
		ctext = fin.read()
		ctext = th.hex_to_nums(ctext)
		streams = split_streams(ctext)
		streams_shifted = shift_streams(streams)
		ptext = clean_streams(streams_shifted)
	with open('./ptext.txt', 'w') as fout:
		fout.write(ptext)
	with open('./key.txt', 'w') as fout:
		text_key = 'key_length: %d\n' % NUM_STREAMS
		key_hex = ''.join(th.nums_to_hex(KEY))
		text_key += 'key: 0x%s\n' % key_hex
		fout.write(text_key)
	

def split_streams( msg, num_streams=NUM_STREAMS ):
	""" splits the msg into distinct streams based on estimated key length """
	streams = []
	for i in range(num_streams):
		pos = i
		stream = []
		while pos < len(msg):
			stream.append(msg[pos])
			pos += num_streams
		streams.append(stream)
	return streams


def shift_streams( streams ):
	""" shifts all streams in the input list of streams """
	streams_shifted = []
	for stream in streams:
		freq_char = __get_freq_char(stream)
		stream_shifted = __shift_stream(stream, freq_char)
		streams_shifted.append(stream_shifted)
	return streams_shifted


def clean_streams( streams ):
	""" converts streams into their ascii characters and outputs original msg """
	num_streams = len(streams)
	len_msg = sum([len(s) for s in streams])
	msg = [' '] * len_msg

	for i in range(num_streams):
		stream = streams[i]
		for j in range(len(stream)):
			c = stream[j]
			msg[j*num_streams + i] = chr(c)
	return ''.join(msg)


def __get_freq_char( stream, ignorable=[] ):
	""" returns the most freq char in the stream, that are not in ignorable """
	stream_counts = __count_stream_chars(stream)
	max_char = max(stream_counts, key=stream_counts.get)
	return max_char


def __shift_stream( stream, initial, target=32 ):
	""" shifts bytes in list stream so chr: initial becomes chr: target """
	shift = initial ^ target
	KEY.append(shift)
	stream_shifted = stream[:]
	for i in range(len(stream)):
		stream_shifted[i] = stream[i] ^ shift
	return stream_shifted


def __count_stream_chars( stream ):	
	""" count the number of character occurrences in the input stream """
	char_counts = {}
	for c in stream:
		char_counts[c] = char_counts.get(c,0) + 1
	return char_counts


main()

