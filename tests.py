from main import Solution
import threading
import json


class TestSolution:
    def test_add(self):
        """
        Test add function creates new item in database.

        :return: None
        """
        test_solution = Solution()
        action_item = '{"action":"jump", "time":100}'
        test_solution.add_action(action_item)
        assert test_solution.database != {}

    def test_get_stats(self):
        """
        Test get_stats is a string formatted json object with correct items.

        :return: None
        """
        test_solution = Solution()

        action_item = '{"action":"jump", "time":100}'
        test_solution.add_action(action_item)

        action_item = '{"action":"jump", "time":200}'
        test_solution.add_action(action_item)

        action_item = '{"action":"run", "time":75}'
        test_solution.add_action(action_item)

        stats = test_solution.get_stats()

        assert type(stats) == str

        stats_json = json.loads(stats)

        assert type(stats_json) == list

        for stat in stats_json:
            if "action" in stat and stat["action"] == "jump":
                assert stat["avg"] == 150
            elif "action" in stat and stat["action"] == "run":
                assert stat["avg"] == 75

    def test_multithread_write(self):
        """
        Test multithread writing to database

        :return: None
        """
        def thread_task(solution, action):
            solution.add_action(action)

        test_solution = Solution()

        thread_1 = threading.Thread(target=thread_task, args=(test_solution, '{"action":"jump", "time":100}'))
        thread_2 = threading.Thread(target=thread_task, args=(test_solution, '{"action":"run", "time":75}'))

        thread_1.start()
        thread_2.start()

        thread_1.join()
        thread_2.join()

        stats = test_solution.get_stats()

        assert len(stats) > 1

