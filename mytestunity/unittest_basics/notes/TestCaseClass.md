> # __TestCase Class__

> > Object of this class represents the smallest testable unit. It holds the test routines and
provides hooks for preparing each routine and for cleaning up thereafter. 
> 

The following methods are defined in the TestCase class:  

| Method             | Description                                                                                                                                        |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| setUp()            | Method called to prepare the test fixture. This is called immediately before calling the test method                                               |
| tearDown()         | Method called immediately after the test method has beencalled and the result recorded. This is called even if the testmethod raised an exception. |
| setUpClass()       | A class method called before tests in an individual class run.                                                                                     |
| tearDownClass()    | A class method called after tests in an individual class have run.                                                                                 |
| run(result=None)   | Run the test, collecting the result into the test result object passed as result.                                                                  |
| skipTest(reason)   | Calling this during a test method or setUp() skips the current test.                                                                               |
| debug()            | Run the test without collecting the result.                                                                                                        |
| shortDescription() | Returns a one-line description of the test.                                                                                                        |

> > Check the examples 
[Student.py](..%2F..%2FLibrary%2FStudent.py) and 
 [TestLibraryStudent.py](..%2FTestLibraryStudent.py).
>
---