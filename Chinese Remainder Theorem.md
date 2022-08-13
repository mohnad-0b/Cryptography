# Chinese Remainder Theorem

$x \equiv a1 \mod n1$           
$x \equiv a2 \mod n2$       
...             
$x \equiv an \mod nn$       

How to find $x$?        
first rember wht the mean of `Congruence` is:       
if ( $a \equiv b \mod n$ ) then         
( $a \mod n$ ) ==>  ( $b \mod n$ )

this mean $a \equiv b \mod n$ is a congruence.

now how find value of $x$ in :


$x \equiv 3 \mod 4$           
$x \equiv 5 \mod 6$           
$x \equiv 2 \mod 5$       


what possible value of $x$ in $x \equiv 3 \mod 4$ ?

$x$ = 3,7,11... any value of n*3 + 4 

what possible value of $x$ in $x \equiv 5 \mod 6$ ?

here $x$ = 5,11,17... any value of n*5 + 6

what possible value of $x$ in $x \equiv 2 \mod 5$ ?

here $x$ = 2,8,14... any value of n*2 + 5


$x$ in first equation &rarr; 3,7,11...          
$x$ in second equation &rarr; 5,11,17...            
$x$ in third equation &rarr; 2,8,14...

we need just value avaliable in all equation So :

in first equation 11 is avaliable in second equation  
( $3 \mod 4 = 3$ ) and ( $7 \mod 4 = 3$ ) and ( $5 \mod 6 = 5$ ) and ( $11 \mod 6 = 5$ )

so now $x = 11$ so what is $x \equiv 2 \mod 5$ ? 

$x = 5,11,17,23,29,35,41,47$  &rarr; (47)

So :

$47 \equiv 3 \mod 4$           
$47 \equiv 5 \mod 6$           
$47 \equiv 2 \mod 5$       

:)
