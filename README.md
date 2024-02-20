# Huffman Encoder

Huffman Encoder is a simple Python implementation of a file compression utility using the Greedy Huffman Encoding algorithm.

## Overview

The Huffman Encoder consists of two main components:
- Compression: Converts a given text file into a compressed binary file using Huffman Encoding.
- Decompression: Reverses the compression process, recovering the original text file from the compressed binary file.

## Features

- File compression using Huffman Encoding.
- File decompression to recover the original file.
- Huffman codes are saved to a separate file for future decompression.

## Usage

### Compression

```bash
python huffman_encoder.py compress input_file.txt compressed_file.bin
```

### Decompression
```bash
python huffman_encoder.py decompress compressed_file.bin decompressed_file.txt
```
- compressed_file.bin: The input compressed binary file.
- decompressed_file.txt: The output decompressed text file.


## Requirements
Python 3.x

## Acknowledgments
This project was inspired by the Huffman Coding algorithm for file compression.
