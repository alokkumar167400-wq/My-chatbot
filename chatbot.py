# complete_chatbot.py
import tkinter as tk
from tkinter import scrolledtext
import datetime
import random

class SimpleChatbot:
    def __init__(self):
        self.name = "ChatBot"
        self.responses = {
            'greetings': [
                "Namaste! Kaise ho aap?",
                "Hello! Aap sunaiye",
                "Hi! Kya haal chaal?",
                "Pranam! Aapka swagat hai"
            ],
            'farewell': [
                "Alvida! Phir milenge",
                "Bye bye! Accha rahe",
                "Khuda hafiz! Aapse baat karke accha laga",
                "Shubh ratri! Sweet dreams"
            ],
            'thanks': [
                "Koi baat nahi!",
                "Happy to help!",
                "Aapka swagat hai!",
                "Mujhe aapki madad karke khushi hui"
            ],
            'jokes': [
                "Kyun computer teacher ne students ko punish kiya? Because they didn't do their Java homework!",
                "Main ek funny chatbot hoon, lekin mere jokes byte-size hote hain!",
                "Kyun programmer fridge nahi khol paaya? Because he lost the fridge door handle exception!",
                "Kyun computer kabhi bimaar nahi hota? Because it has too many bytes!"
            ],
            'questions': [
                "Aap mujhse kuch aur puchna chahte hain?",
                "Kya main aapki koi aur madad kar sakta hoon?",
                "Aur bataiye, main aapke liye kya kar sakta hoon?"
            ]
        }
    
    def get_time(self):
        return datetime.datetime.now().strftime("%H:%M")
    
    def get_date(self):
        return datetime.datetime.now().strftime("%d-%m-%Y")
    
    def generate_response(self, user_input):
        user_input = user_input.lower()
        
        # Greetings
        if any(word in user_input for word in ['hello', 'hi', 'namaste', 'hey', 'hola', 'pranam']):
            return random.choice(self.responses['greetings'])
        
        # Farewell
        elif any(word in user_input for word in ['bye', 'exit', 'quit', 'alvida', 'goodbye']):
            return random.choice(self.responses['farewell'])
        
        # Time
        elif 'time' in user_input or 'samay' in user_input or 'kitne baje' in user_input:
            return f"🕒 Abhi samay hai: {self.get_time()}"
        
        # Date
        elif 'date' in user_input or 'tareekh' in user_input or 'aaj kitni tarikh' in user_input:
            return f"📅 Aaj ki tareekh hai: {self.get_date()}"
        
        # Thanks
        elif any(word in user_input for word in ['thanks', 'thank you', 'dhanyavad', 'shukriya']):
            return random.choice(self.responses['thanks'])
        
        # Name
        elif 'tumhara naam' in user_input or 'your name' in user_input or 'naam' in user_input:
            return f"🤖 Mera naam {self.name} hai!"
        
        # Jokes
        elif 'joke' in user_input or 'hasao' in user_input or 'funny' in user_input or 'mazak' in user_input:
            return f"😄 {random.choice(self.responses['jokes'])}"
        
        # How are you
        elif 'kaise ho' in user_input or 'how are you' in user_input:
            return "Main toh ek chatbot hoon, always ready to help! Aap kaise ho?"
        
        # Help
        elif 'help' in user_input or 'madad' in user_input or 'sahayata' in user_input:
            help_text = "🆘 Main in cheezein bata sakta hoon:\n"
            help_text += "• Time/Date\n• Greetings\n• Jokes\n• Thanks\n• Farewell\n"
            help_text += "• Aapka naam\n• How are you"
            return help_text
        
        # Default response with follow-up
        else:
            return f"🤔 Mujhe samjha nahi, kya aap dobara puch sakte hain?\n{random.choice(self.responses['questions'])}"

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Simple Chatbot")
        self.root.geometry("500x650")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(True, True)
        
        self.chatbot = SimpleChatbot()
        self.setup_gui()
    
    def setup_gui(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(padx=15, pady=15, fill='both', expand=True)
        
        # Title
        title_label = tk.Label(main_frame, text="🤖 Simple Chatbot", 
                              font=("Arial", 18, "bold"), bg='#2c3e50', fg='white')
        title_label.pack(pady=10)
        
        # Chat display area with better styling
        self.chat_display = scrolledtext.ScrolledText(
            main_frame, 
            width=55, 
            height=22, 
            font=("Arial", 11),
            wrap=tk.WORD,
            bg='#ecf0f1',
            fg='#2c3e50',
            relief=tk.FLAT,
            bd=3,
            padx=10,
            pady=10
        )
        self.chat_display.pack(pady=10, padx=5, fill='both', expand=True)
        self.chat_display.config(state='disabled')
        
        # Configure tags for different message types
        self.chat_display.tag_config('user', foreground='#2980b9', font=("Arial", 11, "bold"))
        self.chat_display.tag_config('bot', foreground='#27ae60', font=("Arial", 11))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#2c3e50')
        input_frame.pack(pady=10, fill='x')
        
        # Input field with placeholder
        self.user_input = tk.Entry(
            input_frame, 
            font=("Arial", 12), 
            bg='white', 
            fg='#2c3e50',
            relief=tk.FLAT,
            bd=2,
            insertbackground='#2c3e50'
        )
        self.user_input.pack(side='left', padx=5, fill='x', expand=True)
        self.user_input.bind('<Return>', self.send_message)
        
        # Send button with better styling
        send_btn = tk.Button(
            input_frame, 
            text="📤 Send", 
            command=self.send_message,
            bg='#3498db',
            fg='white',
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=5,
            cursor='hand2'
        )
        send_btn.pack(side='right', padx=5)
        
        # Welcome message
        self.add_message("Chatbot", "Namaste! 👋 Main ek simple chatbot hoon. Aap mujhse baat kar sakte hain!\nType 'help' for assistance.")
        
        # Focus on input field
        self.user_input.focus()
    
    def add_message(self, sender, message):
        self.chat_display.config(state='normal')
        
        if sender == "You":
            self.chat_display.insert(tk.END, f"You: {message}\n\n", 'user')
        else:
            self.chat_display.insert(tk.END, f"Chatbot: {message}\n\n", 'bot')
        
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)
    
    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        
        if user_text:
            self.add_message("You", user_text)
            self.user_input.delete(0, tk.END)
            
            # Simulate typing delay
            self.root.after(500, lambda: self.process_response(user_text))
    
    def process_response(self, user_text):
        response = self.chatbot.generate_response(user_text)
        self.add_message("Chatbot", response)
        
        # Check for exit command
        if any(word in user_text.lower() for word in ['bye', 'exit', 'quit', 'alvida']):
            self.root.after(2000, self.root.quit)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()