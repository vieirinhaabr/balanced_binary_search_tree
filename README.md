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

## How this project work?

I will explain step by step what this code do to balance the Tree:
  <ul>
    I will insert some nodes, in this example I will insert these in this order -> [50, 40, 35, 36, 39, 38, 37, 51, 52], ok lets do it.
    I will insert Nodes on Tree how in reality, one by one, I will stop to explain when Tree is unbalanced.
    <br>
	<li> I inserted 50(root), then 40, then 35 and Tree looks how this: </li>
	<p align="center">
	<img src="https://i.ibb.co/WVXp9zR/Balanced-Tree-Step-01.png" border="0">
	</p>
	<li> How you can see, Tree is unbalanced on left side, left is 2 Nodes more high than right, lets balance it:</li>
	<p align="center">
	<img src="https://i.ibb.co/DgXvWZZ/Balanced-Tree-Step-02-1.png" border="0">
	</p>
	<li> Above I change the root of Tree to keep it balanced (how left side is the highest, i get the first Node on left and replace in root, if on this case the right side was the highest I replace the first Node on right), ok, now we can keep inserting Nodes:</li>
	<p align="center">
	<img src="https://i.ibb.co/SVkW3V3/Balanced-Tree-Step-03.png" border="0">
	</p>
	<li>On image above how you can see, Tree is again unbalanced, lets balance it:</li>
	<p align="center">
	<img src="https://i.ibb.co/Jms4BkY/Balanced-Tree-Step-04-1.png" border="0">
	</p>
	<li>On image above I replace the root with the nearest Node on highest side, in this case on left side (how you can see, now the first Node on left no is the nearest from root, in this case the nearest from root will be the last Node of the right side of the first left Node of the root  - it will be the nearest from root all times), lets insert more Nodes:</li>
  </ul>
	<p align="center">
	<img src="https://i.ibb.co/mNNqxZW/Balanced-Tree-Step-05.png" border="0">
	</p>
	<li>Again Tree its unbalanced, but now the last Node of the right side have a left Node, will be do the same process but when we pass this node to root, the left Node will be linked at Node before (in right side), after this, Tree will look how that:</li>
	<p align="center">
	<img src="https://i.ibb.co/2cGL7fL/Balanced-Tree-Step-06.png" border="0">
	</p>
	<li>Lets insert more Nodes:</li>
	<p align="center">
	<img src="https://i.ibb.co/XCy1cyH/Balanced-Tree-Step-07.png" border="0">
	</p>
	<li>Again Tree is unbalanced, but now on right side, to balance we will use the same process before, replacing the root with first Node of the highest side:</li>
	<p align="center">
	<img src="https://i.ibb.co/nRtvjJ1/Balanced-Tree-Step-08.png" border="0">
	</p>
	<li>Now we insert all Nodes and Tree is balanced, it will improve the search :D</li>
  </ul>
<br>

## About Functions

I will talk about some functions in the code above, what they do and how they work:
<br>

<h5 align="center">need_balance()</h5>
<p> It </p>

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
