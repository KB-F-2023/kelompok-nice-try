import tkinter as tk
from tkinter import scrolledtext
import pandas as pd
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import vstack
from nltk.metrics.distance import edit_distance

nltk.download('stopwords')
nltk.download('words')

# Load dictionary
print("Reading dictionary...")
dictionary_input = ""
with open("new_words.txt", "r") as file:
    dictionary_input = file.read()

dictionary_input = dictionary_input.lower()
words_dict = word_tokenize(dictionary_input)
words_dict = list(set(words_dict))
print("Length of dictionary =", len(words_dict))
print("Dictionary ready!!!")

# Preprocess dictionary
stop_words = set(stopwords.words('english'))
words_dict = [
    word for word in words_dict if word not in
    stop_words and word.isalpha()]

# Build word corpus
english_words = set(words.words())
word_corpus = list(english_words.union(set(words_dict)))

# Vectorize words
vectorizer = CountVectorizer().fit(word_corpus)
word_vectors = vectorizer.transform(word_corpus)

# Autocorrect


def autocorrect(word):
    if word in words_dict:
        return "No error!!"
    else:
        # Calculate Levenshtein distance
        lev_distances = [(w, edit_distance(word, w)) for w in words_dict]
        lev_distances = sorted(lev_distances, key=lambda x: x[1])

        # Get words with low Levenshtein distance
        possible_words = [w[0] for w in lev_distances if w[1] <= 2]

        # AI-based approach
        if len(possible_words) == 0:
            # Vectorize input word
            input_vector = vectorizer.transform([word])

            # Calculate cosine similarity
            similarities = cosine_similarity(input_vector, word_vectors)[0]
            similar_words = [(word_corpus[i], similarities[i])
                             for i in range(len(word_corpus))]

            # Sort by similarity and filter possible words
            similar_words = sorted(
                similar_words, key=lambda x: x[1], reverse=True)
            possible_words = [w[0]
                              for w in similar_words[:10]]  # Get top 10 similar words

        result = f"Possible words generated: {len(possible_words)}\n"
        for w in possible_words:
            result += w + "\n"
        return result

# Output in GUI


def show_output():
    word = input_entry.get().strip()
    output_text = autocorrect(word)
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.END, output_text)


window = tk.Tk()
window.title("Autocorrect App")

# Sets the GUI background color
window.configure(bg="#cfe2f3")

# Sets font size
font = ("Arial", 12)

# Create a "Team Nice Try" logo
logo_label = tk.Label(window, text="Tim Nice Try", font=(
    "Arial", 24, "bold"), fg="#2c3e50", bg="#cfe2f3")
logo_label.pack(pady=20)

# Create input text
input_label = tk.Label(window, text="Enter a word:", bg="#cfe2f3", font=font)
input_label.pack()
input_entry = tk.Entry(window, font=font)
input_entry.pack()

# Create a button to display the output
output_button = tk.Button(window, text="Autocorrect",
                          command=show_output, font=font)
output_button.pack(pady=10)

# Creates a scrollbar in text area
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

output_text_area = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, yscrollcommand=scrollbar.set, font=font)
output_text_area.pack(pady=10)

# Linking Scrollbar with Text Area
scrollbar.config(command=output_text_area.yview)

# Running GUI interface
window.mainloop()
