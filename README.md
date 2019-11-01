<p align="center">
  <img width="200" height="200" style="align=center;" src="https://miro.medium.com/max/2400/1*TiJl4Rh47os3hVGoWMwhJQ.gif">
</p>

#### Project was made based on my classroom exercicies

<h1 style"align-text=center;"> Project: Balanced Binary Tree </h1>
 A project about Data Structure based on Tree Model with balance.

## What I use?

I use Python and this libs:
    <ul>
      <li> drawtree (to print Tree) </li>
      <li> chronometer (to get time per instruction) </li>
      <li> random (to generate random numbers and insert they on tree) </li>
    </ul>

## What I do?

I will explain step by step i do to balance Tree:
  <ul>
    I will insert some Nodes, on this example I will insert those -> [50, 40, 35, 30, 25, 47, 43, 41, 44, 55, 60, 57, 65], ok lets do it.
    I will insert Nodes on Tree how in reality, one by one, i will stop when Tree is unbalanced.
    <br>
	<li> I inserted 50(root), then 40, then 35 and Tree looks how this: </li>
	<p align="center">
	<img src="https://i.ibb.co/WVXp9zR/Balanced-Tree-Step-01.png" border="0">
	</p>
	<li> How you can see, Tree is unbalanced on left side, left is 2 Nodes more high than right, lets balance it:</li>
	<p align="center">
	<img src="https://i.ibb.co/b5fwt8j/Balanced-Tree-Step-02.png" border="0">
	</p>
	<li> Above I change the root of Tree to keep it balanced (how left side is the highest, i get the first Node on left and replace in root, if on this case the right side was the highest I replace the first Node on right), ok, now we can keep inserting Nodes:</li>
	<p align="center">
	<img src="https://i.ibb.co/6JcNYQd/Balanced-Tree-Step-02.png" border="0">
	</p>
  </ul>
<br>

## What a Balanced Binary Tree have different compared to a Simple Binary Tree?

<p align="center">
<img width="375" height="150" style="align=center;" src="https://www.tutorialspoint.com/data_structures_algorithms/images/unbalanced_avl_trees.jpg">
</p>

<p align="left">
  A Balanced Tree can improve a search on Tree making it more faster with some rules:
    <ul>
      <li> Left side and right side of the Tree need to have same height or in maximum one Node of difference in height (height its referenced by root of the Tree)</li>
      <li> If some side is more high, is doing a balance of Tree </li>
      <li> The balance involve passing Nodes from highest side to the lowest side (right or left) up until they have a maximum of one Node of height of difference or equal (You can see this on example image above)</li>
    </ul>
</p>
<br>
<p align="left">
  A Binary Tree without Balance which contain much insertions can spend so much time on a search, while a Balanced Tree can do it so much faster when have same height on sides
</p>
