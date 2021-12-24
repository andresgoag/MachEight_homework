![Image](./static/logo.png "logo")

NBA Pairs of Players by Height
=======

Simple flask application to find pairs of players by the sum of their heights.<br>
[Source data](https://mach-eight.uc.r.appspot.com)


# How to run #

There are three ways to run the code.

  1. Go online https://mach-eight-homework.herokuapp.com/
     - [Go to live app](https://mach-eight-homework.herokuapp.com/)
     - Enter the desired sum of heights.
     - Find your perfect pairs of players.

  2. Consume as an API
     - Use the endpoint /matching_pairs/{integer} to get your results in json format.  
     - Example: https://mach-eight-homework.herokuapp.com//matching_pairs/139

  3. Run the basic.py file
     - Install the requirements described on requirements.txt file
     - python3 basic.py