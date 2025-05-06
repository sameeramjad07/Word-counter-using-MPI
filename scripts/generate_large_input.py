import os
import google.generativeai as genai

def generate_text_with_gemini(prompt, max_tokens=1000):
    """Generate text using Gemini API."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=0.7
            )
        )
        return response.text
    except Exception as e:
        print(f"Error generating text: {e}")
        return ""

def generate_large_text(filename, size_mb=1):
    """Generate a large text file using Gemini API."""
    target_size = size_mb * 1024 * 1024  # Convert MB to bytes
    current_size = 0
    topics = [
        "Write a detailed article about recent advancements in artificial intelligence.",
        "Compose a short story set in a futuristic city.",
        "Explain the science behind climate change in an engaging way.",
        "Describe the history of classical literature.",
        "Write a technical overview of quantum computing."
    ]

    with open(filename, 'w', encoding='utf-8') as f:
        topic_index = 0
        while current_size < target_size:
            prompt = topics[topic_index % len(topics)]
            text = generate_text_with_gemini(prompt)
            if text:
                f.write(text + "\n\n")
                current_size += len(text.encode('utf-8'))
            topic_index += 1

if __name__ == '__main__':
    generate_large_text('data/large_input.txt', size_mb=1)