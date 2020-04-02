0. Team Members
Alan Luo - afl59

1. Implementation of LS tracking TS responses/timeout
The LS tracks which TS responds to the query by using the system "system" select call. The LS sets a timeout of 5 seconds,
after which the blocking call is removed and the program progresses as normal. The LS logic will examine the return
value of the select call and if a connection is returned, the LS will call recv() on that specific connection
and return the output to the client.

2. Known Issues
There are no currently known issues within this project.

3. Problems
One problem in developing for this project was determining how the LS should manage the logic of establishing the sockets for the ts.

4. Lessons
I learned that it would be prudent to decompose certain functions so as to reduce the total size of the code base.