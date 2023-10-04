# Week 3 Homework: Git & GitHub

Welcome to week 3 of Linux Club! This week, your homework is to be done in-class, in teams of 3-4 people.

## Task

We have prepared a template of a tiny Python project in this directory, in the file `fibonacci.py`. Your task here is to take a number as input from the user and print the corresponding number of Fibonacci terms. The catch is, you have to use the [nth term formula](https://r-knott.surrey.ac.uk/Fibonacci/fibFormula.html). This formula is to be calculated using the functions defined in the Python file.

## Steps

The instuctions for completing the assignment are as follows:

1. Fork the [Linux Club repo](https://github.com/ucu-computer-science/UCU_Linux_Club) to your GitHub profile.
2. Add collaborators to the repo on GitHub (split into teams of 3-4 people)
2. Clone the repo to your machine

```{bash}
git clone <link to your fork>
```
3. Each person should create their own branch to make changes

```{bash}
git branch <name of branch>; git checkout <name of branch>
```
4. Split the tasks up between the members of your team
4. Each person navigates to the homework directory and does their task
5. Each person pushes their changes to their branch in the repo

```{bash}
git add .
```

```{bash}
git commit -m "commit name"
```

```{bash}
git push origin <name of branch>
```

6. Pull the changes made by others from GitHub

```{bash}
git pull origin master
```

6. Checkout to main branch and merge your changes

```{bash}
git checkout master
```

```{bash}
git merge <name of branch>
```

7. Push the master branch to GitHub


```{bash}
git push origin master
```

8. Create a pull request to the main repo.
