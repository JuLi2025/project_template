from app.io.input import input_from_console, read_text_from_file, read_data_from_file
from app.io.output import output_to_console, write_to_file

def main():
    console_text = input_from_console()
    file_text = read_text_from_file("data/input.txt")
    pandas_data = read_data_from_file("data/data.csv")

    output_to_console(console_text)
    output_to_console(file_text)
    output_to_console(pandas_data)

    write_to_file("data/output.txt", console_text)
    write_to_file("data/output.txt", file_text)
    write_to_file("data/output.txt", str(pandas_data))

if __name__ == "__main__":
    main()