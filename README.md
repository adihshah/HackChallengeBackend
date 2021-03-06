# Runner

Get hired any day, any time.

# [Link to iOS Git Repo](https://github.com/Kompella/Runner)

# Screenshots of Runner

![Opening Frame][opening_frame] ![Profile][profile] ![Sign Up][sign_up]
![Job Posting][job_posting] ![Create Job][create_job] ![Job Confirmation][job_confirmation]
![Delete Job][delete_job] 
![Home Screen with Job][home_screen] ![Job Poster][job_poster] ![Report][report]
![Job Details][job_details] ![You're Hired!][youre_hired] ![Your Runner][your_runner]

[opening_frame]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/opening_frame.png "Opening Frame"
[profile]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/2_profile.png "Profile"
[sign_up]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/sign_up.png "Sign Up"
[job_posting]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/1_job_posting.png "Job Posting"
[create_job]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/3_creating_job.png "Create Job"
[job_confirmation]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/job_confirmation.png "Job Confirmation"
[delete_job]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/delete_job.png "Delete Job"
[home_screen]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/home_screen_on_job.png "Home Screen W/ Job"
[job_poster]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/6_opposite_user.png "Job Poster"
[report]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/report.png "Report"
[job_details]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/4_details_of_job.png "Job Details"
[youre_hired]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/5_feedback_accepting.png "You're Hired!"
[your_runner]: https://github.com/adihshah/HackChallengeBackend/blob/master/images/your_job_confirm.png "You got a runner!"

# Description of Runner

> Don't you have those lazy days when you don't want to move? However, you are really hungry and really want food from like collegetown, but you live on north campus... If this is not the case, is it the case that you want some money? Sometimes, finding a job on campus can be tough, especially one with very little commitment. Well, if you can relate to any of these, then this is the app for you! With Runner, you can post a job to get Collegetown Bagel or Utea. Anyone with the app can accept the job and get the food for you! This is a win win app for both the job poster at home or even in the library and for the runner who needs some quick cash. Not only does this app support food delivery, but it also branches out all other kinds of small jobs. For example, you can post a job to take some pictures of a textbook for a few bucks. Of course, this app currently relies on the integrity of both parties. Sign up for an account today!

# iOS Requirements

* We have used SnapKit to contraint each of the elements on the screen
* The API integration allows users to currently post and view jobs. They are also able to reload jobs to be upto date with any new updated jobs
* A TableView was used in two screens. One to actually display all the jobs and the other to create jobs.
* A navigation controller allows users to move between screens. Screens are also presented modally in this app.

_The goal of the app, would be to further implement functionality and allow users to actually accept and do jobs with OAuth!_

# Backend Requirements

## API Design:

**_GET /api/jobs/_** - Get all jobs

> This gets all the jobs that is currently available for anyone to grab.

**_POST /api/job/{user_id}/_** - Create a job for a specific user

> Creates a job for runners to see/accept.

**_GET /api/user/{user_id}/_** - Get a specific user

> Get a user's profile information

**_DELETE /api/job/delete/{job_id}/_** - Delete a job BEFORE it’s completed

> Remove a job from the listing. This can be useful if a job is no longer needed or a job was created by accident.

**_DELETE /api/job/finished/{job_id}/_** - Complete a job

> When a job is completed, the job is moved to the poster's job history of past job creations and each user's infomation is changed accordingly. 

**_POST /api/user/{user_id}/_** - Update a user’s information

> If someone wants to change their profile information, this is the endpoint to do so. If no information is provided, nothing is changed. 

**_POST /api/job/{job_id}/edit/_** - Update Job Information

> If someone posted a job, but information needs to be changed, this is the endpoint to do so. If no information is provided, nothing is changed. 

**_POST /api/user/{user_id}/job/{job_id}/_** - Assign a runner to a job

> When a runner wants to accept a job, this is where you send the information of which user to which job. 

**_POST /api/signup/_** - Create a user (signing up)

> Sign a user up if the user doesn't already exist. Password is encrypted.

**_POST /api/login/_** - Logging in for a user

> Log a user into the app. 

**_POST /api/update/session_** - Update session of a user

> Update the session of a user currently on the app. 


## Deployment to Google Cloud:

Deployed on ip address: _35.227.99.222_

# Additional Comments

The iOS github repo had an issue, so it is uploaded in the form of a zip file. As for the next steps of this project, we'd like to have an in-app messaging system that'll allow users to interact with each other without calling on another external app, via phone call which is currently the only option. Also, we would like multiple sign ups such as google sign up and facebook sign up. We'd like to implement actual paypal or venmo payment system, since it's a large part of this app. Upholding the integrity of each user is one of the hardships, but privacy is an important role to this app. These are only a few of the possible further steps to this app. 
