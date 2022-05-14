# Python Data Structures and Algorithms

## 02 - The Stack Data Structure

- All insertions and deletions are made on one end: the top of the stack
- LIFO: last in, first out
  - `push(item)`: append on top
  - `pop(stack)`: remove and return the top item
  - `peek(stack)`: return the top item without removing it
  - `is_empty(stack)`: check the stack is empty

## 03 - The 2D List Data Structure

- Grid, table, matrix
- List of lists
- 2D lists and Graphs
  - Nodes
  - Edges
  - Undirected
  - Directed
  - Weights
- Each cell of a table = Node
- The surrounding cells are connected by Edges
  - Obstacles are possible
- Cartesian Coordinates `(x, y)`
- Matrix Coordinates `(i, j)` (row, column)

## 04 - Depth-first Search Algorithm

- Optimizations for criteria (cost, speed, safety, fuel, etc)
- Pathfinding
- Scheduling algorithms
- Assessing investment decision trees
- Ordering of formula cell evaluation in spreadsheets
- Determining the order of compilation tasks for software builds
- Data serialization
- Resolving symbol dependencies
- Pseudocode
  - Stack: [start_position]
  - Predecessors: {start_pos: None}
  - Algorithm:
    - Pop the stack
    - Is this the goal?
      - If so, we're done
      - Othewise push undiscovered neighbors onto the stack and add them to predecessors/discovered
        - Up, right, down, left

## 05 - The Queue Data Structure

- CPU schedule
- Data is transferred asynchronously between two processes
- Graph traversal algorithms
- Transport and operations management
- File servers
- IO buffers
- Printer queues
- Phone calls to customer service hotlines
- Resource is shared among multiple consumers
- Appends to the `tail`
- Pops from `head`
- FIFO
  - `enqueue`: append to `tail`
  - `dequeue`: pop from `head`

## 06 - Breadth-first Search Algorithm

- GPS systems
- Flight reservation systems
- Finding neighbor nodes in peer-to-peer networks
- Social networking sites to find connections between users
- Web crawlers
- Many applications in AI
- Electronics and communication engineering
- Scientific modeling

## 07 - The Priority Queue Data Structure

- Resources must be allocated depending in rules of predecessors
- AI: A\* search algorithm
- Optimization algorithms
- Operating system process scheduling
- Bandwidth management
- Statistical analysis
- Spam filtering
- Operations:
  - `get()`: retrieve the item with the highest priority
  - `put(item)`: add item to priority queue
  - `is_empty()`: determine if the priority queue is empty

## 08 - The A\* Search Algorithm

- Traffic navigational system (GPS)
- Social network analysis
- Natural language processing
- Machine learning
- Puzzle solutions and puzzle-analogous problems
- Algorithimic trading
- Robotics
- Video games
- `Manhattan distance` or `Taxi-cab distance`
  - Use heuristics to determine the best path choice for the algorithm
  - Rule of thumb: change the next position given its distance from the goal
- Key Values:
  - G value: best distance from start to current cell
  - H value: heuristic distance from current cell to destination
  - F value: the sum of the G value and the H value (representing the probable optimal value or minimum distance based on the heuristic used)
