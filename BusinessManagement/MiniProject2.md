<table><tr><td> <em>Assignment: </em> IS601 Mini Project 2  Business Management</td></tr>
<tr><td> <em>Student: </em> Mohan Krishna Kotha (mk994)</td></tr>
<tr><td> <em>Generated: </em> 12/5/2022 9:14:13 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/mk994" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>checkout dev and pull any latest changes</li><li>Create a branch called MiniProject-2</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li>Immediate add/commit/push to github</li><li>Open a pull request and keep it open until you're done adding the submission file</li><li>&nbsp;(optional) updated the deploy dev yml file and add MiniProject-2 so you can deploy to dev without needing to merge into dev</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item)<br></li><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 5</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together</li><li>Ensure all screenshots are properly captioned in the deliverable section</li></ol><li>You may save your progress when filling out this submission as often as you want</li><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from dev to prod and merge it</li><li>Navigate to the submission file under the BusinessManagement folder</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F22-MiniProject-2">https://github.com/MattToegel/IS601/tree/F22-MiniProject-2</a></div><div>May want to download branch as a zip, then copy/paste the files into your repo</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205746557-7a0553ff-8dba-4c94-a795-c23f3a7cbea3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>index page with my details<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/204156470-c0a2be2c-d673-448b-84ab-b4fea5c151f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>companies table screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/204156537-a82c766d-2dad-4e1a-a61f-9176a669fd8e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>employees table screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205523573-a699ea7e-9af5-4089-a51e-c1a57e22d3de.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code to check if the input file is csv or not<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205523646-33e9d11b-b4cb-4711-a0b2-86a203361b5a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>reading the csv file from stream, and appending the employee and company data<br>as dictionaries to respective lists<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205523811-c92b70e0-ecdb-4f9d-86cc-fc7118efa028.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for flash messages showing records processed or if the list is empty<br>that messagee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205747076-173a2488-0309-4280-8aaf-500a024e1a2b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>messages showing the number of companies &amp; employees being successfully imported<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205747550-c9586f0e-aa04-4db3-83c8-36f08dc4c1ab.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message when file is not .csv<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205747811-cfdd3062-b51f-4092-a03c-db7cf3ae0ad1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>message when the form is submitted without file attached<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205748185-d790141d-507d-491b-b6dd-604b973fd8f2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>companies data in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205748322-e22ebbc3-3411-4665-948c-09fca06e18a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>employees data in database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205524397-7dc6af19-c7c8-4ba6-ae51-b10616bb5e4e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for retreving the employee data and checking required fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205524501-046a6000-477f-40bf-8f8e-28bd0b89912b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>INSERT query and flash message code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205748717-4969a61c-6422-43fa-8d87-c5d175b9499d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>first name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205748985-c35567c8-d6b8-4d56-855e-98be5c5cd772.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205749275-4ec5eb0f-9566-487d-bdab-0a7872da34c0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>email error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205749480-6dd04d76-70c2-4d96-a275-319e2fc74922.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205750554-770a425d-b02d-46eb-99b8-7d288dc55726.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message for adding record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205750979-46349d9d-17f3-4ee0-8745-325e89353964.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>added employee data recorded iin database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205528448-9c4be16b-c958-4552-9896-7b4d838deacb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for SELECT query and request arguments<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205528867-af3233ba-e09f-4d0c-abaa-c5880a07b2ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for filters of fn,ln, email, order by and limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205528985-4f93a3a6-d288-4a7e-91d8-4960e15f7a5c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash message for exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205752187-84a6622e-7275-4f9a-a1d7-0596f5b3f437.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search results with first name filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205752591-1370bff0-3d43-4a1f-8143-5aadbbcbc9d1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search results with last name filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205752867-f644c3d3-e356-4bcc-a5a8-5bbf96393d0d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search results with email filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205753023-5bcad7cb-764e-473f-b22c-8a949b0a4094.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search results with company filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205753609-8337ba5e-7c77-42ba-833f-61d70fbe4b57.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last name field, aescnding field filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205754388-063a6fdf-f12f-41f5-8451-0082ed0b288d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>last name field, descnding field filter applied<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205786919-c20918b1-0bb5-4755-b52f-654be31d729c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for retrieving the form data and flash messages for the required data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205787198-8358621b-da2d-4559-8ddf-4c2260d749cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for UPDATE, SELECT queries and flash messages for exceptions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205755844-135fa747-7ab6-49d7-89bc-dcf1a9dcf00d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before an edit from website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205756762-0628f891-5706-4df0-a024-4f6472c48bbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after an edit from website<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205756199-75b5ca7b-98ef-4919-b30a-76abcfd32863.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before edit in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205762678-b5c3609c-b1d8-436e-8731-f1ebdc604c7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after edit in database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205529402-9d28e10d-aa8c-4598-ad30-85db310b75e3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for reteving the form data and checking the required fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205530491-ccb2ab7d-7c0c-4bc3-817f-442314b753a0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Insert query to add company and flash message for exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205763322-e82db747-a906-4fcd-a3f0-22cf1c46ee0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205763448-d7f82de0-9812-41ad-bd23-6eb1a0ad7c30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205763953-369d2790-a22b-49ff-b94c-da4d589e2e09.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>name error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205764164-e3629e64-2f44-4cae-8ce5-f1c613c3567b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>address error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205764303-a55d237a-9024-4274-bd8e-a997ec3410ee.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>city error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205764593-de92bcfd-6893-4d36-afc1-3a3b9fc27653.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205765722-5721bee3-9b82-4d03-8a97-62fe685aeba4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>country error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205766172-606462ef-00d4-49fc-a22f-1bdff39720dc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data included in database<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205530856-96846087-b73a-4501-a6ba-9b63f2947f53.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for select query and arguments<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205531095-0e4b1b5c-49d0-44c1-b9d5-652bd4cb9234.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for appending the required filter and LIMIT flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205531289-457bcc0e-1d17-4b52-97cc-d5aaec270628.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash message for exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205767319-b6fe6cd3-872d-4e7b-9455-9b23d0b2472f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search results with name filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205768185-d5c7c601-f86a-4f3a-98b7-c7833cb3ffd3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search results with company filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205768353-bb1ea8c6-1bc4-466b-81a3-9e724a1373b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search results with state filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205769116-fe163338-d7e4-40b9-a293-b258a3e90542.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>search results with company filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205769360-f7b6a8fd-8673-49ef-95f3-1363292ba034.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>ascending filter applied on state column <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205769591-633ddcc5-ed31-4109-882e-2bfd4e6a76e9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>descending filter applied on state column<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205787457-e223eefc-bce3-4d2e-a9d5-2ee368cd605e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for retrieving the form data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205787587-1857cca0-97f5-40f9-905a-856926b49821.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for flash messages of required fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205787743-765cf294-bca9-432f-819f-720fde36d60b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for UPDATE, SELECT queries and flash messages for exceptions<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205780763-8cbff05f-c6a8-4c29-8bb2-6b5dce96e947.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company data before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205781995-67893080-a02b-44b6-896b-d1dda4de6f08.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company data after edit<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205782778-880af646-4fbd-4312-b20f-3c9d56c35a7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company data before edit in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205782655-797ea11c-5bb1-419e-bbbf-a67fcfa49830.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company data after edit in database, updates city, state and zip<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205531556-13a52026-0338-4aa7-ac2e-fbfa7f33884e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for delete employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205783701-316dfd5a-8adf-402f-843e-14f3f611cff2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before deleting in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205783857-4c917543-d989-4cb6-8ffc-a90babc045fd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after deleting the record 3 in website and success message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205531839-5bf71da3-22d5-456b-bfd9-f72b72c3c6a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for deleting company<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205784494-13db4c2d-fe85-42eb-ab1f-8c4ee979fe9b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data before deleting in website<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205784807-8235c23b-3d94-4c06-938c-f3336d8b9fff.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>data after deleting the record 4 in website and success message flashing<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/205791817-91be4a7d-241a-44fe-ac47-626462b228cd.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing test case results<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>Learnt the flask templates, views and all.&nbsp;<div>learnt textWrappper reading&nbsp;</div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-mini-project-2-business-management/grade/mk994" target="_blank">Grading</a></td></tr></table>