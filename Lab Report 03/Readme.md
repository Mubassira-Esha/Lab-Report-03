You are given an undirected graph with N vertices and M edges. Your task is to implement a Python program that uses Backtracking to determine whether the graph can be colored using K colors such that no two adjacent vertices share the same color. The input will be read from a file, where the first line contains three integers: N (number of vertices, numbered from 0 to N−1), M (number of edges), and K (number of available colors). Each of the following M lines contains two integers u and v, representing an undirected edge between vertex u and vertex v.

Case#1Input:
4 5 3
0 1
0 2
1 2
1 3
2 3

Case#1Output:
Coloring Possible with 3 Colors
Color Assignment: [1, 2, 3, 1]

![Output](Screenshot/(Case01).png)

Case#2Input:
4 5 2
0 1
0 2
1 2
1 3
2 3

Case#2Output:
Coloring Not Possible with 2 Colors


![Output](Screenshot/(Case02).png)
