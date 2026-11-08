import unittest,tempfile,json
from pathlib import Path
from core import run

class Tests(unittest.TestCase):
 def test_feed(self):self.assertEqual(len(run(json.loads(Path('example.json').read_text()))['items']),1)
 def test_empty(self):self.assertEqual(run({})['items'],[])
 def test_bad(self):
  with self.assertRaises(TypeError):run({'xml':3})
 def test_entity_block(self):
  with self.assertRaises(Exception):run({'xml':'<!DOCTYPE x [<!ENTITY y SYSTEM "file:///etc/passwd">]><rss>&y;</rss>'})

if __name__=="__main__":unittest.main()
