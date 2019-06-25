import unittest
from h3p2_recursive_bingers import MatrixChainMultiplication as recursive_class
from h3p2_dp_bingers import MatrixChainMultiplication as dp_class
from h3p2_memoized_bingers import MatrixChainMultiplication as memoized_class

class TestCases(unittest.TestCase):
	def testcase1(self):
		dimensions = [1, 2, 3, 4, 3]
		answer = 30

		recursive_instance = recursive_class(dimensions)
		dp_instance = dp_class(dimensions)
		memoized_instance = memoized_class(dimensions)


		self.assertEqual(recursive_instance.recursive(), answer)
		self.assertEqual(dp_instance.dp(), answer)
		self.assertEqual(memoized_instance.memoized(), answer)

if __name__ == "__main__":
    unittest.main()