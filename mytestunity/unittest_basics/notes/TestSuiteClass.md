> # __TestSuite Class__

> > Python's testing framework provides a useful mechanism by which test case instances can
be grouped together according to the features they test. This mechanism is made available
by TestSuite class in unittest module. 

> The following steps are involved in creating and running a test suite: 
> 
> > - __Step 1:__ Create an instance of TestSuite class.
>> ```python 
>> suite = unittest.TestSuite()
>> ```
>
> > - __Step 2:__ Add tests inside a TestCase class in the suite.
>> ```python 
>> suite.addTest(testcase class)
>> ```
>
> > - __Step 3:__ You can also use makeSuite() method to add tests from a class.
>> ```python 
>> suite=unittest.makeSuite(test case class)
>> ```
>
> > - __Step 4:__ Individual tests can also be added in the suite. .
>> ```python 
>> suite.addTest(testcaseclass(""testmethod")
>> ```
>
> > - __Step 5:__ Create an object of the TestTestRunner class.
>> ```python 
>> runner = unittest.TextTestRunner()
>> ```
>
> > - __Step 6:__ Call the run() method to run all the tests in the suite.
>> ```python 
>> runner.run (suite)
>> ```
>
> > Check the example [run_unittest_basics.py](..%2Frun_unittest_basics.py).
>

> The following methods are defined in TestSuite class:
> 
| Method           | Description                                                                                  |
|------------------|----------------------------------------------------------------------------------------------|
| addTest()        | Adds a test method in the test suite.                                                        |
| addTests()       | Adds tests from multiple TestCase classes.                                                   |
| run()            | Runs the tests associated with this suite, collecting the result into the test result object |
| debug()          | Runs the tests associated with this suite without collecting the result.                     |
| countTestCases() | Returns the number of tests represented by this test object .                                |
---