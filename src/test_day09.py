import unittest

from day09 import *

class TestDay09(unittest.TestCase):
    def testDefault(self):
        input = "2333133121414131402"
        #print(process_input(input))
        disk_image = render_disk_image(input)
        #print(disk_image)
        formatted = format_disk(disk_image)
        #print(formatted)
        self.assertEqual(1928, calculate_checksum(formatted))

        disk_image_2 = render_disk_image_with_whole_files(input)
        formatted_2 = format_disk_with_whole_files(disk_image_2)
        #print(render_part2_disk(formatted_2))
        #print(part2(input))
        self.assertEqual(2858, part2(input))

        pass

if __name__ == "__main__":
    unittest.main()
