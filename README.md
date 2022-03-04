**Backend Hackathon**
*API that takes in data from an attendees.json file and builds full CRUD API*
March, 2022
General Assembly

---

***Planning***
📝 Sketches of views and interfaces in the application.
Link to [Structure of Models to Views](https://imgur.com/qfmaJhn).



***Challenges*** 
*Demonstrating Code*
- What was the most difficult part? 
The most difficult part was figuring out what kind of json format django needed in order to load data.  I had to make a seperate program that went through the json file and reformat according to [Django Docs](https://docs.djangoproject.com/en/4.0/howto/initial-data/)

- What did you learn? 
One thing I struggled with was updating an object without needing all fields.  I learned how to use the ```partial=True``` as seen here ```data = AttendeeSerializer(attendee, data=request.data, partial=True)```