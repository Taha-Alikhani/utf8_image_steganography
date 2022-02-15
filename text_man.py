def read_file(filename: str) -> list:
    """
    Reads the text file and returns the code as a list of strings.
    """
    f = open(filename, "r", encoding="utf-8")
    code = f.readlines()
    f.close()
    return code

def str_to_bytes(code: list) -> list:
    """
    Converts the string list to bytes.
    """
    bytes_code = []
    for line in code:
        for c in line:
            bytes_code.append(c.encode('utf-8'))
    return bytes_code

def bytes_to_bin(bytes_code: list) -> list:
    """
    Converts the byte list to bits.
    """
    bin_code = []
    for b in bytes_code:
            bits_32 = "{:b}".format(int(b.hex(), 16)).zfill(32)
            bin_code.extend([bits_32[i:i+8] for i in range(0, 32, 8)])
    bin_code.extend(["00000000"]*4) #An extra 4 bits to recognize the end of the file
    return bin_code