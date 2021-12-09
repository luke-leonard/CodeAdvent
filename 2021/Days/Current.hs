module Main where
import System.IO 
import Data.List.Split
import Debug.Trace
import Data.List
import Data.Function
import qualified Data.Map as Map  
import Data.Char

main :: IO ()
main = do
    contents <- readFile "Days/Day09/Input.txt" 
    let vals = map (map digitToInt) $ lines contents
    let len = length $ head vals
    let empty = take len [10,10..]
    let res = adj2 $  map padd10 ([empty] ++ vals ++ [empty])
    print $ sum $ map (+1) $ filter (/=(-1)) $ concat res

padd10 :: [Int] -> [Int]
padd10 val = [10] ++ val ++ [10]

adj2 :: [[Int]] -> [[Int]]
adj2 [] = []
adj2 vals = adj vals : adj2 (tail vals)

adj :: [[Int]] -> [Int] 
adj [] = []
adj vals = getNeighbors vals : adj (transpose (tail $ transpose vals))

getNeighbors :: [[Int]] -> Int
getNeighbors start@((_:u:_):(l:x:r:_):(_:d:_):_) = isMinimum x [l,r,u,d]
getNeighbors _  = -1


isMinimum :: Int -> [Int] -> Int
isMinimum val vals
    | val < minimum vals = val
    | otherwise = -1



