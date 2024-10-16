from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class SentimentAnalysisView(APIView):
    def post(self, request):
        text = request.data.get('text')
        if not text:
            return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            llm = Ollama(model="llama3.2:3b")
            prompt = PromptTemplate(
                input_variables=["text"],
                template="Analyze the sentiment of the following text and respond with either 'positive', 'negative', or 'neutral': {text}"
            )
            chain = LLMChain(llm=llm, prompt=prompt)
            sentiment = chain.run(text)

            response = llm(f"Respond to this message in the context of financial advice: {text}")

            return Response({
                'sentiment': sentiment.strip(),
                'response': response.strip()
            })
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ConversationHistoryView(APIView):
    def get(self, request):
        # For now, we'll return a mock conversation history
        # In a real application, you would fetch this from a database
        mock_history = [
            {'user': 'What do you think about the current stock market?'},
            {'ai': 'The stock market has been volatile lately...'},
            {'user': 'Should I invest in tech stocks?'},
            {'ai': 'Investing in tech stocks can be risky...'},
        ]
        return Response(mock_history)
