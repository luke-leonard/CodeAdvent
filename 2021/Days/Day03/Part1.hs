module Main where
import System.IO 


main :: IO ()
main = do
    contents <- readFile "Days/Day03/Input.txt" 
    let contentList = lines contents
    -- print contentList
    let modResults = findPopularBits contentList (take (length (head contentList)) [0,0..])
    -- print modResults
    print (getResult modResults)

getResult :: [Int] -> Int
getResult xs = getGamma (reverse xs) 1 * getEpsilon (reverse xs) 1

getGamma :: [Int] -> Int -> Int
getGamma [] multiplier = 0
getGamma xs multiplier = (getGammaDigit (head xs) * multiplier) + getGamma (tail xs) (multiplier * 2)

getGammaDigit :: Int -> Int
getGammaDigit digit
    | digit > 0 = 1
    | digit <= 0 = 0
getGammaDigit _ = 0

getEpsilon :: [Int] -> Int -> Int
getEpsilon [] multiplier = 0
getEpsilon xs multiplier = (getEpsilonDigit (head xs) * multiplier) + getEpsilon (tail xs) (multiplier * 2)

getEpsilonDigit :: Int -> Int
getEpsilonDigit digit
    | digit > 0 = 0
    | digit <= 0 = 1
getEpsilonDigit _ = 0

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




