import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    print("Downloading NLTK resources (punkt, stopwords)...")
    nltk.download('punkt')
    nltk.download('stopwords')

MOCK_FILE_CONTENT = """
Artificial intelligence (AI) is intelligence—perceiving, synthesizing, and
inferring
information—demonstrated by machines, as opposed to intelligence displayed by
animals and humans. Example tasks in which this is done include speech
recognition,
computer vision, translation between languages, and other complex processes.
"""

def remove_stopwords_from_text(text_content):
    words = word_tokenize(text_content.lower())
    human_words = []
    for word in words:
        if word.isalpha() and word not in stop_words:
            human_words.append(word)
    return human_words, " ".join(human_words)

if __name__ == "__main__":
    passage = MOCK_FILE_CONTENT
    list_of_words, filtered_passage = remove_stopwords_from_text(passage)
    print("--- Original Passage ---")
    print(passage.strip())
    print("\n--- Processed Results ---")
    print(f"Filtered Word List: {list_of_words}")
    print(f"\nFiltered Passage: {filtered_passage}")
