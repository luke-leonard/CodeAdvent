module MyTest where  
import Part1
import Test.Framework
import Test.Framework.Providers.HUnit
import Test.HUnit


test1 = TestCase $ assertEqual "[]" 0 (calcNumberOfTimesListIncreases [])

-- hUnitTestToTests: Adapt an existing HUnit test into a list of test-framework tests
tests = hUnitTestToTests $ TestList [
    TestLabel "testfoo" test1 ]

main = defaultMain tests