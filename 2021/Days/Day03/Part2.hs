module Main where
import System.IO 


main :: IO ()
main = do
    contents <- readFile "Days/Day03/Input.txt" 
    let contentList = lines contents
    -- print contentList
    print $ getResult contentList



getResult :: [String] -> Int
getResult xs = do
    let o2Str =  getOxygenLevelString xs 0
    let cO2Str = getC02LevelString xs 0
    getBinaryVal (reverse o2Str) 1 * getBinaryVal (reverse cO2Str) 1

getBinaryVal :: String -> Int -> Int
getBinaryVal [] multiplier = 0
getBinaryVal xs multiplier = (getBinaryDigit (head xs) * multiplier) + getBinaryVal (tail xs) (multiplier * 2)

getBinaryDigit :: Char -> Int
getBinaryDigit char
    | char == '0' = 0
    | char == '1' = 1
getBinaryDigit _ = 0

getOxygenLevelString :: [String] -> Int -> String
getOxygenLevelString [str] index = str
getOxygenLevelString xs index = do
    let aggValue = findPopularBits xs (take (length (head xs)) [0,0..]) !! index
    getOxygenLevelString (reduceStringListWhereIndexEqualsChar xs index (getGammaDigit aggValue)) (index + 1)
    
getC02LevelString :: [String] -> Int -> String
getC02LevelString [str] index = str
getC02LevelString xs index = do
    let aggValue = findPopularBits xs (take (length (head xs)) [0,0..]) !! index
    getC02LevelString (reduceStringListWhereIndexEqualsChar xs index (getEpsilonDigit aggValue)) (index + 1)

reduceStringListWhereIndexEqualsChar :: [String] -> Int -> Char -> [String]
reduceStringListWhereIndexEqualsChar xs index val = filter (\str -> str !! index == val) xs

findPopularBits :: [String] -> [Int] -> [Int]
findPopularBits [] total = total
findPopularBits xs total = findPopularBits (tail xs) (addSampleToTotal (head xs) total)

addSampleToTotal :: String -> [Int] -> [Int] 
addSampleToTotal [] total = []
addSampleToTotal sample total = applyBitOpp (head sample) (head total) : addSampleToTotal (tail sample) (tail total)

applyBitOpp :: Char -> Int -> Int 
applyBitOpp sample total
    | sample == '0' = total - 1
    | sample == '1' = total + 1
applyBitOpp _ _ = 0

getGammaDigit :: Int -> Char
getGammaDigit digit
    | digit >= 0 = '1'
    | digit < 0 = '0'
getGammaDigit _ = '1'

getEpsilonDigit :: Int -> Char
getEpsilonDigit digit
    | digit >= 0 = '0'
    | digit < 0 = '1'
getEpsilonDigit _ = '1'
