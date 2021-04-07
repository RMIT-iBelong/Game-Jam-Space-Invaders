# Game Jam: Space Invaders!
> Read the instructions below and complete each section!
>
> <<< Click on `main.py` to write your code!

---

![](https://i.imgur.com/fl9hJVK.png)

Complete each section to make changes to your ***Space Invaders*** game!

If you make a mistake, that's okay! You can try to fix the error, or you can click on the link below and click the `Fork` button again to take a fresh, brand new copy.

* https://repl.it/@e94175/Game-Jam-Space-Invaders

---

## Section 1: Variables!
Variables are containers that store data values. We can store different **types of values** inside variables. It is entirely up to you what those values might be and it will differ depending on the project you are coding. Some examples of these types are:

* integers (`number = 5`)
* floats (`number = 5.0`)
* strings (`word = "hello"`)

You can read more about Python variables [here](https://www.w3schools.com/python/python_variables.asp).

#### Activity: Player name!

In the file `main.py`, find the variable called `player_name` and change it from `"treetops"` to your own name! **Hint:** the variable is somewhere between lines `60` and `80`. Remember to put your name inside quotation marks!

Below is an example of what your code might look like:

```
player_name = "Alice"
```

---

> <<< `Run` the game to test your changes!

---

#### Activity: Player lives!

In the file `main.py`, find the variable called `lives` and change it from `5` to a different number of your choice. Notice that this one doesn't have quotation marks around it! **Hint:** lives should be a positive number, but what happens if you set it to `-1`?

Below is an example of what your code might look like:

```
lives = 10
```

---

> <<< `Run` the game to test your changes!

---

## Section 2: Features!
Features in games or programs that we create are really important as they give meaning to what we have built using code. Game features can be the ability to play with others in multiplayer, playing music tracks, adding new levels or missions, or having an inventory of items available to the player.

You can read more about game features [here](https://www.gamedesigning.org/learn/basic-game-mechanics/).

#### Activity: Keeping score!

Our game is keeping score, but it's only printing out in the console area, which players won't see if they're just playing the game. Let's make the score show up on the big screen! In `main.py`, find the `score_label` variable, then look at the `WINDOW.blit` code underneath that, which is printing the `player_name` and the number of `lives`. Add another `WINDOW.blit` line just like this, put instead of `player_name_label` or `lives_label`, use `score_label`! You can adjust the `(10, 10)` section to change where the label appears on your screen as well.

Below is an example of what your code might look like:

```
WINDOW.blit(score_label, (10, 60))
```

---

> <<< `Run` the game to test your changes!

---

#### Activity: More ship colours!

In our game the enemy ships that currently spawn are coloured blue and green. But we have a red ship too! There is a `.png` file for a red ship in our `assets` folder that we're not using right now. Let's change that!

In the file `main.py` find the code below:

```
enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice([
	"blue",
	"green",
]))
```

Now, let's update that code to include the colour red.

```
enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice([
	"blue",
	"green",
	"red"
]))
```

Did that work? Why, or why not?

---

> <<< `Run` the game to test your changes!

---

## Section 3: Debugging!
Debugging is the the process of finding errors - commonly known as bugs - in your code and removing them! There are special tools that we can use to help with debugging and finding errors, but sometimes we can find them just by reading our code carefully. You can read more about debugging [here](https://blog.bitlabstudio.com/the-importance-of-debugging-886df73427ea).

#### Activity: Rainbow lasers!
You might have noticed that we have multiple `.png` image files for lasers, like `laser_blue.png` and `laser_green.png`, but all of the enemy ships in our game are shooting red lasers! That must mean they're all using `laser_red.png`, but is that what's supposed to happen?

In `main.py`, see if you can change the code so that each ship fires a laser that matches its own colour. I.e. green ships fire green lasers, blue ships fire blue lasers and red ships fire red lasers.

---

> <<< `Run` the game to test your changes!

---

## Section 4: Extension!
Nice work, you're a programming wizard! Have a go at these extension tasks.

#### Activity: Make your own ship!
1. Draw your own sprite artwork using [PiskelApp](https://www.piskelapp.com/)
2. Download the image from PiskelApp as a `.png` file
3. Save your sprite in the `assets` folder in the `Files` menu
4. In `main.py`, update `PLAYER_SHIP` to your new `.png` file

#### Activity: Cheating!
1. Give yourself a ridiculous amount of lives like `1000000`
2. Change the code so that you don't take damage when an enemy ship hits you
3. Make it so that your health is increased by `100` when you defeat an enemy
4. Give yourself a score that starts at `10000` and increases by `1000` when you defeat an enemy

---

> <<< `Run` the game to test your changes!

---

#### License Information

The source code and image assets for this project have been taken and modified from the code and assets provided by [*Tech with Tim*](https://www.techwithtim.net/) as seen in [this video tutorial](https://www.youtube.com/watch?v=Q-__8Xw9KTM).
