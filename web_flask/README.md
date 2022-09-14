<div class="panel panel-default">
<div class="panel-heading">
<h3 class="panel-title">Concepts</h3>
</div>
<div class="panel-body">
<p><em>For this project, we expect you to look at this concept:</em></p>
<ul>
<li><a href="https://intranet.hbtn.io/concepts/74">AirBnB clone</a></li>
</ul>
</div>
</div>
<div id="project-description" class="panel panel-default">
<div class="panel-body">
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="What is a Web Framework?" href="https://intranet.hbtn.io/rltoken/iWopX7mh5JZI0BtpNmMOCA" target="_blank">What is a Web Framework?</a></li>
<li><a title="A Minimal Application" href="https://intranet.hbtn.io/rltoken/keZjRGkZxdJF8pjP-xNipg" target="_blank">A Minimal Application</a></li>
<li><a title="Routing" href="https://intranet.hbtn.io/rltoken/n7ASsk-KY_obWr4c9N2LZw" target="_blank">Routing</a>&nbsp;(<em>except &ldquo;HTTP Methods&rdquo;</em>)</li>
<li><a title="Rendering Templates" href="https://intranet.hbtn.io/rltoken/y41oKg4UFLTcCs8hElWg2g" target="_blank">Rendering Templates</a></li>
<li><a title="Synopsis" href="https://intranet.hbtn.io/rltoken/-JZxrxnDnOID141U1qDcew" target="_blank">Synopsis</a></li>
<li><a title="Variables" href="https://intranet.hbtn.io/rltoken/-qwqxJ6YyQ7Z9JvvPIE1AA" target="_blank">Variables</a></li>
<li><a title="Comments" href="https://intranet.hbtn.io/rltoken/TsdwbqCk1utlpeOhc5eUFg" target="_blank">Comments</a></li>
<li><a title="Whitespace Control" href="https://intranet.hbtn.io/rltoken/NR5WFn7I6qUTh-b70Od69Q" target="_blank">Whitespace Control</a></li>
<li><a title="List of Control Structures" href="https://intranet.hbtn.io/rltoken/pyvwBzYKgoDeNQ6_QIwUsw" target="_blank">List of Control Structures</a>&nbsp;(<em>read up to &ldquo;Call&rdquo;</em>)</li>
<li><a title="Flask" href="https://intranet.hbtn.io/rltoken/k2C-4UmlYXgA6oMgO7fLgg" target="_blank">Flask</a></li>
<li><a title="Jinja" href="https://intranet.hbtn.io/rltoken/fid5cMJKYMaRJqL60PlUew" target="_blank">Jinja</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/7F5n8fv5KctUYdvD0Aq9pQ" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions&hellip;)</li>
<li>How to display in HTML data from a MySQL database</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using&nbsp;<code>python3</code>&nbsp;(version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the&nbsp;<code>PEP 8</code>&nbsp;style (version 1.7)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code>&nbsp;and&nbsp;<code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
<h3>HTML/CSS Files</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A&nbsp;<code>README.md</code>&nbsp;file at the root of the folder of the project is mandatory</li>
<li>Your code should be W3C compliant and validate with&nbsp;<a title="W3C-Validator" href="https://intranet.hbtn.io/rltoken/nx649rCOtVwREiT1Y3VR9w" target="_blank">W3C-Validator</a>&nbsp;(except for jinja template)</li>
<li>All your CSS files should be in the&nbsp;<code>styles</code>&nbsp;folder</li>
<li>All your images should be in the&nbsp;<code>images</code>&nbsp;folder</li>
<li>You are not allowed to use&nbsp;<code>!important</code>&nbsp;or&nbsp;<code>id</code>&nbsp;(<code>#...</code>&nbsp;in the CSS file)</li>
<li>Current screenshots have been done on&nbsp;<code>Chrome 56.0.2924.87</code>.</li>
<li>No cross browsers</li>
</ul>
<h2>More Info</h2>
<h3>Install Flask</h3>
<pre><code>$ pip3 install Flask
</code></pre>
<p><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png" alt="" /></p>
<iframe src="https://www.youtube.com/embed/lzs4nQOiZQY" frameborder="0" width="560" height="315"></iframe>
<h3>Manual QA Review</h3>
<p><strong>It is your responsibility to request a review for this project from a peer before the project&rsquo;s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.</strong></p>
</div>
</div>