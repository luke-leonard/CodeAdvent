module Main where
import System.IO 


main :: IO ()
main = do
    putStrLn . show . answerQuestion $ "hi"
    putStrLn . show . calcNumberOfTimesListIncreases $ []
    putStrLn . show . calcNumberOfTimesListIncreases $ [1]
    putStrLn . show . calcNumberOfTimesListIncreases $ [1,0]
    putStrLn . show . calcNumberOfTimesListIncreases $ [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    contents <- readFile "Days/Day01/input.txt" 
    putStrLn . show . calcNumberOfTimesListIncreases $ map readInt (lines contents)

readInt :: String -> Int
readInt s = read s :: Int

answerQuestion :: String -> Int
answerQuestion "" = 0 
answerQuestion s = length s

calcNumberOfTimesListIncreases :: [Int] -> Int
calcNumberOfTimesListIncreases [] = 0
calcNumberOfTimesListIncreases [x] = 0
calcNumberOfTimesListIncreases xs 
    | head xs < (head . tail $ xs) = 1 + (calcNumberOfTimesListIncreases . tail $ xs)
    | head xs >= (head . tail $ xs) = calcNumberOfTimesListIncreases . tail $ xs
    | otherwise = 0