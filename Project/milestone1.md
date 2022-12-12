<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Mohan Krishna Kotha (mk994)</td></tr>
<tr><td> <em>Generated: </em> 12/11/2022 9:11:06 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/mk994" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206465277-895a8d19-3ba7-4502-a17c-cd39ed16605a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of password not match validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206465575-89f38127-6c64-489d-a134-21f185bc3788.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of username not available<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206465928-8c38f6e1-18e8-4916-90a6-be978f9ff2f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid email validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206466368-19d92dc1-95ad-4b0a-9106-04d8758a8fcc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206466622-4fa38ab9-0447-4e7e-86fc-a24b24893cea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>chosen email not available validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206467167-95922082-f092-4198-afd1-f5c33069957d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>valid data for form submission<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206467736-f3ea040e-112d-45f9-b603-9c05550578f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>registered user data recorded in database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/24">https://github.com/mohankrishna99/IS601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>We use WTforms for from generation and validation<div>2. WTform validatiors are used<br>to validate data both in frontend &amp; backend, username is validated to be<br>of length between 2 &amp; 30 characters and it shouldn&#39;t be previously be<br>used by another user, email validation is done using email validator.</div><div>3. password &amp;<br>confirm password should both be same and should be of length of 8,<br>This is validated using wtform validators and it is stored in database after<br>hashing it using bcrypt hashing algorithm</div><div>4.email, username and hashed password is stored in<br>the users table.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206469997-635e11d2-54fc-431a-b11f-13b3607e6020.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206470222-41a6584e-576c-460b-b392-5b3968029fd6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid user screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206470672-22a94849-5b03-439a-bdd2-38eeeb4d766a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>successful login of user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/24">https://github.com/mohankrishna99/IS601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>login form is handled using wt forms, this is similar to register<br>forms, but we will not use confirm pwd field and use username or<br>email field.<div>2. In the front end, if the username or email field checks<br>if data is entered or not, and if the field has &#39;@&#39; it<br>will use email validator else it checks for the username format, if the<br>length is between 2 &amp; 30 or not, and checks if password is<br>entered or not.&nbsp;</div><div>In the backend, we fetch the data from users table passing<br>email/username, if we get something we compare the password &amp;then check if user<br>is assigned roles</div><div>3. In the front end, we first check if password entered<br>&amp; then in back we fetch the password from database based on username/email<br>&amp; then check if the passwords match, if they match then we delete<br>the password from that point in the program.</div><div>4. we fetch username, email, password<br>from users table passing username/email, and then check if passwords match, and then<br>check if the user is assigned is any roles from userroles tables &amp;<br>fetch it.</div><br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206471077-11b64a8a-ac57-40a4-be68-7fe453b30123.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>user logged out successfully screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206485588-e5165489-6276-48f4-9ba4-c3dea4405474.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unauthorized access for logout user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/24">https://github.com/mohankrishna99/IS601-005/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p><span id="docs-internal-guid-cd249f26-7fff-0785-2f26-89e2cf5dae68">we use flask_login package to work with user session &amp; manage it,&nbsp;</span><div>&lt;span<br>style=&quot;font-family: Arial;&quot;&gt;<font size="2">In our main.py we’ll utilize LoginManager</font></span><span style="font-family: Arial; font-size: 12pt;">, t</span>&lt;span<br>style=&quot;font-size: small; font-family: Arial;&quot;&gt;his handles<br>     our user session and<br>provides helpful utilities</span><p style="margin: 0in; font-family: Arial;"><span style="background-image: initial; background-position: initial; background-size: initial;<br>background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;"><font size="2">Since we’re using an app<br>factory we’ll defined a<br>variable for login_manager outside of the factory, t</font></span><span style="font-size: small;">hen<br>inside the factory we use its init_app() method<br>to associate the app</span></p><ul type="disc" style="direction:ltr;unicode-bidi:embed;margin-top:0in;<br><br>margin-bottom:0in"></p><br></ul><br><br><p style="margin: 0in; font-family: Arial;"><span style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial;<br>background-attachment: initial; background-origin: initial; background-clip: initial;"><font size="2">Next, inside of the app factory we’ll<br>use the<br>user_loader decorator, t</font></span><span style="font-size: small;">his will run<br>     a<br>process to lookup a user by id</span></p><p style="margin: 0in; font-family: Arial;"><br></p><ul type="disc" style="direction:ltr;unicode-bidi:embed;margin-top:0in;<br><br>margin-bottom:0in"><br></ul></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206485588-e5165489-6276-48f4-9ba4-c3dea4405474.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>unauthorized access for logout user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206471447-1ab4cd89-a136-4d6c-a8e1-52ec85b3859c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>permission denied message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206485977-5019cbb3-170d-4b78-adc9-d7abfb1abfcf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>roles table with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206486244-16d3e092-3124-44df-8ef5-9dd527145d59.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>the only entry in userroles tables is my admin user(role id: -1) mapped<br>to the user with id: 3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/25">https://github.com/mohankrishna99/IS601-005/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <p><span style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial;<br>background-clip: initial; font-family: Arial;"><font size="2">Since we’re using an app factory we’ll defined a<br>variable for login_manager outside of the factory, t</font></span><span style="font-family: Arial; font-size: small;">hen inside<br>the factory we use its init_app() method to associate the app,&nbsp;</span><div><font face="Arial" size="2">For<br>the login protected pages, we decorate the views with @login_required function,&nbsp;</font>If the user<br>is not logged in, it calls the&nbsp;<a class="reference internal" href="https://flask-login.readthedocs.io/en/latest/#flask_login.LoginManager.unauthorized" title="flask_login.LoginManager.unauthorized" style="">&lt;span class=&quot;pre&quot;<br>style=&quot;hyphens: none;&quot;&gt;LoginManager.unauthorized</span></a>&nbsp;function.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <ol><br><li>similar to login protected page, here we use @admin_permission_require function from roles.permissions<br>package, If the user is not a admin,&nbsp; we raise 403 exception and<br>display 403 html page saying permission denied.<br></li><br></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206880227-1d9073e9-f6d7-4701-8901-94dc754a3b28.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot of navigation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206880252-923ccccb-aadc-48d5-8fa6-0da2486cd496.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>styled form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206880304-86d25d74-44e9-44ec-9c38-e43bb0329834.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>good UI<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206880324-ae3a8a86-b9a6-48a6-bc0e-fc89039bbd8b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>DB output display in a good manner<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/25">https://github.com/mohankrishna99/IS601-005/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>we use the styles from bootstrap,&nbsp;<div>navbars require a wrapping&nbsp;<span style="word-break: break-word;">.navbar</span>&nbsp;with&nbsp;<span style="word-break: break-word;">.navbar-expand-lg</span>&nbsp;for<br>responsive collapsing at large break point, and&nbsp;bg-light for color.<br><div><span style="word-break: break-word;">.navbar-brand</span>&nbsp;for the project<br>name.<br></div><div><span style="word-break: break-word;">.navbar-nav</span>&nbsp;for a full-height and lightweight navigation (including support for dropdowns).<br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206485588-e5165489-6276-48f4-9ba4-c3dea4405474.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>login protected pages saying to the user &quot;unauthorized&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206471447-1ab4cd89-a136-4d6c-a8e1-52ec85b3859c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>role protected pages saying to the user &quot;permission denied&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206465928-8c38f6e1-18e8-4916-90a6-be978f9ff2f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email validation saying to the user that &quot;@ is not there and it<br>is not email&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/25">https://github.com/mohankrishna99/IS601-005/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <p>we use flask error handler functions for 403 &amp; 404 errors, and at<br>most places we see what code is doing in backend and write a<br>flash message for that, if any field is missing or else other.<div><div><br></div></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206488361-d5f4a7e3-dd91-444c-afac-85999d28d6fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>profile page with email and username prefilled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/26">https://github.com/mohankrishna99/IS601-005/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <p>when profile page is opened, if it is not a POST request then<br>email, username are fetched from users table passing user id, then the are<br>rendered into the profile form.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206881889-a25fa373-7086-4956-bde0-6d45128aaea3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>username validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206881923-2a31b92d-3bcc-495f-9880-30d03ff122b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206557430-e9077b44-9fe3-4451-bf0b-793338dede30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206555756-703b5a2f-db01-45db-8ac8-8a4426ee6650.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206489629-c10b2a09-31b1-428a-8380-6284ef5f0fbb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email already in use<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206558959-a950a269-6adc-44ac-8693-e38825d0f388.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before profile edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/206559226-41db7eec-f93b-4fc0-91bf-65a5deac578d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after edit, edited the email &amp; username<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/26">https://github.com/mohankrishna99/IS601-005/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <p>the code first checks for if it is POST request, if it is,<br>then it checks if current_password, password &amp; confirm are given, then it retrieves<br>password from users table, then the current password &amp; pwd from DB are<br>compared to check if they are the same or not, if they are<br>not same we will raise a invalid password flask, if they are same<br>then the new password is hashed &amp; updated in the database.<div>Then the username<br>&amp; email are updated in the database and a flash message &quot;saved profile&quot;<br>is displayed.</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Learned how the flask_login works &amp; how loginmanager is used for sessios &amp;<br>all, referred from flask_login documentation. and also how error handlers work for known<br>errors like 403 &amp; 404.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/login">https://is601-mk994-finalproj-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone1-deliverable/grade/mk994" target="_blank">Grading</a></td></tr></table>