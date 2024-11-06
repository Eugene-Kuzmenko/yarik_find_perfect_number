import sys
from tkinter import Tk, ttk, E, W, S, N, IntVar, StringVar
from find_dividers import find_dividers

def find_perfect_number(max_number):
  return (number for number in range(max_number + 1) if number == sum(find_dividers(number)))

def format_result(max_number, perfect_numbers):
  return f"perfect numbers lesser than {max_number} are {", ".join(str(number) for number in perfect_numbers)}"

if __name__ == "__main__":
  window = Tk(className="Find perfect numbers")

  max_number_store = IntVar(window, 0)
  result_text_store = StringVar(window, "")

  def handle_find_button():
    max_number = int(max_number_store.get())
    result = list(find_perfect_number(max_number))

    result_text_store.set(format_result(max_number, result))
 
  content = ttk.Frame(window, padding=5)
  content.grid(sticky=E + W + S + N)

  max_input_labelframe = ttk.LabelFrame(content, text="Insert max number")
  max_input_labelframe.grid(column=0, row=0, columnspan=2,  sticky="nsew")

  max_number_input = ttk.Entry(max_input_labelframe, textvariable=max_number_store)
  max_number_input.pack(fill="both", expand=True, padx=8, pady=5)
  
  result_label = ttk.Label(content, padding=2, textvariable=result_text_store)
  result_label.grid(column=0, row=1)


  find_button = ttk.Button(content, text="Find", command=handle_find_button)
  find_button.grid(column=1, row=2, sticky=E)

  window.mainloop()