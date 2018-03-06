type Dominoe = (Int, Int)

dominoeSet :: Int -> [Dominoe]
dominoeSet (-1) = []
dominoeSet n = [(n,q)| q <- [0..n]] ++ (dominoeSet (n - 1))
