"""Test cases for package.

Test's check for all the sources

"""
import unittest
import lyricfetcher as lw


class TestSourceMethods(unittest.TestCase):
    """A Class to test all source."""

    # def test_azlyrics(self):
    #     """
    #     Method to test azlyrics.
    #     Not recommended as AZ says so
    #     """
    #     bad_res = lw.get_lyrics('azlyrics', 'eminem', 'los yourself')
    #     good_res = lw.get_lyrics('azlyrics', 'eminem', 'lose yourself')
    #     self.assertEqual(bad_res, 404)
    #     self.assertTrue(good_res)

    def test_genius(self):
        """Method to test genius lyrics."""
        bad_res = lw.get_lyrics('genius', 'eminem', 'los yourself')
        good_res = lw.get_lyrics('genius', 'eminem', 'lose yourself')
        self.assertEqual(bad_res, 404)
        self.assertTrue(good_res)

    def test_lyricswikia(self):
        """Method to test Lyricswikia."""
        bad_res = lw.get_lyrics('lyricswikia', 'eminem', 'los yourself')
        good_res = lw.get_lyrics('lyricswikia', 'eminem', 'lose yourself')
        self.assertEqual(bad_res, 404)
        self.assertTrue(good_res)

    def test_metrolyrics(self):
        """Method to test metrolyrics."""
        bad_res = lw.get_lyrics('metrolyrics', 'eminem', 'los yourself')
        good_res = lw.get_lyrics('metrolyrics', 'eminem', 'lose yourself')
        self.assertEqual(bad_res, 404)
        self.assertTrue(good_res)


if __name__ == '__main__':
    unittest.main()
