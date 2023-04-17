(define (problem drones-problem)
 (:domain drones-domain)
 (:objects
   d1 d2 d3 - drone
   h1 h2 h3 h4 h5 h6 h7 h8 h9 - house
   s1 s2 - shop
   sugar - sugar_0
   milk - milk_0
 )
 (:init (at_ d1 s2) (at_ d2 s2) (at_ d3 h5) (requires h3 milk) (requires h8 sugar) (requires h7 milk) (requires h7 sugar) (sells s1 sugar) (sells s2 milk) (adjacent h1 s1) (adjacent h2 s1) (adjacent h3 h5) (adjacent h4 h5) (adjacent h4 h7) (adjacent h5 h3) (adjacent h5 h4) (adjacent h5 h8) (adjacent h5 s1) (adjacent h6 h8) (adjacent h7 h4) (adjacent h7 s2) (adjacent h8 h5) (adjacent h8 h6) (adjacent h8 h9) (adjacent h9 h9) (adjacent s1 h1) (adjacent s1 h2) (adjacent s1 h5) (adjacent s2 h7) (adjacent s2 h8) (free d1) (free d2) (free d3))
 (:goal (and (not (requires h1 milk)) (not (requires h1 sugar)) (not (requires h2 milk)) (not (requires h2 sugar)) (not (requires h3 milk)) (not (requires h3 sugar)) (not (requires h4 milk)) (not (requires h4 sugar)) (not (requires h5 milk)) (not (requires h5 sugar)) (not (requires h6 milk)) (not (requires h6 sugar)) (not (requires h7 milk)) (not (requires h7 sugar)) (not (requires h8 milk)) (not (requires h8 sugar)) (not (requires h9 milk)) (not (requires h9 sugar))))
)
