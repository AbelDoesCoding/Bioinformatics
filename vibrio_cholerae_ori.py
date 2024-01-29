ori="ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            count = count + 1
    return count

def FrequencyMap(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = 0
    for i in freq:
        count = 0
        freq[i] = PatternCount(text, i) 
        count += 1
    return freq

def FrequentWords(text, k):
    words = []
    freq = FrequencyMap(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
    return words

def ReverseComplement(pattern):
    pattern = Reverse(pattern)
    pattern = Complement(pattern)
    return pattern

def Reverse(pattern):
    revString = ""
    for i in pattern:
        revString = i + revString
    return revString

def Complement(pattern):
    complementPattern = ""
    for i in pattern:
        if i == "A":
            complementPattern = complementPattern + "T"
        elif i == "C":
            complementPattern = complementPattern + "G"
        elif i == "G":
            complementPattern = complementPattern + "C"
        elif i == "T":
            complementPattern = complementPattern + "A"
    return complementPattern

test = "TGCA"
gup = Complement(test)
print(gup)


