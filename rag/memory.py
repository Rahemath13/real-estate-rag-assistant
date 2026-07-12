"""
memory.py

Conversation history manager.
"""

from langchain_core.chat_history import InMemoryChatMessageHistory


class ConversationMemory:

    def __init__(self):
        self.memory = InMemoryChatMessageHistory()

    def add_user(self, text):
        self.memory.add_user_message(text)

    def add_ai(self, text):
        self.memory.add_ai_message(text)

    def get_messages(self):
        return self.memory.messages

    def clear(self):
        self.memory.clear()