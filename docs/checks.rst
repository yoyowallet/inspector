Checks and check runs
=====================

The concept of a check comes from mathematical equations,
which have a right hand side and a left hand side.
Additionally, a warning value can be set. It is evaluated only
when the primary condition is not met. Warning value was designed
to be used for 'known issues', where a certain degree of discrepancy
is acceptable.

Check groups
------------

Currently a check can belong to a maximum of 1 group,
and a whole group can be executed at once.
In the future, there might be a more flexible solution,
such as tags, but this is not a priority for now
