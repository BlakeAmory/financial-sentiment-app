import gradio as gr
import requests

API_URL = "http://localhost:8000/api"

def analyze_sentiment(message):
    response = requests.post(f"{API_URL}/analyze-sentiment/", json={"text": message})
    if response.status_code == 200:
        data = response.json()
        sentiment = data['sentiment']
        ai_response = data['response']
        
        if sentiment == 'positive':
            sentiment_color = 'green'
        elif sentiment == 'negative':
            sentiment_color = 'red'
        else:
            sentiment_color = 'yellow'
        
        return f"AI: {ai_response}\n\nSentiment: <span style='color:{sentiment_color}'>{sentiment}</span>"
    else:
        return f"Error: {response.text}"

def get_conversation_history():
    response = requests.get(f"{API_URL}/conversation-history/")
    if response.status_code == 200:
        history = response.json()
        return "\n".join([f"User: {msg['user']}\nAI: {msg['ai']}\n" for msg in history])
    else:
        return f"Error: {response.text}"

with gr.Blocks() as demo:
    gr.Markdown("# Financial Sentiment Analysis Chatbot")
    
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="Enter your message")
            clear = gr.Button("Clear")
        
        with gr.Column(scale=1):
            sentiment_display = gr.HTML(label="Sentiment Analysis")
    
    def user(user_message, history):
        return "", history + [[user_message, None]]
    
    def bot(history):
        user_message = history[-1][0]
        bot_response = analyze_sentiment(user_message)
        history[-1][1] = bot_response
        return history
    
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()
