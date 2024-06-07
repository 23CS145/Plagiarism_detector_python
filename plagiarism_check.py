from difflib import SequenceMatcher

def compare_text(text1, text2):
    # Remove spaces and newlines to compare the raw text
    text1 = text1.replace(" ", "").replace("\n", "")
    text2 = text2.replace(" ", "").replace("\n", "")
    
    d = SequenceMatcher(None, text1, text2)
    similarity_ratio = d.ratio()
    similarity_percentage = int(similarity_ratio * 100)
    diff = list(d.get_opcodes())
    return similarity_percentage, diff
