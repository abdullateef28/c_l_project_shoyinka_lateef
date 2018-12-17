import turtle
#Lift up the pen
turtle.penup()
turtle.delay(50)

#2. Move the turtle to the position that is at (-200, 200)
turtle.setposition(-200, 200)

#3. Place the pen down
turtle.pendown()

#comment to increase the pensize
turtle.pensize(10)

#4. Change the colours for the pen such that the outline colour for the pen is gold and the fill colour is black
turtle.color('blue', 'orange')

#5. Begin the fill
turtle.begin_fill()

#6. Move the turtle forward by 400 pixels7. Turn right by 90 degrees
turtle.forward(400)
turtle.right(90)

#8. Move the turtle forward by 400 pixels
#9. Turn right by 90 degrees
turtle.forward(400)
turtle.right(90)

#10. Move the turtle forward by 400 pixels
#11. Turn right by 90 degrees
turtle.forward(400)
turtle.right(90)

#12. Move the turtle forward by 400 pixels
#13. Turn right by 90 degrees
turtle.forward(400)
turtle.right(90)

#14. End the fill
turtle.end_fill()

#15. Lift the pen
#16. Move the turtle back to the home position
#17. Change the pen colour to gold
#18. Set the pen size to 10 pixels
turtle.penup()
turtle.home()
turtle.pencolor('blue')
turtle.pensize(10)

#19. Move to the position that is (0, -80)
#20. Place the pen down
#21. Draw a circle that is 80 pixels in radius
turtle.setposition(0, -80)
turtle.pendown()
turtle.circle(80)

#comment to draw the second circle
#22. Lift up the pen
#23. Move to the position that is (0, -130)
#24. Place the pen down
#25. Draw a line that is 130 pixels in radius
turtle.penup()
turtle.setposition(0, -130)
turtle.pendown()
turtle.circle(130)

#comment to draw the last concentric circle
#26. Lift up the pen
#27. Move to the position that is (0, -180)
#28. Place the pen down
#29. Draw a line that is 180 pixels in radius
#30. Hide the turtle
turtle.penup()
turtle.setposition(0, -180)
turtle.pendown()
turtle.circle(180)
turtle.hideturtle()

turtle.end_fill()

