import heapq
import os
import pickle

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def create_frequency_table(data):
    freq_table = {}
    for char in data:
        freq_table[char] = freq_table.get(char, 0) + 1
    return freq_table

def build_huffman_tree(freq_table):
    heap = [HuffmanNode(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, code='', mapping=None):
    if mapping is None:
        mapping = {}

    if node is not None:
        if node.char is not None:
            mapping[node.char] = code
        build_huffman_codes(node.left, code + '0', mapping)
        build_huffman_codes(node.right, code + '1', mapping)

    return mapping

def compress_file(input_file, output_file):
    if not os.path.exists('bin'):
        # Creating bin folder
        os.makedirs('bin')

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            data = file.read()
            freq_table = create_frequency_table(data)
            huffman_tree = build_huffman_tree(freq_table)
            huffman_codes = build_huffman_codes(huffman_tree)

            # Save the Huffman codes to a file
            with open('bin/'+output_file + '.huffman', 'wb') as code_file:
                pickle.dump(huffman_codes, code_file)

            # Compress the data using Huffman codes
            compressed_data = ''.join(huffman_codes[char] for char in data)

            # Write the compressed data to a binary file
            with open(output_file, 'wb') as compressed_file:
                compressed_file.write(int(compressed_data, 2).to_bytes((len(compressed_data) + 7) // 8, 'big'))

            print(f"File '{input_file}' compressed to '{output_file}'!")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def decompress_file(input_file, output_file):
    try:
        # Read Huffman codes from the file
        with open('bin/'+input_file + '.huffman', 'rb') as code_file:
            huffman_codes = pickle.load(code_file)

        # Read compressed data from the binary file
        with open(input_file, 'rb') as compressed_file:
            compressed_data = bin(int.from_bytes(compressed_file.read(), 'big'))[2:]

        # Decompress the data using Huffman codes
        current_code = ''
        decompressed_data = ''
        for bit in compressed_data:
            current_code += bit
            if current_code in huffman_codes.values():
                char = next(key for key, value in huffman_codes.items() if value == current_code)
                decompressed_data += char
                current_code = ''

        # Write the decompressed data to a file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decompressed_data)

        print(f"File '{input_file}' decompressed to '{output_file}'!")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

