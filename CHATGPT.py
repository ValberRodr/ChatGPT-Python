import tkinter as tk
from tkinter import filedialog, ttk
import requests
prompt = ""
result = ""

def generate_text(prompt, api_key, objective):
    headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {api_key}"
    }
    model = 'text-davinci-003'
    url = "https://api.openai.com/v1/completions"
        #Corpo
    corpo = {
        "prompt": prompt,
        "max_tokens": 1000,
        "n": 1, 
        "stop": None, 
        #"temperature": 1,
        'model': model
    }
    
    response = requests.post(url, headers=headers, json=corpo)
    if response.status_code == 200:
        response_json = response.json()
        return response_json["choices"][0]["text"]
    else:
        return "An error occurred while generating text."

def send_message(api_key, objective):
    global prompt
    global result
    prompt1 = user_input.get()
    prompt = "Voce disse: " + str(result) + "; " + str(prompt1)
    if prompt:
        result = generate_text(prompt, api_key, objective)
        chat_history.config(state='normal')
        chat_history.insert("end", "Você: ", ("red_tag",))
        chat_history.insert("end", prompt1 + "\n", ("red_text",))
        chat_history.insert("end", "Will: ", ("blue_tag",))
        chat_history.insert("end", result + "\n", ("blue_text",))
        chat_history.config(state='disabled')
        user_input.delete(0, "end")

root = tk.Tk()
root.title("Pergunte ao GPT")
root.geometry("600x700")

#chat_history.config(font=("Arial", 12))
chat_history = tk.Text(root, bg='white', height=28, width=40)
chat_history.pack(side="top", fill="both", pady=10)
chat_history.config(state='disabled', font=("Arial", 12))

chat_history.tag_configure("red_tag", foreground="#ff0000")
chat_history.tag_configure("red_text", foreground="#ff0000")
chat_history.tag_configure("blue_tag", foreground="#0000ff")
chat_history.tag_configure("blue_text", foreground="#0000ff")

frame = tk.Frame(root)
frame.pack()

user_input = tk.Entry(frame, bg='white', width=65)
user_input.pack(side="left", padx=5)

send_button = tk.Button(frame, text="Send", command=lambda: send_message(api_key.get(), objective.get()))
send_button.pack(side="left", padx=5)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

api_key_label = tk.Label(frame2, text="API Key:")
api_key_label.pack(side="left")

api_key = tk.Entry(frame2, width=50)
api_key.pack(side="left")

frame3 = tk.Frame(root)
frame3.pack(pady=10)

objective_label = tk.Label(frame3, text="Objetividade vs Criatividade:")
objective_label.pack(side="left")

objective = ttk.Combobox(frame3, values=[0.5, 0.7, 0.9, 1.0], width=50)
objective.current(3) # seta o item selecionado para o valor padrão 1.0
objective.pack(side="left")

root.mainloop()
