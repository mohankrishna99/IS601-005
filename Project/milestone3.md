<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 Shop Project</td></tr>
<tr><td> <em>Student: </em> Mohan Krishna Kotha (mk994)</td></tr>
<tr><td> <em>Generated: </em> 12/22/2022 11:29:25 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-3-shop-project/grade/mk994" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Orders will be able to be recorded </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Orders table with valid data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209239480-18f61949-93e6-4c29-bd6f-32dd41296468.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>orders table with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of OrderItems table with validate data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209239590-e949c4d7-bbd8-4408-89d9-51a2c90f36b3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>orderitems table with data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the purchase form UI from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209240553-3ade4873-a7fe-472f-ba61-a25b6850b123.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>purchase form with billing information and address<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot showing the items pending purchase from Heroku</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209240490-023e710f-f55f-40e9-98d0-6b8fcb4f9a32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>checkout form with item data before changing price<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209240723-a3b52a60-e94d-4f80-a8f2-db3fd8f497c4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>checkout form with item data after changing price showing the %difference<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a screenshot showing the Order Process validations from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209240953-d0f86b9b-4237-4f14-b8e9-315c1dc3309b.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code  showing validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209241072-9d2e8edf-c8e5-4cf4-9590-e8526eb05fd9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code verifying amount<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209241139-3075c9b4-053e-4c46-b70a-6dd304087730.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code updating stock<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a screenshot showing the Order Process validations from the UI (Heroku)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209241335-0f0cf180-638d-4f75-b85b-b13abf0798f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>price difference flash<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209241472-667179fb-c265-4895-9997-55f84d21b7d7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>stock flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209241543-d45cb890-3275-4f23-a897-31a241859745.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid amount flask<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Briefly describe the code flow/process of the purchase process</td></tr>
<tr><td> <em>Response:</em> <p>A new checkout.html page is created to ask for the billing &amp; shipping<br>information of the user.&nbsp;<div>When clicking on the proceed to checkout button it redirects<br>to checkout page asking the details.</div><div>After entering the information and clicking checkout the<br>order get validated checking the amount entered by user against the cart balance<br>and gives error if any,&nbsp;</div><div>it also checks the price of item in cart<br>against the price in products table, if any change we show it in<br>the output<br>and we check if the item is in stock and minus it<br>later.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 8: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/51">https://github.com/mohankrishna99/IS601-005/pull/51</a> </td></tr>
<tr><td> <em>Sub-Task 9: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/checko">https://is601-mk994-finalproj-prod.herokuapp.com/checko</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Order Confirmation Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot showing the order details from the purchase form and the related items that were purchased with a thank you message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209246462-312f214d-5154-4b3f-ad68-9fccda1eef91.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>order summary page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how this information is retrieved and displayed from a code logic perspective</td></tr>
<tr><td> <em>Response:</em> <p>we get the billing &amp; shipping information from the checkout and process that<br>information in this summary page, we also get the products table which are<br>in &amp; show here and display a personalized thank you message<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/53">https://github.com/mohankrishna99/IS601-005/pull/53</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/purchase">https://is601-mk994-finalproj-prod.herokuapp.com/purchase</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> User will be able to see their Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history for a user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209251471-e5ac871a-0b95-481b-b7cc-be41478a1952.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>orders history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209251556-de221596-ea07-4449-a4ef-23c626a1dcea.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>order details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details</td></tr>
<tr><td> <em>Response:</em> <p>when clicking on the order in navigation bar, the code gets the user<br>id and retrieves the orders from orders table with that userid and displays<br>that in purchase history, and when clicking view button we fetch the order<br>id and get the product details, &amp; display it.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/56">https://github.com/mohankrishna99/IS601-005/pull/56</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/orders">https://is601-mk994-finalproj-prod.herokuapp.com/orders</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Store Owner Purchase History </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing purchase history from multiple users</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209253663-c498f7f3-a385-46f2-92a9-2d176fc2a27a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin purchase history<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing full details of a purchase (Order Details Page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209253768-dabeab59-c2ca-466f-9156-7d5f891da4c6.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>order details<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the logic for showing the purchase list and click/displaying the Order Details (mostly how it differs from the user's purchase history feature)</td></tr>
<tr><td> <em>Response:</em> <p>when admin wants to see the purchase history we don&#39;t pass any user<br>id into orders table just retrieve all the orders from orders table and<br>display them.<br>and clicking on view button we get the order id and display<br>the products from orderitems table.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/57">https://github.com/mohankrishna99/IS601-005/pull/57</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/order?id=12">https://is601-mk994-finalproj-prod.herokuapp.com/order?id=12</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart page showing the button to place an order</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/209270360-a92ba4f0-5fcb-4f32-b541-c6cfceac9985.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>learnt about writting the if conditions in jinja templates and display different results<br>on conditions. And writting thenew html page and rendering tables and forms and<br>getting information.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-3-shop-project/grade/mk994" target="_blank">Grading</a></td></tr></table>