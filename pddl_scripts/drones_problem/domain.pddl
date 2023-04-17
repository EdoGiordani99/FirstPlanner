(define (domain drones-domain)
 (:requirements :strips :typing :negative-preconditions)
 (:types
    drone location good - object
    sugar_0 milk_0 - good
    house shop - location
 )
 (:predicates (at_ ?drone - drone ?locaiton - location) (holds ?drone - drone ?good - good) (free ?drone - drone) (requires ?house - house ?good - good) (adjacent ?l1 - location ?l2 - location) (sells ?shop - shop ?good - good))
 (:action fly
  :parameters ( ?d - drone ?li - location ?lf - location)
  :precondition (and (at_ ?d ?li) (not (at_ ?d ?lf)) (adjacent ?li ?lf))
  :effect (and (at_ ?d ?lf) (not (at_ ?d ?li))))
 (:action take
  :parameters ( ?d - drone ?g - good ?s - shop)
  :precondition (and (at_ ?d ?s) (free ?d) (not (holds ?d ?g)) (sells ?s ?g))
  :effect (and (holds ?d ?g) (not (free ?d))))
 (:action leave
  :parameters ( ?d - drone ?g - good ?h - house)
  :precondition (and (at_ ?d ?h) (not (free ?d)) (holds ?d ?g) (requires ?h ?g))
  :effect (and (not (holds ?d ?g)) (not (requires ?h ?g)) (free ?d)))
)
