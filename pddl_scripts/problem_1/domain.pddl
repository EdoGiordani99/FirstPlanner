(define (domain problem_1-domain)
 (:requirements :strips :typing :negative-preconditions)
 (:types robot apple location)
 (:predicates (at_ ?robot - robot ?locaiton - location) (on ?apple - apple ?location - location) (holding ?robot - robot ?apple - apple))
 (:action move
  :parameters ( ?r - robot ?l_from - location ?l_to - location)
  :precondition (and (at_ ?r ?l_from) (not (at_ ?r ?l_to)))
  :effect (and (not (at_ ?r ?l_from)) (at_ ?r ?l_to)))
 (:action pick
  :parameters ( ?a - apple ?r - robot ?loc - location)
  :precondition (and (at_ ?r ?loc) (on ?a ?loc) (not (holding ?r ?a)))
  :effect (and (holding ?r ?a) (not (on ?a ?loc))))
 (:action place
  :parameters ( ?a - apple ?r - robot ?l - location)
  :precondition (and (holding ?r ?a) (at_ ?r ?l) (not (on ?a ?l)))
  :effect (and (on ?a ?l) (not (holding ?r ?a))))
)
