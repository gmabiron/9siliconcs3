# Class Attributes and Methods
## Previous Activity
Link to my previous activity:
[classObjectUML.md](classObjectUML.md)
## Design Revision
- Set the class name to Sport to encapsulate common attributes across different sports like Basketball and Volleyball.
- Added a private __score attribute to safely keep track of team points.
- Encapsulated __condition as private to prevent direct external modification of the game status.

## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
| name | string | Public | General identifier that poses no risk when accessed directly. |
| inventor | string | Public | Informational historical property that requires no protection. |
| games | int | Public | Represents regular season scheduled length; safely readable openly. |
| condition | boolean | Private | Regulates game execution state; must be updated through dedicated game methods. |
| score | int | Private | Protects team scores from direct, unvalidated external modification. |

## Updated UML Class Diagram
![Class Diagram](images/classDiagramSG5.png)

## Python Implementation
[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
I made the score and condition attributes private so an external code cannot change variables directly without validation.

### Which method changes the state of your object?
The add_point(points: int) method directly modifies the internal state of the __score attribute. When executed, it validates that the added points are positive and increments self.__score by the given value.

### How did your two objects demonstrate that instances are independent?

### What is the difference between your class diagram and your object diagram?