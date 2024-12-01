import unittest
from src.page_generator import generate_page
import os

class TestPageGenerator(unittest.TestCase):
    
    def test_generate_page(self):
        
        def clean_up():
            pattern = "index.html"
            directory = "./tests/testing-data/"
            for filename in os.listdir(directory):
                if filename.startswith(pattern):
                    file_path = os.path.join(directory, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)           
        clean_up()
        
        
        def get_filename():
            pattern = "index.html"
            directory = "./tests/testing-data/"
            for filename in os.listdir(directory):
                if filename.startswith(pattern):
                    return filename        
            return None
        
        
        def normlize_html(html):
            return ' '.join(html.split())

        expected = '''
        <!DOCTYPE html>
        <html>

        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title> This is an h1 heading </title>
            <link href="/index.css" rel="stylesheet">
        </head>

        <body>
            <article>
                <div><h1>This is an h1 heading</h1><p><b> Some bold text</b> :D</p><blockquote>A nice quote</blockquote><h2>An h2 heading</h2><p>Just text</p></div>
            </article>
        </body>

        </html>
        '''
        

        generate_page("./tests/testing-data/test_markdown.md", "./template.html", "./tests/testing-data/")
        actual = ""
        
        file_name = get_filename()
        if file_name is None:
            self.fail("No content files have have been generated")
            
        file_path = os.path.join("./tests/testing-data", file_name)
            
        with open(file_path) as content_file:
            actual = content_file.read()
        
        normlized_actual = normlize_html(actual)
        normlized_expected = normlize_html(expected)
        
        
        self.assertEqual(normlized_actual, normlized_expected)
    