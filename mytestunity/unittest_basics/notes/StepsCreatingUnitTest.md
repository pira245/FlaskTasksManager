> # __The following steps are involved in writing a simple unit test:__

> > - __Step 0:__ Create a package directory with 2 sub-directories called Library and unittest_test.
> 
> > - __Step 1:__ Import the unittest module in your program.
> 
> > - __Step 2:__ Define a function or class to be tested. Keep the source file of the function or class in the Library sub-directory. 
>
> > - __Step 3:__ Create a testcase by subclassing unittest.TestCase. Keep the source file for the unittest in the unittest_test folder.
>
> > - __Step 4:__ Define a test as a method inside the class. Name of method must start with 'test'.
>
> > - __Step 5:__ Each test calls assert function of TestCase class. There are many types of asserts.
Following example calls assertEquals() function.
>
> > - __Step 6:__ assertEquals() function compares result of add() function with arg2 argument and
throws assertionError if comparison fails.
>
> > - __Step 7:__ Finally, call main() method from the unittest module.
>
> > Check the examples 
[Company.py](..%2F..%2FLibrary%2FCompany.py) and 
[TestLibraryCompany.py](..%2FTestLibraryCompany.py) .
>
---