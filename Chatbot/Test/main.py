import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


class OpenAIChatbot:
    def __init__(self):
        """Initialize the chatbot with OpenAI client."""
        # Get API key from environment variables
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            print("Error: OPENAI_API_KEY not found in environment variables.")
            print("Please make sure you have added your OpenAI API key to the .env file in the Chatbot/Test directory.")
            sys.exit(1)
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"
        
        # Store conversation history
        self.conversation_history = [
            {"role": "system", "content": "You are a helpful assistant. Be concise and friendly."}
        ]
    
    def get_response(self, user_message):
        """Get response from OpenAI API."""
        try:
            # Add user message to conversation history
            self.conversation_history.append({"role": "user", "content": user_message})
            
            # Get response from OpenAI
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                max_tokens=500,
                temperature=0.7
            )
            
            # Extract the assistant's response
            assistant_message = response.choices[0].message.content
            
            # Add assistant response to conversation history
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            
            return assistant_message
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    def chat(self):
        """Start the interactive chat session."""
        print("🤖 OpenAI Chatbot (GPT-4o-mini)")
        print("=" * 40)
        print("Type 'quit', 'exit', or 'bye' to end the conversation.")
        print("Type 'clear' to clear conversation history.")
        print("=" * 40)
        
        while True:
            try:
                # Get user input
                user_input = input("\nYou: ").strip()
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n🤖 Goodbye! Have a great day!")
                    break
                
                # Check for clear command
                if user_input.lower() == 'clear':
                    self.conversation_history = [
                        {"role": "system", "content": "You are a helpful assistant. Be concise and friendly."}
                    ]
                    print("\n🤖 Conversation history cleared!")
                    continue
                
                # Skip empty input
                if not user_input:
                    continue
                
                # Get and display response
                print("\n🤖 Assistant: ", end="")
                response = self.get_response(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print("\n\n🤖 Goodbye! Have a great day!")
                break
            except EOFError:
                print("\n\n🤖 Goodbye! Have a great day!")
                break


def main():
    """Main function to run the chatbot."""
    print("Starting OpenAI Chatbot...")
    
    # Create and start the chatbot
    chatbot = OpenAIChatbot()
    chatbot.chat()


if __name__ == "__main__":
    main()
