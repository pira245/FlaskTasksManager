> # __TestLoader Class__

> > The unittest package has the TestLoader class which is used to create test suites from
classes and modules. By default, the unittest.defaultTestLoader instance is automatically
created when the unittest.main(0 method is called. An explicit instance, however enables
the customization of certain properties. 
> The following steps are involved in creating and running a test suite: 
> 
> > In the following code, tests from two classes are collected in a List by using the TestLoader
object.
>> ```python 
>> import unittest
>> testList = [Test1, Test2]
>> testLoad = unittest.TestLoader()
>> TestList = []
>> for testCase in testList:
>>     testSuite = testLoad.loadTestsFromTestCase(testCase)
>>     TestList.append(testSuite)
>>
>> newSuite = unittest.TestSuite(TestList)
>> runner = unittest.TextTestRunner()
>> runner.run(newSuite) 
>> ```

> The following methods are defined in TestSuite class:
> 
| Method                  | Description                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| loadTestsFromTestCase() | Return a suite of all tests cases contained in a TestCase class.                                                              |
| loadTestsFromModule()   | Return a suite of all tests cases contained in the given module.                                                              |
| loadTestsFromName()     | Return a suite of all tests cases given a string specifier.                                                                   |
| discover()              | Find all the test modules by recursing into subdirectories from the specified start directory, and return a TestSuite object. |

---