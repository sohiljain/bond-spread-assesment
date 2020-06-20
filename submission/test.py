import unittest
import json
from submission.main import process

class MyTestCase(unittest.TestCase):
    def test_1(self):
        input_file = 'test_files/sample_input.json'
        output_file = 'test_files/sample_output.json'
        # Reading file into a json dictionary
        with open(input_file) as f:
            in_data = json.load(f)

        with open(output_file) as f:
            out_data = json.load(f)

        json_object = process(in_data)

        print(json_object)
        self.assertEqual(sorted(out_data.items()) == sorted(json_object.items()), True)

    def test_2(self):
        input_file = 'test_files/sample_input_2.json'
        output_file = 'test_files/sample_output_2.json'
        # Reading file into a json dictionary
        with open(input_file) as f:
            in_data = json.load(f)

        with open(output_file) as f:
            out_data = json.load(f)

        json_object = process(in_data)

        print(json_object)
        self.assertEqual(sorted(out_data.items()) == sorted(json_object.items()), True)

    def test_3(self):
        """
        This test should fail because 'yield' key is missing in one bond
        :return:
        """
        input_file = 'test_files/sample_input_3.json'
        # Reading file into a json dictionary
        with open(input_file) as f:
            in_data = json.load(f)

        try:
            json_object = process(in_data)
        except:
            return True

    def test_4(self):
        input_file = 'test_files/sample_input_4.json'
        output_file = 'test_files/sample_output_4.json'
        # Reading file into a json dictionary
        with open(input_file) as f:
            in_data = json.load(f)

        with open(output_file) as f:
            out_data = json.load(f)

        json_object = process(in_data)

        print(json_object)
        self.assertEqual(sorted(out_data.items()) == sorted(json_object.items()), True)

if __name__ == '__main__':
    unittest.main()
