0. Team Members
Alan Luo - afl59

1. Recursive client functionality
The way that the client is implemented is that it first makes an initial request to the root-level server
Then, the client analyzes the response string. If the response string ends with an A, then the hostname
request has been resolved and the response is printed to the output file.

Otherwise, if the request ends with "NS", then the client takes the hostname provided in the response and
opens a socket connection to the specified host. It then makes the same request to that host and analyzes
its response. For this project, the response is printed to the output file no matter what, but normally,
the client would repeat this process everytime it found an NS in its response.

2. Known Issues
There are no currently known issues within this project.

3. Problems
One problem in developing for this project was determining how to conditionally create a new socket
connection based on the response from the root server.

4. Lessons
I learned that it is important to ensure that in every single part of your protocol, you are properly
formatting your messages between hosts so that everyone is working with the same information.