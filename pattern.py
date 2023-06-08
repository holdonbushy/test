import re
pattern = r"apple"
text = "I have an apple"
new_text = re.sub(pattern, "orange", text)
print("替换后的文本:", new_text)
