"""

import os
from groq import Groq
from flask import Flask, request, render_template

# User input for GROQ API key
GROQ_API_TOKEN = "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"#input("Enter your GROQ API Key: ")
os.environ['GROQ_API_KEY'] = GROQ_API_TOKEN

# Initialize Groq client
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

def llama3_70b(prompt, temperature=0.0, input_print=True):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        model="llama3-70b-8192",
        temperature=temperature,
    )
    return chat_completion.choices[0].message.content

# Prompt template
prompt_template = #Recognize all aspect terms with their corresponding sentiment polarity in the given review delimited by triple quotes. The aspect terms are nouns or phrases appearing in the review that indicate specific aspects or features of the product/service. Determine the sentiment polarity from the options ["positive", "negative", "neutral"]. Answer in the format ["aspect", "sentiment"] without any explanation. If no aspect term exists, then only answer "[]".


# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        prompt_text = prompt_template + "'''" + text + "'''"
        output = llama3_70b(prompt_text)
        return render_template('index.html', output=output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)



"""
import os
import base64
from groq import Groq
from flask import Flask, request, render_template
import matplotlib.pyplot as plt

# User input for GROQ API key
GROQ_API_TOKEN = "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"
os.environ['GROQ_API_KEY'] = GROQ_API_TOKEN

# Initialize Groq client
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

def llama3_70b(prompt, temperature=0.0, input_print=True):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        model="llama3-70b-8192",
        temperature=temperature,
    )
    return chat_completion.choices[0].message.content

# Prompt template
prompt_template = """Recognize all aspect terms with their corresponding sentiment polarity in the given review delimited by triple quotes. The aspect terms are nouns or phrases appearing in the review that indicate specific aspects or features of the product/service. Determine the sentiment polarity from the options ["positive", "negative", "neutral"]. Answer in the format ["aspect", "sentiment"] without any explanation. If no aspect term exists, then only answer "[]".
"""

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        prompt_text = prompt_template + "'''" + text + "'''"
        output = llama3_70b(prompt_text)
        
        # Calculate ratings
        positive_count = output.count('"positive"')
        neutral_count = output.count('"neutral"')
        negative_count = output.count('"negative"')
        
        # Plotting the graph
        labels = ['Positive', 'Neutral', 'Negative']
        counts = [positive_count, neutral_count, negative_count]
        plt.figure(figsize=(8, 6))
        plt.bar(labels, counts, color=['green', 'gray', 'red'])
        plt.title('Sentiment Analysis')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.ylim(0, max(counts) * 1.2)  # Adjust ylim for better visualization
        plt.grid(True)
        
        # Save the plot to a file or buffer if needed
        # plt.savefig('static/sentiment_analysis.png')
        
        # Convert plot to HTML representation
        import io
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
        buf.close()
        
        return render_template('index.html', output=output, plot_url=plot_url)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

