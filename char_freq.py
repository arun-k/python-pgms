def char_frequency(lines):
    frequency = {}
    for line in lines:
        for words in line:
            for char in words:
                frequency[char] = frequency.get(char, 0) + 1
    return frequency

def main(filename):
    f=open(filename,'r')
    frequency = char_frequency(f.readlines())
    for char in sorted(frequency,key=lambda x:frequency[x],reverse=True)[:10]:
        print char, frequency[char]

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
