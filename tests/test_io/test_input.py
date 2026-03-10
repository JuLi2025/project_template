import unittest
import pandas as pd
from app.io.input import read_text_from_file, read_data_from_file


class TestInputFunctions(unittest.TestCase):

# тести для read_text_from_file

    def test_read_text_correct(self):
        with open("test.txt", "w", encoding="utf-8") as f:
            f.write("Hello")

        result = read_text_from_file("test.txt")
        self.assertEqual(result, "Hello")

    def test_read_text_empty(self):
        with open("empty.txt", "w", encoding="utf-8") as f:
            f.write("")

        result = read_text_from_file("empty.txt")
        self.assertEqual(result, "")

    def test_read_text_multiline(self):
        with open("multi.txt", "w", encoding="utf-8") as f:
            f.write("Hello\nWorld")

        result = read_text_from_file("multi.txt")
        self.assertEqual(result, "Hello\nWorld")

 # тести для read_data_from_file

    def test_read_csv_correct(self):
        df = pd.DataFrame({"name": ["Anna"], "age": [20]})
        df.to_csv("test.csv", index=False)
        result = read_data_from_file("test.csv")
        self.assertEqual(result.iloc[0]["name"], "Anna")

    def test_read_csv_rows(self):
        df = pd.DataFrame({"name": ["Anna", "Ivan"], "age": [20, 22]})
        df.to_csv("test2.csv", index=False)
        result = read_data_from_file("test2.csv")
        self.assertEqual(len(result), 2)

    def test_read_csv_columns(self):
        df = pd.DataFrame({"name": ["Anna"], "age": [20]})
        df.to_csv("test3.csv", index=False)
        result = read_data_from_file("test3.csv")
        self.assertIn("name", result.columns)

if __name__ == "__main__":
    unittest.main()