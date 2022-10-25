<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - IceCream</td></tr>
<tr><td> <em>Student: </em> Mohan Krishna Kotha (mk994)</td></tr>
<tr><td> <em>Generated: </em> 10/24/2022 10:10:35 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/mk994" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216">https://gist.github.com/MattToegel/17d0ac833a03580d010ad92e83fc4216</a>&nbsp;</li><li>Put them into a subfolder in your repository folder (I called my folder IcecreamMachine)</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197427256-d1c37193-f3b5-4882-94f9-663798762efd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot shows the calculate_cost method code, looping through the inprogress_icecream list to calculate<br>the cost<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197427458-470d97fa-5381-46da-a30e-f793269e7f5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code shows how the currency is formatted to display<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <ol><li>To calculate the cost, first set the value of cost to zero and<br>then looped through the inprogress_icecream list to calculate the cost based on choices</li><li>currency<br>is formatted using format function to display two decimals --&gt; format(expected, '.2f')&nbsp;</li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197430998-4303671e-640a-46f3-9fe8-732fd86b41ea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot contains Outofstockexception, Invalidpayment exception and ExceededRemainingChoices exception<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197431362-3997944f-be5d-4fa0-b014-ab260eb85069.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot contains Needscleaningexception &amp; InvalidChoiceException<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197431954-94217c42-d640-4b49-ade2-b9b974f734ec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output showing how Outofstockexception and Invalidchoiceexception is working<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197432135-9d34c3c2-f982-4008-a6d8-b5740148abc5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output showing how Invalidpayment and ExceededRemainingChoices Exception are handled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197432419-1aef0313-393e-4285-aab8-132858fd1cc7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output showing how NeedsCleaning exception is handled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <ol><li><span style="font-size: 13px;">OutOfStockException:<br></span>when this exception is raised we print a message for user<br>to choose from the available options, saying the requested one is out of<br>stock</li><li><span style="font-size: 13px;">NeedsCleaningException:<br></span>when this exception is raised we ask for user input to<br>clean or not, if yes then the remaining_uses variable is set to USES_UNTIL_CLEANING,<br>if no is entered the same prompt is displayed again</li><li><span style="font-size: 13px;">InvalidChoiceException:<br></span>when this<br>raised, we print a message saying entered value is invalid &amp; ask again<br>to enter the choice</li><li><span style="font-size: 13px;">ExceededRemainingChoicesException:<br></span>when this is raised, we print a message<br>saying the choices for the stage is over and we move to next<br>stage i.e: if we exceeded the flavor choices move to the toppings, if<br>toppings is exceeded move to Pay stage.</li><li><span style="font-size: 13px;">InvalidPaymentException:<br></span>when this is raised, we<br>print a message entered values is incorrect and ask the user to enter<br>again.</li></ol><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197647684-5d85ef62-fb2f-49ee-bcdc-34b04f147835.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test -1 container must be the first selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197660221-132b7fd5-b138-4991-99bc-b8d9109ab6ef.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>tests 2 and 3<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197661235-71ad524d-940a-4a1a-9edc-d8dc10ba7977.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test 4 and 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197663019-f7f226c5-7f00-44cd-b95d-01ba2057d2db.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>test 6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197664336-a9e5f108-ee13-4e04-8ff9-e8c479077338.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>tests 7 &amp; 8<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <p>Test-1: <br>Container must be the first selection, we check for the first item<br>in inprogress_icecream list &amp; see if it is a container.<div>Test-2 &amp; 3:</div><div><span style="font-size:<br>13px;">can only add flavors &amp; toppings if they&#39;re in stock, we check if<br>the quantity available is greater than zero or not</span><br></div><div><span style="font-size: 13px;">Test-4 &amp; 5:</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;A maximum of 3 flavors and maximum of 3 toppings can be<br>added to the icecream, we check for the number of flavors and number<br>of toppings and if they are less than or equal to 3.</span></div><div><span style="font-size:<br>13px;">Test - 6:</span></div><div><span style="font-size: 13px;">based on the inputs we caluclate the cost using<br>method and check if it correct or not</span></div><div><span style="font-size: 13px;">Test -7 &amp; 8:</span></div><div>&lt;span<br>style=&quot;font-size: 13px;&quot;&gt;Based on the inputs provided for icecreammachine with two orders, we check<br>in the tests if the total sales &amp; total icecreams are being calculated<br>properly or not.</span></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/5">https://github.com/mohankrishna99/IS601-005/pull/5</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>writing the test cases for different functions &amp; scenarios has been difficult.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197445752-48d6519f-6231-456e-999f-35ce5b0c17fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>one output of icecream machine<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/197445873-0880cf01-3599-4e5e-ab30-9a8dc3551cb8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>output of icecream machine<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-1-icecream/grade/mk994" target="_blank">Grading</a></td></tr></table>