from streamlit import *
import re 

def get_words_from_text(text):
    text = re.sub(r'[^\w\s]', '', text) 
    text = re.sub(r'\d+', '', text)
    return text.lower().split()


def count_freq_and_classify_streamlit(words):
   
    hc = ['healthcare', 'hospital', 'medical', 'patient', 'doctor', 'nurse', 'clinic', 'medicine', 'health']
    fn = ['financial', 'finance', 'bank', 'investment', 'money', 'economy', 'market', 'stocks', 'fund']
    tech = ['technology', 'software', 'digital', 'ai', 'artificial intelligence', 'code', 'cybersecurity', 'innovation', 'tech', 'data']
    edu = ['education', 'school', 'university', 'college', 'student', 'learning', 'academic', 'classroom', 'professor']
    trvl = ['travel', 'holiday', 'vacation', 'trip', 'destination', 'explore', 'tourism', 'journey', 'airport']

    word_freq = {}
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    words_lower = [w.lower() for w in words] 

    subheader("Detected Categories:")
    categories_found = False

    if any(keyword in words_lower for keyword in hc):
        success("✅ **Health Care**")
        categories_found = True
    if any(keyword in words_lower for keyword in fn):
        success("✅ **Financial**")
        categories_found = True
    if any(keyword in words_lower for keyword in tech):
        success("✅ **Technology**")
        categories_found = True
    if any(keyword in words_lower for keyword in edu):
        success("✅ **Education**")
        categories_found = True
    if any(keyword in words_lower for keyword in trvl):
        success("✅ **Travel**")
        categories_found = True

    if not categories_found:
        info("🤷‍♂️ No predefined category keywords found in the text.")

    subheader("Word Frequencies:")
   
    if word_freq:
        
        import pandas as pd
        freq_df = pd.DataFrame(list(word_freq.items()), columns=['Word', 'Frequency']).sort_values(by='Frequency', ascending=False)
        table(freq_df)
    else:
        info("No words processed or frequencies found.")


def main():
    set_page_config(
        page_title="Text Classifier",
        page_icon="🏷️",
        layout="centered"
    )

    title("🏷️ Rule-Based Text Classifier")
    markdown("""
        Enter text to see which predefined categories it might belong to,
        based on the presence of specific keywords.
        Multiple categories can be detected if relevant keywords are present.
    """)

    user_text = text_area(
        "Paste or type your text here:",
        height=200,
        placeholder="E.g., The latest medical research on patient care needs significant financial investment from tech companies."
    )

    if button("Classify Text"):
        if not user_text.strip():
            warning("Please enter some text to classify.")
            return

        with spinner('Analyzing text...'):
            words = get_words_from_text(user_text)
            count_freq_and_classify_streamlit(words)

    markdown("---")
    write("This classifier uses a simple keyword-matching approach.")

if __name__ == "__main__":
    main()