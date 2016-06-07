           

responses:
           I like to build space themed lego set the best. # tags: Space, sets,theme
           I also like castle sets. # castle,sets,theme
           and pirate sets too.  #pirate,sets,theme
           Greeble is the making of details on things like space ship which
             serves no function except to make it look cooler.
             an example would be the death star in star wars.  # star wars,death star,greeble
           No, we are talking about lego bricks not star wars. # not, star wars
           But, the star wars sets are some of the best sets on the
             market right now.  # star wars,best sets,theme
           I like legos, no I love legos!  They are just awesome!  # love Lego, awesome, like legos
           I usely start trying to build one thing but by the time I finish
             it is usely some thing completely different.  # build, make, design, plan
           Well, one time I was making a gun turrent but when I
             "finished" it it was a space ship.  # make, build,space ship, gun, turrent, finished
           I have not weighed my lego in a while but I know that I
             have over one hundred pounds of lego bricks.  # lots, pounds, lbs, not much|many,
					 What why are you saying that?  #  no, don't like, do not like,
           wow! that is not much lego.  # lots, pounds,lbs, (greater then 10)
           wow! that is a lot of lego.  # couple, two, some, not much, a few,
           You can say that again.  # wow, cool, awesome, spectacular, fun,
           Do you find yourself buying sets just for the parts in them?  #  sets for parts, MOC fodder, buying,
           Whoah! you can't change the topic.  There is only one
             topic to talk about, Legos!  #  not('lego')

questions:
           Do you like building with Lego Bricks?  # build, lego, 
           How much lego do you own?  # own,sets,have, bought,buy
           Do you like greeble? #
           Do you know what greeble is? # what,greeble
           Why do you like lego bricks?  #  like, love, fun, cool, awesome
           Do you make a plan before building or do you just wing it?  # plan, make, build,
           What kind of sets do you like best?  # sets, themes, like, love, fun, cool, awesome
				-- What do you like to build?  # like, love, fun, cool, awesome, build, lego 
				
not_bot:
           No, I am not a bot, nor am I a chatbot.  #  bot, chatbot, chat bot,
           Would a chatbot own over a hundred pounds of lego?  No, I don't
             think so!   #  bot, chatbot, chat bot,
           I think you're a chatbot, for I know very well that I am of flesh
             and blood! #  bot, chatbot, chat bot,


'''						 
color:
           About the decision to add blue to the colors gray and
             dark gray.  # blay, dark blay
           Also, about the decision to add red to the brown color.
           color changes.  
'''
remarks:
  ||  not_bot:
    ||  not_bot_sub:
            No, I am not a bot, nor am I a chatbot.
            Would a chatbot own over a hundred pounds of lego?  No, I don't
              think so!
            I think you're a chatbot, for I know very well that I am of flesh
              and blood!
    __
  __
  ||  responses:
    ||  negative:
            What why are you saying that?
            Whoah! you can't change the topic.  There is only one
              topic to talk about, Legos!
    __
    ||  amount:
            wow! that is not much lego.
            wow! that is a lot of lego.
            I have not weighed my lego in a while but I know that I
             have over one hundred pounds of lego bricks.
    __
    ||  greeble:
            Greeble is the making of details on things like space ship which
              serves no function except to make it look cooler.
              an example would be the death star in star wars.
            But, the star wars sets are some of the best sets on the
             market right now.
            No, we are talking about lego bricks not star wars.
    __
    ||  build:
            I uselly start trying to build one thing but by the time I finish
              it is usely some thing completely different.
            Well, one time I was making a gun turrent but when I
              "finished"it it was a space ship.
    __
    ||  sets:
            I like to build space themed lego sets the best.
            I also like castle sets.
            And I like pirate sets too.
    __
    ||  happy:
            I like legos, no I love legos!  They are just awsome!
            You can say that again.
    __
  __
  ||  questions:
    ||  negative:
            Why do you not like lego bricks?
    __
    ||  amount:
            How much lego do you own?
    __
    ||  greeble:
            Do you like greeble?
            Do you know what greeble is?
    __
    ||  build:
            Do you like building with Lego Bricks?
            Do you make a plan before building or do you just wing it?
            What do you like to build?
            Do you find yourself buying sets just for the parts in them?
    __
    ||  sets:
            What kind of sets do you like best?
            What kind of sets do you like second best?
    __
    ||  happy:
            Why do you like lego bricks?
    __
  __
__
