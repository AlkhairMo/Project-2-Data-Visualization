import unittest
import python_repos


class PythonReposTest(unittest.TestCase):
    def test_status_code(self):
        status_code = python_repos.r.status_code
        self.assertEqual(status_code, 200)

    def test_items_returned(self):
        items_expected = len(python_repos.repo_dicts)
        items_returned = python_repos.done
        self.assertEqual(items_returned, items_expected)

    def test_total_repos(self):
        total_repos = python_repos.response_dict['total_count']
        self.assertGreater(total_repos, 16_200_000)


if __name__ == '__main__':
    unittest.main()
