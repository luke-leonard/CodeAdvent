module Main where
import System.IO 
import Data.List.Split
import Debug.Trace
import Data.List



main :: IO ()
main = do
    contents <- readFile "Days/Day05/Input.txt" 
    let lines = getAsLines contents
    let board = applyLinesToBoard (repeat [0,0..]) lines
    -- mapM_ print (windowBoard board 11)
    print . getHotspots $ windowBoard board 1001


getAsLines :: String -> [((Int,Int),(Int,Int))]
getAsLines contents = map (tuplifyPointPair . ( map makePoint . splitOn " -> ")) (splitOn "\n" contents)

tuplifyPointPair :: [(Int,Int)] -> ((Int,Int),(Int,Int))
tuplifyPointPair [x,y] = (x,y)

makePoint :: String -> (Int,Int)
makePoint str = tuplifyInt2 (splitOn "," str)

tuplifyInt2 :: [String] -> (Int,Int)
tuplifyInt2 [x,y] = (readInt x,readInt y)

readInt :: String -> Int
readInt s = read s :: Int


getHotspots :: [[Int]] -> Int
getHotspots board = sum (map (length . filter (>=2)) board)

windowBoard :: [[Int]] -> Int -> [[Int]]
windowBoard board size = take size (map (take size) board)

applyLinesToBoard :: [[Int]] -> [((Int,Int),(Int,Int))] -> [[Int]]
applyLinesToBoard board [] = board
applyLinesToBoard board lines = applyLinesToBoard (applyLineToBoard board (head lines)) (tail lines)

applyLineToBoard :: [[Int]] -> ((Int,Int),(Int,Int)) -> [[Int]]
applyLineToBoard board line 
    | (snd . fst $ line) == (snd . snd $ line) = replaceLine board (zipWith (+) (board !! (snd . fst $ line)) (getHorizontalLine line)) (snd . fst $ line)
    | (fst . fst $ line) == (fst . snd $ line) = transpose (replaceLine (transpose board) (zipWith (+) (transpose board !! (fst . fst $ line)) (getVerticleLine line)) (fst . fst $ line))
    | otherwise = applyLine board line

replaceLine :: [[Int]] -> [Int]-> Int -> [[Int]] 
replaceLine board line index = take index board ++ [line] ++ drop (index + 1) board

getHorizontalLine :: ((Int,Int),(Int,Int)) -> [Int]
getHorizontalLine ((x1,y1),(x2,y2)) = replicate (min x1 x2) 0 ++ replicate (abs(x2-x1) + 1) 1 ++ repeat 0

getVerticleLine :: ((Int,Int),(Int,Int)) -> [Int]
getVerticleLine ((x1,y1),(x2,y2)) = replicate (min y1 y2) 0 ++ replicate (abs(y2-y1) + 1) 1 ++ repeat 0

applyLine :: [[Int]] -> ((Int,Int),(Int,Int)) -> [[Int]]
applyLine board ((x1,y1),(x2,y2)) 
    | x1 == x2 && y1 == y2 = addValAtIndex board (x1,y1)
    | (x1 > x2) && (y1 > y2) = applyLine (addValAtIndex board (x1,y1)) ((x1-1,y1-1),(x2,y2)) 
    | (x1 > x2) && (y1 < y2) = applyLine (addValAtIndex board (x1,y1)) ((x1-1,y1+1),(x2,y2))  
    | (x1 < x2) && (y1 > y2) = applyLine (addValAtIndex board (x1,y1)) ((x1+1,y1-1),(x2,y2)) 
    | (x1 < x2) && (y1 < y2) = applyLine (addValAtIndex board (x1,y1)) ((x1+1,y1+1),(x2,y2)) 

addValAtIndex::[[Int]] -> (Int,Int) -> [[Int]]
addValAtIndex board (x,y) = take y board ++ [take x (board !! y) ++ [(board !! y !! x) + 1] ++ drop (x + 1) (board !! y)] ++ drop (y + 1) board