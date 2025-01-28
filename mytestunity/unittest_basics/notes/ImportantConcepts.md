> # __unittest supports the following important concepts__


- __test fixture:__ This represents the preparation needed to perform one or more
tests, and any associate cleanup actions. This may involve, for example,
creating temporary or proxy databases, directories, or starting a server
process.
- __test case:__ This is the smallest unit of testing. This checks for a specific
response to a particular set of inputs. unittest provides a base class, TestCase,
which may be used to create new test cases.
- __test suite:__ This is a collection of test cases, test suites, or both. This is used
to aggregate tests that should be executed together. Test suites are
implemented by the TestSuite class.
- __test runner:__ This is a component which orchestrates the execution of tests
and provides the outcome to the user. The runner may use a graphical
interface, a textual interface, or return a special value to indicate the results of
executing the tests.

---