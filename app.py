from huffman_algo import *

input_file = 'data.txt'
compressed_file = 'compressed_file.bin'
decompressed_file = 'decompressed_file.txt'

compress_file(input_file, compressed_file)
decompress_file(compressed_file, decompressed_file)