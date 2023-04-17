(define (domain p_1-domain)
 (:requirements :strips :typing :negative-preconditions)
 (:types robot apple location)
 (:predicates (at_ ?robot - robot ?locaiton - location) (on ?apple - apple ?location - location) (holding ?robot - robot ?apple - apple))
 (:action move
  :parameters ( ?r - robot ?fl - location ?tl - location)
  :precondition (and (at_ ?r ?fl) (not (at_ ?r ?fl)))
  :effect (and (at_ ?r ?fl) (not (at_ ?r ?tl))))
 (:action pick
  :parameters ( ?a - apple ?r - robot ?loc - location)
  :precondition (and (at_ ?r ?loc) (on ?a ?loc) (not (holding ?r ?a)))
  :effect (and (holding ?r ?a) (not (on ?a ?loc))))
 (:action place
  :parameters ( ?a - apple ?r - robot ?loc - location)
  :precondition (and (holding ?r ?a) (at_ ?r ?loc))
  :effect (and (not (holding ?r ?a)) (on ?a ?loc)))
)
