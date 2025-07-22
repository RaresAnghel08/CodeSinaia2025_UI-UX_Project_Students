import tkinter as tk
from chatbot.probability import get_response
from ux.alerts import empty_message_alert, clear_success_alert
def send_message(entry, chat_log):
    
    if not entry.get():
        empty_message_alert()
        return

    user_message = None
    
    #TODO: get entry's text in the user_message variable 
    
    #TODO: if user_message is blank, empty_message_alert


    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_message.strip()}\n")
    
    #TODO: get response for the user message as the bot_response
    bot_response = None
    
    chat_log.insert(tk.END, f"Bot: {bot_response}\n\n")
    
    chat_log.see("end")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)
    
def clear_chat(chat_log):
    chat_log.config(state=tk.NORMAL)
    chat_log.delete('1.0', tk.END)
    chat_log.config(state=tk.DISABLED)
    
    #TODO: alert for succesful clear
    
