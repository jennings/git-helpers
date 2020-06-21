import unittest
from git_helpers import get_base_url

class GitUpstreamUrl(unittest.TestCase):
    def test_https_urls(self):
        def test(remote, expected_url, expected_host):
            base_url, host = get_base_url(remote)
            self.assertEqual(base_url, expected_url)
            self.assertEqual(host, expected_host)

        test("https://github.com/jennings/example", "https://github.com/jennings/example", "github")
        test("https://bitbucket.org/jennings/example", "https://bitbucket.org/jennings/example", "bitbucket")

    def test_ssh_urls(self):
        def test(remote, expected_url, expected_host):
            base_url, host = get_base_url(remote)
            self.assertEqual(base_url, expected_url)
            self.assertEqual(host, expected_host)

        test("git@github.com:jennings/example", "https://github.com/jennings/example", "github")
        test("git@bitbucket.org:jennings/example", "https://bitbucket.org/jennings/example", "bitbucket")

if __name__ == "__main__":
    unittest.main()
