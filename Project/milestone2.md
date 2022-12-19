<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 Shop Project</td></tr>
<tr><td> <em>Student: </em> Mohan Krishna Kotha (mk994)</td></tr>
<tr><td> <em>Generated: </em> 12/19/2022 9:26:43 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/mk994" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Users with admin or shop owner will be able to add products </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of admin create item page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208201593-beac8973-da68-4299-9b29-a343317fd4d9.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>add item page with valid data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of populated Products table clearly showing the columns</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208201730-99d30a93-4120-46f2-b10d-06085c46c1a1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing the products table from DB with filled data<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly describe the code flow for creating a Product</td></tr>
<tr><td> <em>Response:</em> <p>After entering the values in the add page, the values go to the<br>item function in shop.py. It checks whether an id is passed to check<br>if the action is to edit or add. As no id will be<br>passed this is a create action and a INSERT statement is executed passing<br>the values to Products table and is success a flash is displayed.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/34">https://github.com/mohankrishna99/IS601-005/pull/34</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/admin/item">https://is601-mk994-finalproj-prod.herokuapp.com/admin/item</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Any user can see visible products on the Shop Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the Shop page showing 10 items without filters/sorting applied</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208264597-3af14066-d500-453c-ae8f-e906d8e7af32.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop page with items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208264620-b22fcb03-9677-4c9e-a2ae-9b60dea0fce4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop page with items<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208264636-c64fff1e-c383-4290-b7e8-18c25f8ecfdb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop page with items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Shop page showing both filters and a different sorting applied (should be more than 1 sample product)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208265579-d249a469-0813-4e05-97ab-46353cd63595.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>shop results with category &quot;Clothing&quot; filter and price: High to Low sorting applied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the filter/sort logic from the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208265713-097dde80-12fd-461c-9936-7f59d1ae135d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>code showing filter/sort logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Briefly explain how the results are shown and how the filters are applied</td></tr>
<tr><td> <em>Response:</em> <p>For the shop page,&nbsp; initially we get the items &amp; details from Products<br>table whose visibility is 1.&nbsp;<div>and in the page we can search by name<br>or select a category or sort on price &quot;High to Low&quot; or &quot;Low<br>to High&quot;.<br>When we search using one/all of the above option. we go to<br>shop_list function in shop.py and based on the input we add a where<br>condition to the query. and display the results again.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/37">https://github.com/mohankrishna99/IS601-005/pull/37</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/shop">https://is601-mk994-finalproj-prod.herokuapp.com/shop</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Show Admin/Shop Owner Product List (this is not the Shop page and should show visibility status) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of the Admin List page/results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208278928-03925ccb-3bbc-4e5a-bfa3-1c1690f4ff55.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin view of products list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain how the results are shown</td></tr>
<tr><td> <em>Response:</em> <p>We select all fields from Products table without any filter and pass it<br>to the html page.<br>As no where condition is specified, every product will be<br>displayed irrespective of visibility status<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/39">https://github.com/mohankrishna99/IS601-005/pull/39</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/admin/items">https://is601-mk994-finalproj-prod.herokuapp.com/admin/items</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin/Shop Owner Edit button </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the edit button visible to the Admin on the Shop page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208313995-165ba059-6595-4aa7-9a06-099a41d38a2e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button for admin on shop page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the edit button visible to the Admin on the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208314488-113bfb8b-5975-4001-85e7-c1a5b71d7128.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit button in item details page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot showing the edit button visible to the Admin on the Admin Product List Page (The admin page)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208314526-254af5cf-89df-4ca4-99e9-8456efd36525.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>admin list page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after screenshot of Editing a Product via the Admin Edit Product Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208314570-a9dfb3f9-abcf-4c04-9d09-fac07bd08e07.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>edit page before edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208314614-c3c9513f-0177-448f-8b3d-b2cfcb03d7c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>updated the stock to 5 and price to 1.5<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <p>For the <b>Shop</b>&nbsp;page,&nbsp;<div>in shop.html at the end of every product we check if<br>the user is logged in and if the user is a admin, if<br>both are true we display a edit button which redirect to item page<br>with the product details.<br>Same for item details page, if the user is a<br>admin we display the edit button.<br>The admin items page has edit button default<br>as the page is only accessed by admin.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/40">https://github.com/mohankrishna99/IS601-005/pull/40</a> </td></tr>
<tr><td> <em>Sub-Task 7: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/itemdetails?id=1">https://is601-mk994-finalproj-prod.herokuapp.com/itemdetails?id=1</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Product Details Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the button (clickable item) that directs the user to the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208318672-86fefce9-b612-444d-a601-74cc15da7d58.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>view of shop page, clicking on name of the product it takes you<br>to the product details page.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the result of the Product Details Page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208319890-6fde156b-5b42-4210-bb85-b68ee8fe0f90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>product details page of 2nd item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the code process/flow</td></tr>
<tr><td> <em>Response:</em> <div>Created itemdetails.html &amp;&nbsp; itemdetails function for this.</div>Made the product name clickable, when clicked<br>will pass the product id to itemdetails function and get all details from<br>Products table passing the id and render them in the itemdetails page.<br><br><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/42">https://github.com/mohankrishna99/IS601-005/pull/42</a> </td></tr>
<tr><td> <em>Sub-Task 5: </em> Add a direct link to heroku prod for this file (can be any specific item)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/itemdetails?id=2">https://is601-mk994-finalproj-prod.herokuapp.com/itemdetails?id=2</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add to Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot of the success message of adding to cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208322430-2079dcb1-297c-4c20-8f06-202d059966b5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>success message upon adding to cart<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the error message of adding to cart (i.e., when not logged in)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208322526-4ba3eb40-a482-435d-8a18-454139bcf29d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>error message when a user is trying to add to cart without logging<br>in<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Cart table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208322483-c7443f05-7331-4fc1-9bff-9e8eff98d2ca.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cart table from Database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Tell how your cart works (1 cart per user; multiple carts per user)</td></tr>
<tr><td> <em>Response:</em> <p>1 cart per user, having product_id &amp; user_id as composite unique key<br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Explain the process of add to cart</td></tr>
<tr><td> <em>Response:</em> <p>Clicking the ADD button, the product id as hidden field, quantity field gets<br>submitted to cart function in shop.py,&nbsp;<div>and as the product id is passed and<br>quantity is greater than 0, we insert the product id, user id, desired<br>quantity, and unit_price(fetching it from products table)</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/45">https://github.com/mohankrishna99/IS601-005/pull/45</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> User will be able to see their Cart </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the Cart View</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208322983-2911a76b-da2e-4a5c-b99b-4a90f1382a8c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>screenshot showing the cart with products.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain how the cart is being shown from a code perspective along with the subtotal and total calculations</td></tr>
<tr><td> <em>Response:</em> <p>When we click the cart, the cart function checking there is no product<br>id being passed knows that this is not a add or update function<br>and goes to SELECT block getting, id, product id, name, desired quantity and<br>calculates the subtotal multiplying the desired quantity and unit_price in select statement only,<br>passing user id. and passes these values to cart.html.<div>For the total calculation,&nbsp;</div><div>we render<br>each item as a row in table in the HTML output and and<br>for every row we add the subtotal value to the a variable ns.total<br>and later display it as Total in the bottom.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/46">https://github.com/mohankrishna99/IS601-005/pull/46</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a direct link to heroku prod for this file</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/cart">https://is601-mk994-finalproj-prod.herokuapp.com/cart</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> User can update cart quantity </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a before and after screenshot of Cart Quantity update</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208324247-3b2ce6a9-44ce-4413-abf3-0bbcf880068c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before updating the quantity<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208324300-daec11ae-5797-4490-985c-eba7ec956caa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after updating the quantity of Noodles to 2<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show a before and after screenshot of setting Cart Quantity to 0</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208324331-92b5cb5e-5d7f-4d6d-9f2c-1a3b26457f94.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before updating the quantity to zero<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208324393-f4faa48b-c97e-47e5-aa2f-a465ae8d9165.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after updating the quantity of earbuds to zero, so it got deleted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how a negative quantity is handled</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208324457-3d99711f-ca06-477f-a71f-bf4d646638f3.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>gave the HTML input quantity field a attribute min=&quot;0&quot;, so it does not<br>allow negative values<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain the update process including how a value of 0 and negatives are handled</td></tr>
<tr><td> <em>Response:</em> <p>In the cart,<div>Beside the quantity field &amp; update button a hidden product id<br>will be passed to the cart function when we click the update button.<br>And in the code if the quantity &gt; 0,&nbsp;<br>First we get the price<br>&amp; name from products table, then we update the quantity &amp; price in<br>cart table passing product id &amp; user id.</div><div>When we pass the 0 in<br>quantity field, as the quantity is less than 0, the code goes to<br>DELETE block, we delete the product from cart table passing product id &amp;<br>user id.</div><div><br></div><div>For the negative value handling in quantity field, we set the min<br>value for the input field as 0 in HTML.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/47">https://github.com/mohankrishna99/IS601-005/pull/47</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Cart Item Removal </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a before and after screenshot of deleting a single item from the Cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208330473-988a35a0-e0ef-44f9-8f20-4fa6933e9d66.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before deleting a single item<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208330515-eb84ba11-85de-4337-a50f-9bf57d39679f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after deleting a item<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after screenshot of clearing the cart</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208330601-710b3bd3-c51d-46fb-b0e9-e547da2e1770.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart before clearing it<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/67315458/208330632-6afb63c3-a8c1-43e2-978f-8fdeaa131efe.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>cart after clearing all items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how each delete process works</td></tr>
<tr><td> <em>Response:</em> <p>When deleting a single item in cart,<div>Beside the delete button, a hidden field<br>quantity of -1 will be submitted and in the cart function when the<br>quantity is less than zero, it processes the Delete query passing product id.</div><div><br></div><div>When<br>clearing the total cart,</div><div>we pass a variable delete_all equal to 1, and in<br>the cart function, if the delete_all value is True we delete the records<br>in Cart table passing user_id.</div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add related pull request link(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/mohankrishna99/IS601-005/pull/48">https://github.com/mohankrishna99/IS601-005/pull/48</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="http://via.placeholder.com/400x120/009955/fff?text=Complete"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p>Stuck at clearing the cart for some time, but later got the idea<br>to set a variable and passing it when clearing the cart, and checking<br>the value in code to do the rest of the work.<br><br>And the other<br>point stuck at is displaying the shop public page when no user is<br>logged in, initially did not write the if condition for authentication around edit<br>button and got an error at that place as without the user logged<br>in the code is checking for admin role in current user.<br>later added the<br>is_authenticated condition around admin condition.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-mk994-finalproj-prod.herokuapp.com/login">https://is601-mk994-finalproj-prod.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-005-F22/is601-milestone-2-shop-project/grade/mk994" target="_blank">Grading</a></td></tr></table>