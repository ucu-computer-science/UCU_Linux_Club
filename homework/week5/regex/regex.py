import re

# Function to match a regular expression pattern in a string
def match_pattern(pattern, text):
    """
    Match a regular expression pattern in a given text and return the result.
    """
    matches = re.findall(pattern, text)
    return matches

# Function to find and replace using regular expressions
def find_and_replace(pattern, replacement, text):
    """
    Find and replace all occurrences of a regular expression pattern in a given text with a replacement string.
    """
    replaced_text = re.sub(pattern, replacement, text)
    return replaced_text

# Function to split a string using a regular expression
def split_text(pattern, text):
    """
    Split a text into a list of substrings using a regular expression pattern as the delimiter.
    """
    substrings = re.split(pattern, text)
    return substrings

# Example usage
if __name__ == "__main__":
    # Example text
    sample_text = "Hello, my email is john@example.com and my phone number is 123-456-7890."

    # 1. Matching a pattern
    email_pattern = r'WRITE_HERE'
    email_matches = match_pattern(email_pattern, sample_text)
    print("Email matches:", email_matches)

    # 2. Finding and replacing
    phone_pattern = r'WRITE_HERE'
    replaced_text = find_and_replace(phone_pattern, "XXX-XXX-XXXX", sample_text)
    print("Text after phone number replacement:")
    print(replaced_text)

    # 3. Splitting text
    words_pattern = r'WRITE_HERE'
    word_list = split_text(words_pattern, sample_text)
    print("Words in the text:", word_list)
