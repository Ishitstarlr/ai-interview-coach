from utils.preprocessor import preprocess

text = input("Enter your interview answer:\n")
cleaned = preprocess(text)

print("\nCleaned Text:")
print(cleaned)
