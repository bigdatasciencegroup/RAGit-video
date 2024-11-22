from langchain.prompts import PromptTemplate

question_prompt_template = """ 
You are an artificial intelligence designed to answer questions about the content of a video.
This is a transcript of the video:
---
TRANSCRIPT: {context}
--- 

Using the content of the transcript above, answer the following question.
If the question is complex, answer it step by step:

QUESTION: {question}

ANSWER:
"""

question_prompt = PromptTemplate(
    template=question_prompt_template,
    input_variables=['question', 'context']
)


fill_punctuation_template = """
You are an expert in transcribing videos. Your task is to edit video transcriptions that lack punctuation or capitalization 
and return the same transcription with correct punctuation, commas, and capitalization.

Example:

Input:

today we are going to talk about the importance of punctuation in writing

Output:

Today, we are going to talk about the importance of punctuation in writing.

Instructions:

Analyze the input:

- Identify the words, phrases, and sentences in the transcription.
- Recognize the different types of words (nouns, verbs, adjectives, etc.).
- Detect the sentence structure (subject, verb, object).

Predict punctuation:

- Comma (,): Separates elements within a sentence.
- Period (.): Indicates the end of a sentence.
- Semicolon (;): Separates two independent but related sentences.
- Ellipsis (...): Indicates that the sentence is incomplete or information is omitted.
- Question mark (?): Indicates a question.
- Exclamation mark (!): Indicates surprise, emphasis, or emotion.

Predict capitalization:

- First letter of the sentence: Must be capitalized.
- Proper nouns: Must start with a capital letter.
- Titles and roles: Must start with a capital letter.

Consider the context:

- The style of punctuation may vary depending on the context and type of text.
- It is important to be consistent with punctuation throughout the transcription.
- Correct punctuation can improve readability and comprehension.

Input: {raw_transcription}

Output:
"""

fill_punctuation_prompt = PromptTemplate(
    template=fill_punctuation_template,
    input_variables=["raw_transcription"]
)
