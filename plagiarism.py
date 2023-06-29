import difflib
def check_plagiarism(text1, text2):
    
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    similarity = difflib.SequenceMatcher(None, lines1, lines2).ratio()
    return similarity
print("enter text 1:")
text1 = input("")
print("enter text 2:")
text2 = input("")

similarity_ratio = check_plagiarism(text1, text2)
print(f"Similarity ratio: {similarity_ratio}")