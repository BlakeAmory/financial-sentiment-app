from django.urls import path
from .views import SentimentAnalysisView, ConversationHistoryView

urlpatterns = [
    path('analyze-sentiment/', SentimentAnalysisView.as_view(), name='analyze_sentiment'),
    path('conversation-history/', ConversationHistoryView.as_view(), name='conversation_history'),
]
