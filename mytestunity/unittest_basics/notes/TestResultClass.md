> # __TestResult Class__

> > This class is used to compile information about the tests that have been successful and 
the tests that have met failure. A TestResult object stores the results of a set of tests. 
A TestResult instance is returned by the TestRunner.run() method.
> 
> TestResult instances have the following attributes:
> 
> 
| Method          | Description                                                                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Errors          | A list containing 2-tuples of TestCase instances and strings holding formatted tracebacks. Each tuple represents a test which raised an unexpected exception.                                          |
| Failures        | A list containing 2-tuples of TestCase instances and strings holding formatted tracebacks. Each tuple represents a test where a failure was explicitly signalled using the TestCase.assert*() methods. |
| Skipped         | A list containing 2-tuples of TestCase instances and strings holding the reason for skipping the test.                                                                                                 |
| wasSuccessful() | Return True if all tests run so far have passed, otherwise returns False.                                                                                                                              |
| stop()          | This method can be called to signal that the set of tests being run should be aborted.                                                                                                                 |
| startTestRun()  | Called once before any tests are executed.                                                                                                                                                             |
| stopTestRun()   | Called once after all tests are executed.                                                                                                                                                              |
| testsRun        | The total number of tests run so far.                                                                                                                                                                  |
| Buffer          | If set to true, sys.stdout and sys.stderr will be buffered in between startTest() and stopTest() being called.                                                                                         |

---