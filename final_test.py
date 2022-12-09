text_orig = input("Введіть слово, яке потрібно замінити:\n")
text_replace = input("На яке слово потрібно замінити?\n")

with open("input.txt", "r", encoding="utf-8") as file_input:
    text = file_input.read()

text = text.replace(text_orig, text_replace)

with open("output.txt", "w", encoding="utf-8") as file_output:
    file_output.write(text)
