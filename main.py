import tkinter as tk

def remove_comments(input_text):
    lines = input_text.split('\n')
    output_lines = []

    for line in lines:
        line = line.split('#', 1)[0]
        output_lines.append(line)

    return '\n'.join(output_lines)

def remove_comments_button_click():
    input_text = input_textbox.get("1.0", "end-1c")
    output_text = remove_comments(input_text)
    output_textbox.delete("1.0", "end")
    output_textbox.insert("1.0", output_text)

# GUI 생성
root = tk.Tk()
root.title("주석 삭제 프로그램")

input_label = tk.Label(root, text="주석을 삭제할 코드를 입력하세요:")
input_label.pack()

input_textbox = tk.Text(root, height=10, width=40)
input_textbox.pack()

remove_button = tk.Button(root, text="주석 삭제", command=remove_comments_button_click)
remove_button.pack()

output_label = tk.Label(root, text="주석이 삭제된 코드:")
output_label.pack()

output_textbox = tk.Text(root, height=10, width=40)
output_textbox.pack()

root.mainloop()
