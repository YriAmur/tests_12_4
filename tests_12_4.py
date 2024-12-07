import logging
from idlelib.iomenu import encoding

import HumanMoveTest
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner= HumanMoveTest.Runner("Nax", -10)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)


    def test_run(self):
        try:
            runner = HumanMoveTest.Runner(10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f"Неверный тип данных для объекта Runner", exc_info=True)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')
